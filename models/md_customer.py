from odoo import models,fields

class MerchandisingReview(models.Model):
    _name = 'md.customer'

    store = fields.Many2one('md.shopify.store')
    shopify_customer_id = fields.Char()
    email = fields.Char()
    phone = fields.Text()
    ip_address = fields.Char()
    country = fields.Char()
    address = fields.Char()
    first_name = fields.Char()
    last_name = fields.Char()
    uuid = fields.Char()