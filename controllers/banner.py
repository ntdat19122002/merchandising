import json

from ..utils.content_based_filtering import content_based
from odoo import http
from odoo.http import request
import requests

class MerchandisingJudgeMe(http.Controller):
    @http.route("/md/banner", methods=['GET'], auth="public")
    def banner_get_product(self, **kw):
        store = request.env["md.shopify.store"].sudo().search([('store_url', '=', kw.get('store_url'))])
        banner = request.env["md.banner"].sudo().search([('store', '=', store.id)])
        product_ids = content_based.recommend(1,3)
        for product_id in product_ids:
            product = request.env["md.shopify.product"].sudo().search([('id', '=', product_id.item())])
            if product:
                break
        return json.dumps({
            'product_img': product.image_url,
            'product_url': product.url,
        })