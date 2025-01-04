from odoo import http, fields,models


class MerchandisiongReview(models.Model):
    _name = 'md.shopify.product'

    title = fields.Char()
    description = fields.Text()
    image_url = fields.Char()
    url = fields.Char()
    store = fields.Many2one('md.shopify.store')
    stars = fields.One2many('md.review', 'product')
    rate = fields.Float(compute='_compute_rate')
    shopify_id = fields.Char()

    def _compute_rate(self):
        for record in self:
            record.rate = 1