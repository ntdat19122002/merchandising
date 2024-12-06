from odoo import http, fields,models


class MerchandisiongReview(models.Model):
    _name = 'md.shopify.product'

    store = fields.Many2one('md.shopify.store')
    stars = fields.One2many('md.review', 'product')
    shopify_id = fields.Char()