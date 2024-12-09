import json
import shopify
from ebaysdk import shopping
import json

from odoo import http
from odoo.http import request
import requests

class MerchandisingCustomer(http.Controller):
    @http.route("/md/customer", methods=['GET'], auth="public")
    def get_all_shopify_customer(self, **kw):
        store = request.env["md.shopify.store"].sudo().search([('store_url', '=', kw.get('store_url'))])
        customers = request.env["md.customer"].sudo().search([('store', '=', store.id)])
        customer_data = []
        for customer in customers:
            customer_data.append({
                'email': customer.email,
                'phone': customer.phone,
            })
        return json.dumps({
            'customer_data':customer_data
        })
