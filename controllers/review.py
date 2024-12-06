import json
from odoo import http
from odoo.http import request
import requests

class MerchandisingReview(http.Controller):
    @http.route("/md/review", methods=['POST'],type='json', auth="public")
    def create_review(self, **kw):
        store = request.env["md.shopify.store"].sudo().search([('store_url', '=', kw.get('store_url'))])
        product = request.env["md.shopify.product"].sudo().search([('shopify_id', '=', kw.get('product_shopify_id'))])
        review = request.env["md.review"].sudo().create({
            'store': store.id,
            'product': product.id,
            'rating': kw['rating'],
        })
        return ''