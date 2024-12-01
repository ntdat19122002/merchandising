from datetime import datetime, timedelta

import shopify

from odoo import models, fields
topics = {
    "product_update": {
        "name": "products/update",
        "path": "/webhook/merchandising/product/update"
    },
    "uninstall": {
        "name": "app/uninstalled",
        "path": "/webhook/merchandising/uninstalled"
    },
    'product_delete': {
        'name': 'products/delete',
        'path': '/webhook/merchandising/product/delete'
    },
}

class MdShopifyStore(models.Model):
    _name = 'md.shopify.store'

    name = fields.Char()
    email = fields.Char()
    store_url = fields.Char()
    primary_domain = fields.Char()
    install_status = fields.Boolean(default=True)
    timezone = fields.Char()
    shopify_access_token = fields.Char()
    shop_id = fields.Char()
    currency = fields.Char()
    first_install = fields.Boolean(default=True)
    webhook_updated = fields.Boolean(default=True)
    webhook_ids = fields.Char()
    primary_locale = fields.Char()
    country = fields.Char()
    phone = fields.Char()
    current_app_installation = fields.Char()

    plan_version = fields.Integer(string="Plan Version", default=1)
    plan_id = fields.Many2one('md.plan')
    is_test_charge = fields.Boolean(default=False)
    start_trials_date = fields.Datetime()
    billing_on = fields.Char(string='Billing On')
    last_check_plan = fields.Float(string='Last Check Plan', default=1)

    def init_merchandising_shopify_session(self):
        api_version = self.env["ir.config_parameter"].sudo().get_param("merchandising.md_api_version")
        new_session = shopify.Session(version=api_version, token=self.shopify_access_token, shop_url=self.store_url)
        shopify.ShopifyResource.activate_session(new_session)
        return new_session

    def update_store_info(self):
        self.init_merchandising_shopify_session()
        shop = shopify.Shop.current()
        data = {
            'email': shop.email,
            'timezone': shop.timezone,
            'name': shop.name,
            'currency': shop.currency,
            'primary_domain': shop.domain,
            'shop_id': shop.id,
            'country': shop.country,
            'primary_locale': shop.primary_locale,
            'phone': shop.attributes['phone'] if shop.attributes['phone'] else False
        }
        self.sudo().write(data)
        return True

    def register_webhook(self):
        try:
            self.ensure_one()
            webhook_ids = []
            session = self.init_nest_pv_variant_shopify_session()
            existing_webhooks = shopify.Webhook.find(limit=100)
            webhook_base_url = self.env["ir.config_parameter"].sudo().get_param("merchandising.md_webhook_base_url")
            if not len(existing_webhooks) > 0:
                for t in topics:
                    topic = topics[t]
                    full_path = webhook_base_url + topic["path"] + "/" + str(self.id)
                    webhook = shopify.Webhook()
                    webhook.topic = topic["name"]
                    webhook.address = full_path
                    webhook.format = "json"
                    webhook.save()
                    if webhook.id:
                        webhook_ids.append(webhook.id)
                if len(webhook_ids) > 0:
                    self.webhook_ids = ",".join(map(str, webhook_ids))
        except Exception as e:
            return False
        shopify.ShopifyResource.clear_session()

    def get_current_plan(self):
        if not self.plan_id:
            freePlan = self.env['pv.plan'].search([('price', '=', 0), ('plan_version', '=', self.plan_version)],
                                                  limit=1)
            self.plan_id = freePlan.id
        billing_on_start = datetime.now()
        if not self.billing_on:
            start = datetime.now()
            if self.start_trials_date:
                billing_on_start = self.start_trials_date + timedelta(days=8)
            billing_on_end = start + timedelta(days=30)
            next_billing = billing_on_end + timedelta(days=1)
        else:
            billing_on_start = datetime.strptime(self.billing_on, '%Y-%m-%d') - timedelta(days=30)
            billing_on_end = datetime.strptime(self.billing_on, '%Y-%m-%d')
            next_billing = billing_on_end + timedelta(days=1)
        return {
            'id': self.plan_id.id,
            'name': self.plan_id.name,
            'price': self.plan_id.price,
            'is_free_trial': (fields.datetime.now() - self.start_trials_date).days if self.start_trials_date else True,
            'billing_on_start': billing_on_start.strftime('%Y-%m-%d'),
            'billing_on_end': billing_on_end.strftime('%Y-%m-%d'),
            'next_billing': next_billing.strftime('%Y-%m-%d')
        }