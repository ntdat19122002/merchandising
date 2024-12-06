from odoo import models,fields

class MerchandisingReview(models.Model):
    _name = 'md.review'

    store = fields.Many2one('md.shopify.store')
    product = fields.Many2one('md.shopify.product')
    rating = fields.Integer()
    description = fields.Text()