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
            journeys = request.env['md.journey'].sudo().search([('customer', '=', customer.id)])
            total_spend = 0
            for journey in journeys:
                total_spend += journey.order.total_price
            customer_data.append({
                'email': customer.email,
                'phone': customer.phone,
                'ip_address': customer.ip_address,
                'first_name': customer.first_name,
                'last_name': customer.last_name,
                'order': len(journeys),
                'total_spend': total_spend
            })
        return json.dumps({
            'customer_data':customer_data
        })
