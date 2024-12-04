import json
from odoo import http
from odoo.http import request
import requests

class MerchandisingJudgeMe(http.Controller):
    @http.route("/judgeme/token", methods=['GET'], auth="public")
    def just_me(self, **kw):
        store = request.env["md.shopify.store"].sudo().search([('store_url', '=', kw.get('store_url'))])
        jugdeme = request.env["md.judge.me"].sudo().search([('store', '=', store.id)])
        if jugdeme:
            return json.dumps({
                'public_api_token': jugdeme.public_api_token,
                'private_api_token': jugdeme.private_api_token,
            })
        return ''

    @http.route("/judgeme/token", methods=['POST'], type='json', auth="public")
    def just_me_save_token(self, **kw):
        store = request.env["md.shopify.store"].sudo().search([('store_url', '=', kw.get('store_url'))])
        jugdeme = request.env["md.judge.me"].sudo().search([('store', '=', store.id)])
        if not jugdeme:
            request.env["md.judge.me"].sudo().create({
                'store': store.id,
                'public_api_token': kw['public_api_token'],
                'private_api_token': kw['private_api_token'],
            })
        else:
            jugdeme.write({
                'public_api_token': kw['public_api_token'],
                'private_api_token': kw['private_api_token'],
            })
        return "Hello, Just Me!"

    @http.route("/judgeme/reviews/products", methods=['POST'], type='json', auth="public")
    def just_me_reviews_product(self, **kw):
        store = request.env["md.shopify.store"].sudo().search([('store_url', '=', kw.get('store_url'))])
        jugdeme = request.env["md.judge.me"].sudo().search([('store', '=', store.id)])

        base_url = "https://judge.me/api/v1/reviews"
        params = {
            "shop_domain": store.primary_domain,
            "product_id": 8749435355411,
            "per_page": 1,
            "page": 1
        }

        headers = {"Authorization": f"Bearer {jugdeme.private_api_token}"}

        response = requests.get(base_url, headers=headers, params=params)

        if response.status_code == 200:
            reviews = response.json().get("reviews", [])
            for review in reviews:
                print(f"Reviewer: {review['reviewer_name']}, Rating: {review['rating']}, Comment: {review['body']}")
        else:
            print("Failed to fetch reviews:", response.status_code, response.text)

    @http.route("/judgeme/authentication", methods=['POST'], type='json', auth="public")
    def just_me_authentication(self, **kw):
        store = request.env["md.shopify.store"].sudo().search([('store_url', '=', kw.get('store_url'))])
        jugdeme = request.env["md.judge.me"].sudo().search([('store', '=', store.id)])
