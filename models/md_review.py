from odoo import models, fields, api


class MerchandisingReview(models.Model):
    _name = 'md.review'

    store = fields.Many2one('md.shopify.store')
    product = fields.Many2one('md.shopify.product')
    rating = fields.Integer()
    description = fields.Text()
    customer = fields.Many2one('md.customer')