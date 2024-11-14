import json
import logging
import traceback
from datetime import datetime

import shopify
from odoo import models, fields

_logger = logging.getLogger(__name__)


class MerchandisingPlan(models.Model):
    _name = "md.plan"

    name = fields.Char(string="Name")
    plan_version = fields.Integer(string="Plan Version")
    price = fields.Float(string="Price")
    product_page = fields.Boolean(string="Product Page")
    product_groups = fields.Boolean(string="Product Groups")
    collection_page = fields.Boolean(string="Collection Page")
    variant_image = fields.Boolean(string="Variant Image")
    features = fields.Text(string="Features")
    active_status = fields.Boolean(string="Active Status", default=True)

    def get_current_plan_version(self):
        return self.sudo().search([], limit=1, order='plan_version desc').plan_version

    def get_current_plan_list(self):
        result = []
        plans = self.sudo().search([('active_status', '=', True)])
        for plan in plans:
            result.append({
                'name': plan.name,
                'features': json.loads(plan.features),
                'price': plan.price,
                'id': plan.id,
                "product_groups": plan.product_groups,
                "collection_page": plan.collection_page
            })
        return result

    def get_current_plan(self):
        for rec in self:
            return {
                'name': rec.name,
                'price': rec.price,
                'id': rec.id
            }

    def get_charge_url(self, store):
        return_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url') + '/md/plan/accept' + '/' + str(
            store.id) + '/' + str(self.id)
        store.init_nest_md_variant_shopify_session()
        test_env = store.is_test_charge
        data_charge = {
            'name': self.name,
            'price': self.price,
            'return_url': return_url,
            'test': test_env,
        }
        if self.price > 0:
            trial_days = 7
            day_use = (fields.datetime.now() - store.start_trials_date).days if store.start_trials_date else 0
            if day_use < 0:
                day_use = 7
            trial_days = trial_days - day_use
            if trial_days > 0:
                data_charge['trial_days'] = trial_days
        charge = shopify.RecurringApplicationCharge.create(data_charge)
        shopify.ShopifyResource.clear_session()
        return charge.confirmation_url

    def activate_plan(self, charge_id, store):
        for rec in self:
            store.init_nest_md_variant_shopify_session()
            charge = shopify.RecurringApplicationCharge.find(charge_id)
            charge.activate()
            store.plan_id = rec.id
            store.plan_version = rec.plan_version
            if not store.start_trials_date:
                store.start_trials_date = datetime.now()
            store.billing_on = charge.attributes.get('billing_on') if charge and charge.attributes.get(
                'billing_on') else False
            if charge.status != 'active':
                raise Exception('Could not activate your plan. Please try again!')
            shopify.ShopifyResource.clear_session()
            return charge

    def set_shop_free_plan(self, store):
        for rec in self:
            store.plan_id = rec.id
            store.plan_version = rec.plan_version
            store.billing_on = False

    def cron_check_plan(self, limit=50):
        plans = self.get_current_plan_list()
        plan_ids = []
        for plan in plans:
            if plan['price'] > 0:
                plan_ids.append(plan['id'])
        current_timestamp = datetime.now().timestamp()
        stores = self.env['md.shopify.store'].sudo().search(
            [('plan_id', 'in', plan_ids), ('install_status', '=', True), ('last_check_plan', '<', current_timestamp)],
            limit=limit)
        for store in stores:
            try:
                store.check_plan()
                store.last_check_plan = int(current_timestamp) + 86400
            except Exception as e:
                store.last_check_plan = int(current_timestamp) + 86400
                _logger.error(traceback.format_exc())
                continue
        return True

    def check_plan_feature(self, feature):
        for rec in self:
            if hasattr(rec, feature):
                return getattr(rec, feature, None)
        return False
