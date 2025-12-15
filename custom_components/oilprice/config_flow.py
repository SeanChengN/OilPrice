"""Config flow for OilPrice integration."""
import logging
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers import config_validation as cv
from . import DOMAIN

_LOGGER = logging.getLogger(__name__)

class OilPriceConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for OilPrice."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        
        if user_input is not None:
            # 检查是否已经存在相同名称的配置
            await self.async_set_unique_id(user_input["name"])
            self._abort_if_unique_id_configured()
            
            # 创建配置条目
            return self.async_create_entry(
                title=user_input["name"],
                data=user_input
            )

        data_schema = vol.Schema({
            vol.Required("name", default="油价"): str,
            vol.Required("region", default="zhejiang"): str,
        })

        return self.async_show_form(
            step_id="user", 
            data_schema=data_schema, 
            errors=errors
        )
    
    async def async_step_import(self, import_config):
        """Handle import from YAML."""
        # 检查是否已经存在相同名称的配置
        await self.async_set_unique_id(import_config.get("name", "油价"))
        self._abort_if_unique_id_configured()
        
        return self.async_create_entry(
            title=import_config.get("name", "油价"),
            data=import_config
        )