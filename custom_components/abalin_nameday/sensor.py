"""Sensor platform for Abalin Nameday integration."""

from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType, DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)

from .const import CONF_COUNTRY, COUNTRY_NAMES, DOMAIN


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Abalin Nameday sensors from a config entry."""
    coordinator: DataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]
    country = entry.data[CONF_COUNTRY]
    country_name = COUNTRY_NAMES.get(country, country.upper())

    async_add_entities(
        [
            NameDaySensor(coordinator, entry, country, country_name, "today"),
            NameDaySensor(coordinator, entry, country, country_name, "tomorrow"),
        ]
    )


class NameDaySensor(CoordinatorEntity, SensorEntity):
    """Sensor representing today's or tomorrow's name day for a country."""

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: DataUpdateCoordinator,
        entry: ConfigEntry,
        country: str,
        country_name: str,
        day_key: str,  # "today" or "tomorrow"
    ) -> None:
        super().__init__(coordinator)
        self._country   = country
        self._day_key   = day_key

        # Unique ID: one per country + day combination
        self._attr_unique_id = f"{entry.entry_id}_{day_key}"

        # Translation key selects the right name from strings.json
        self._attr_translation_key = f"nameday_{day_key}"

        self._attr_icon = "mdi:account-star" if day_key == "today" else "mdi:account-clock"

        # Group both sensors under a single device page
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, entry.entry_id)},
            name=f"Nameday — {country_name}",
            manufacturer="Abalin",
            model="Name Day API",
            entry_type=DeviceEntryType.SERVICE,
            configuration_url="https://nameday.abalin.net/",
        )

    @property
    def native_value(self) -> str | None:
        """Return the nameday names."""
        if self.coordinator.data is None:
            return None
        return self.coordinator.data.get(self._day_key)

    @property
    def extra_state_attributes(self) -> dict:
        """Return extra attributes."""
        return {
            "country": self._country,
            "timezone": self.hass.config.time_zone,
        }
        