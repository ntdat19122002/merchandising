import json
import shopify
from ebaysdk import shopping

from odoo import http
from odoo.http import request
import requests

class MerchandisingProduct(http.Controller):
    @http.route("/md/shopify/product/all", methods=['POST'],type='json', auth="public")
    def fetch_all_shopify_product(self, **kw):
        store = request.env["md.shopify.store"].sudo().search([('store_url', '=', kw.get('store_url'))])
        store.init_merchandising_shopify_session()
        products = shopify.Product().find()
        product_data = []
        for product in products:
            product_find_by_shopify_id = request.env["md.shopify.product"].sudo().search([('shopify_id', '=', product.id)])
            if not product_find_by_shopify_id:
                product_find_by_shopify_id = request.env["md.shopify.product"].sudo().create({
                    'shopify_id':product.id,
                    'title': product.title,
                    'store':store.id,
                    'image_url': product.image.src if product.image else None,
                    'url':f'https://{store.primary_domain}/products/${product.handle}'
                })
            else:
                product_find_by_shopify_id.write({
                    'title': product.title,
                    'image_url': product.image.src if product.image else None,
                    'url':f'https://{store.primary_domain}/products/{product.handle}'
                })
            product_data.append({
                'id': product_find_by_shopify_id.id,
                'shopify_id': product_find_by_shopify_id.shopify_id,
                'title': product_find_by_shopify_id.title,
                'image_url': product_find_by_shopify_id.image_url,
                'url': product_find_by_shopify_id.url
            })
        return json.dumps({
            'product_data': product_data
        })

    @http.route("/md/shopify/product", methods=['GET'], auth="public")
    def get_all_shopify_product(self, **kw):
        store = request.env["md.shopify.store"].sudo().search([('store_url', '=', kw.get('store_url'))])
        products = request.env["md.shopify.product"].sudo().search([('store', '=', store.id)])
        product_data = []
        for product in products:
            product_data.append({
                'id': product.id,
                'shopify_id': product.shopify_id,
                'title': product.title,
            })
        return json.dumps({
            'product_data': product_data
        })