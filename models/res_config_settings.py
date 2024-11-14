import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    md_api_key = fields.Char("API Key", config_parameter="merchandising.md_api_key")
    md_api_secret_key = fields.Char("Secret Key", config_parameter="merchandising.md_api_secret_key")
    md_api_version = fields.Char("API Version", config_parameter="merchandising.md_api_version")
    md_webhook_base_url = fields.Char("Webhook URL", config_parameter="merchandising.md_webhook_base_url", default="")
    md_password_master = fields.Char('Password Master', config_parameter='merchandising.md_password_master')
