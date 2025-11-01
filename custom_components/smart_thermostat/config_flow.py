"""Config flow for Smart Thermostat."""
from __future__ import annotations

import logging
import voluptuous as vol
from typing import Any, Dict, Optional

from homeassistant import config_entries
from homeassistant.const import (
    CONF_NAME,
    CONF_TEMPERATURE_UNIT,
    UnitOfTemperature,
    CONF_UNIQUE_ID,
)
from homeassistant.core import callback
from homeassistant.data_entry_flow import FlowResult
import homeassistant.helpers.config_validation as cv

from .const import (
    DOMAIN,
    DEFAULT_NAME,
    DEFAULT_TEMP_STEP,
    DEFAULT_TOLERANCE,
    DEFAULT_INITIAL_HVAC_MODE,
    DEFAULT_MIN_TEMP,
    DEFAULT_MAX_TEMP,
)

_LOGGER = logging.getLogger(__name__)

class SmartThermostatConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Smart Thermostat."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            # Validar y crear la entrada
            return self.async_create_entry(
                title=user_input[CONF_NAME],
                data=user_input
            )

        # Si no hay input, mostrar el formulario
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_NAME, default=DEFAULT_NAME): str,
                    vol.Required("heater_entity_id"): str,
                    vol.Required("temp_sensor_entity_id"): str,
                    vol.Optional("cooler_entity_id"): str,
                    vol.Optional("temp_step", default=DEFAULT_TEMP_STEP): vol.Coerce(float),
                    vol.Optional("tolerance", default=DEFAULT_TOLERANCE): vol.Coerce(float),
                    vol.Optional("min_temp", default=DEFAULT_MIN_TEMP): vol.Coerce(float),
                    vol.Optional("max_temp", default=DEFAULT_MAX_TEMP): vol.Coerce(float),
                    vol.Optional(CONF_TEMPERATURE_UNIT, default=UnitOfTemperature.CELSIUS): vol.In(
                        [UnitOfTemperature.CELSIUS, UnitOfTemperature.FAHRENHEIT]
                    ),
                }
            ),
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: config_entries.ConfigEntry,
    ) -> config_entries.OptionsFlow:
        """Get the options flow for this handler."""
        return SmartThermostatOptionsFlow(config_entry)


class SmartThermostatOptionsFlow(config_entries.OptionsFlow):
    """Handle options."""

    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Optional(
                        "temp_step",
                        default=self.config_entry.options.get(
                            "temp_step", DEFAULT_TEMP_STEP
                        ),
                    ): vol.Coerce(float),
                    vol.Optional(
                        "tolerance",
                        default=self.config_entry.options.get(
                            "tolerance", DEFAULT_TOLERANCE
                        ),
                    ): vol.Coerce(float),
                    vol.Optional(
                        "min_temp",
                        default=self.config_entry.options.get(
                            "min_temp", DEFAULT_MIN_TEMP
                        ),
                    ): vol.Coerce(float),
                    vol.Optional(
                        "max_temp",
                        default=self.config_entry.options.get(
                            "max_temp", DEFAULT_MAX_TEMP
                        ),
                    ): vol.Coerce(float),
                }
            )
        )