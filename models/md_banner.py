from odoo import models,fields

class MerchandisingReview(models.Model):
    _name = 'md.banner'

    store = fields.Many2one('md.shopify.store')
    description = fields.Char()
    product = fields.Many2one('md.shopify.product')