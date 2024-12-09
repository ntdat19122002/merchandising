from odoo import models,fields

class MerchandisingReview(models.Model):
    _name = 'md.event'

    customer = fields.Many2one('md.customer')
    event = fields.Char()
    context = fields.Char()
    data = fields.Text()