"""Constants for the Smart Thermostat component."""
from homeassistant.const import (
    ATTR_TEMPERATURE,
    CONF_NAME,
    CONF_UNIQUE_ID,
    UnitOfTemperature,
)

DOMAIN = "pid_pwm_smart_thermostat"

# Defaults
DEFAULT_NAME = "PID PWM Smart Thermostat"
DEFAULT_TEMP_STEP = 0.5
DEFAULT_TOLERANCE = 0.3
DEFAULT_MIN_TEMP = 7
DEFAULT_MAX_TEMP = 35
DEFAULT_INITIAL_HVAC_MODE = "off"

# Configuration
CONF_HEATER = "heater_entity_id"
CONF_COOLER = "cooler_entity_id"
CONF_SENSOR = "temp_sensor_entity_id"
CONF_MIN_TEMP = "min_temp"
CONF_MAX_TEMP = "max_temp"
CONF_TARGET = "target"
CONF_TOLERANCE = "tolerance"
CONF_TEMP_STEP = "temp_step"