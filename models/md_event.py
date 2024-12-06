from odoo import models,fields

class MerchandisingReview(models.Model):
    _name = 'md.event'

    store = fields.Many2one('md.shopify.store')
    shopify_customer_id = fields.Char()
    type = fields.Char()
    data = fields.Text()