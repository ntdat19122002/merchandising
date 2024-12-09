from odoo import models, fields


class MerchandisingReview(models.Model):
    _name = 'md.shopify.order'

    store = fields.Many2one('md.shopify.store')
    shopify_id = fields.Char(string='Shopify ID')
    type = fields.Char(string='Type')
