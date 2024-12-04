from odoo import models, fields

class MerchandisingJudgeMe(models.Model):
    _name = "md.judge.me"

    public_api_token = fields.Char()
    private_api_token = fields.Char()
    store = fields.Many2one('md.shopify.store')

