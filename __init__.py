"""Abalin Nameday integration — setup, DataUpdateCoordinator and services."""

from __future__ import annotations

import logging
from datetime import timedelta, datetime, timezone as dt_timezone

import aiohttp
import voluptuous as vol

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall, SupportsResponse
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import (
    API_BASE_URL,
    CONF_COUNTRY,
    COUNTRY_NAMES,
    DOMAIN,
    REQUEST_TIMEOUT,
    UPDATE_INTERVAL_MINUTES,
)

_LOGGER = logging.getLogger(__name__)

PLATFORMS = ["sensor"]

SERVICE_GET_NAMEDAY = "get_nameday_for_date"

SERVICE_SCHEMA = vol.Schema(
    {
        vol.Required("day"): vol.All(vol.Coerce(int), vol.Range(min=1, max=31)),
        vol.Required("month"): vol.All(vol.Coerce(int), vol.Range(min=1, max=12)),
        vol.Optional("country"): vol.In(list(COUNTRY_NAMES.keys())),
    }
)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Abalin Nameday from a config entry."""
    country  = entry.data[CONF_COUNTRY]
    timezone = hass.config.time_zone

    session = async_get_clientsession(hass)

    async def _async_fetch() -> dict:
        """Fetch today and tomorrow nameday data from the V2 API."""
        timeout = aiohttp.ClientTimeout(total=REQUEST_TIMEOUT)
        result: dict = {}

        # TODAY: GET /V2/today
        today_url = f"{API_BASE_URL}/V2/today"
        try:
            async with session.get(today_url, timeout=timeout) as resp:
                if resp.status != 200:
                    raise UpdateFailed(
                        f"Abalin API returned HTTP {resp.status} for today"
                    )
                data = await resp.json(content_type=None)
                result["today"] = _extract_names(data, country)
        except UpdateFailed:
            raise
        except Exception as exc:
            raise UpdateFailed(f"Error communicating with Abalin API: {exc}") from exc

        # TOMORROW: GET /V2/date?day=X&month=Y
        now = datetime.now(dt_timezone.utc)
        tomorrow = now + timedelta(days=1)
        try:
            async with session.get(
                f"{API_BASE_URL}/V2/date",
                params={"day": tomorrow.day, "month": tomorrow.month},
                timeout=timeout,
            ) as resp:
                if resp.status != 200:
                    raise UpdateFailed(
                        f"Abalin API returned HTTP {resp.status} for tomorrow"
                    )
                data = await resp.json(content_type=None)
                result["tomorrow"] = _extract_names(data, country)
        except UpdateFailed:
            raise
        except Exception as exc:
            raise UpdateFailed(f"Error communicating with Abalin API: {exc}") from exc

        return result

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name=f"{DOMAIN}_{country}",
        update_method=_async_fetch,
        update_interval=timedelta(minutes=UPDATE_INTERVAL_MINUTES),
    )

    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    # Register the service only once (first entry loaded)
    if not hass.services.has_service(DOMAIN, SERVICE_GET_NAMEDAY):
        await _async_register_services(hass)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    # Remove service when no entries remain
    if not hass.data.get(DOMAIN):
        hass.services.async_remove(DOMAIN, SERVICE_GET_NAMEDAY)

    return unload_ok


async def _async_register_services(hass: HomeAssistant) -> None:
    """Register the get_nameday_for_date service."""

    async def handle_get_nameday(call: ServiceCall) -> dict:
        """Fetch namedays for a specific day and month."""
        day     = call.data["day"]
        month   = call.data["month"]
        country = call.data.get("country")  # None -> return all countries

        session = async_get_clientsession(hass)
        timeout = aiohttp.ClientTimeout(total=REQUEST_TIMEOUT)

        try:
            async with session.get(
                f"{API_BASE_URL}/V2/date",
                params={"day": day, "month": month},
                timeout=timeout,
            ) as resp:
                if resp.status != 200:
                    _LOGGER.error(
                        "Abalin API returned HTTP %s for date %02d/%02d",
                        resp.status, day, month,
                    )
                    return {"error": f"API returned HTTP {resp.status}"}
                data = await resp.json(content_type=None)
        except Exception as exc:
            _LOGGER.error("Error fetching nameday for date: %r", exc)
            return {"error": str(exc)}

        if country:
            names = _extract_names(data, country)
            return {
                "day": day,
                "month": month,
                "country": country,
                "country_name": COUNTRY_NAMES.get(country, country.upper()),
                "names": names or "",
            }

        # No country specified — return all countries
        all_names = _extract_all_names(data)
        return {
            "day": day,
            "month": month,
            "namedays": all_names,
        }

    hass.services.async_register(
        DOMAIN,
        SERVICE_GET_NAMEDAY,
        handle_get_nameday,
        schema=SERVICE_SCHEMA,
        supports_response=SupportsResponse.OPTIONAL,
    )


def _extract_names(data: dict, country: str) -> str | None:
    """Extract nameday string for a specific country from the V2 API response."""
    if not data.get("success"):
        return None

    raw = data.get("data")

    if isinstance(raw, list):
        for item in raw:
            if isinstance(item, dict):
                if item.get("country") == country:
                    return item.get("name")
                if country in item:
                    return item[country]
        return None

    if isinstance(raw, dict):
        return raw.get(country)

    return None


def _extract_all_names(data: dict) -> dict[str, str]:
    """Extract namedays for all countries from the V2 API response."""
    if not data.get("success"):
        return {}

    raw = data.get("data")
    result: dict[str, str] = {}

    if isinstance(raw, list):
        for item in raw:
            if isinstance(item, dict):
                country = item.get("country")
                name    = item.get("name")
                if country and name:
                    result[country] = name
    elif isinstance(raw, dict):
        result = {k: v for k, v in raw.items() if isinstance(v, str)}

    return result
    