import json
import shopify
from ebaysdk import shopping

from odoo import http
from odoo.http import request
import requests

class MerchandisingReview(http.Controller):
    @http.route("/md/shopify/product/all", methods=['POST'],type='json', auth="public")
    def get_all_shopify_product(self, **kw):
        store = request.env["md.shopify.store"].sudo().search([('store_url', '=', kw.get('store_url'))])
        store.init_merchandising_shopify_session()
        products = shopify.Product().find()
        for product in products:
            if not request.env["md.shopify.product"].sudo().search([('shopify_id', '=', product.id)] ):
                request.env["md.shopify.product"].sudo().create({
                    'shopify_id':product.id,
                    'store':store.id
                })
        return ''