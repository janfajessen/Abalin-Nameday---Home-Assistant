"""Config flow for Abalin Nameday integration."""

from __future__ import annotations

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.helpers.selector import (
    SelectSelector,
    SelectSelectorConfig,
    SelectSelectorMode,
)

from .const import CONF_COUNTRY, COUNTRIES, COUNTRY_NAMES, DOMAIN


class AbalinNamedayConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle the UI config flow for Abalin Nameday."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict | None = None
    ) -> config_entries.FlowResult:
        """Show the setup form and handle submission."""
        errors: dict[str, str] = {}

        if user_input is not None:
            country = user_input[CONF_COUNTRY]

            # Prevent adding the same country twice
            await self.async_set_unique_id(country)
            self._abort_if_unique_id_configured()

            country_label = COUNTRY_NAMES.get(country, country.upper())
            return self.async_create_entry(
                title=f"Nameday — {country_label}",
                data={CONF_COUNTRY: country},
            )

        schema = vol.Schema(
            {
                vol.Required(CONF_COUNTRY): SelectSelector(
                    SelectSelectorConfig(
                        options=COUNTRIES,
                        mode=SelectSelectorMode.DROPDOWN,
                        translation_key="country",
                    )
                ),
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
            errors=errors,
        )
        