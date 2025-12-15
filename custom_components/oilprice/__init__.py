"""The OilPrice integration."""
import logging
import asyncio
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv

_LOGGER = logging.getLogger(__name__)
DOMAIN = "oilprice"

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the OilPrice component from YAML."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up OilPrice from a config entry."""
    _LOGGER.info("Setting up OilPrice entry: %s", entry.title)

    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
    
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    _LOGGER.info("Unloading OilPrice entry: %s", entry.title)
    
    unload_ok = await hass.config_entries.async_unload_platforms(entry, ["sensor"])
    
    return unload_ok

async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Reload config entry."""
    _LOGGER.info("Reloading OilPrice entry: %s", entry.title)
    await async_unload_entry(hass, entry)
    await async_setup_entry(hass, entry)
