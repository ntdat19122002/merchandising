from crypt import methods

import shopify

from odoo import http
from odoo.http import request, Response


class Pixel(http.Controller):
    @http.route('/pixel/events/page_viewed',methods=['GET'], auth='public')
    def shopify_pixel_page_viewed(self,**kw):
        store = request.env['md.shopify.store'].sudo().search([('store_url','=',kw['store_url'])])
        customer = request.env['md.customer'].sudo().search([('shopify_customer_id','=',kw['client_id'])])
        if not customer:
            customer = request.env['md.customer'].sudo().create({
                'store': store.id,
                'shopify_customer_id':kw['client_id'],
            })
        request.env['md.event'].sudo().create({
            'customer': customer.id,
            'event': kw['event'],
        })
        return {}

    @http.route('/pixel/events/checkout_completed',methods=['GET'], auth='public')
    def shopify_pixel_checkout_completed(self, **kw):
        store = request.env['md.shopify.store'].sudo().search([('store_url', '=', kw['store_url'])])
        customer = request.env['md.customer'].sudo().search([('shopify_customer_id', '=', kw['client_id'])])
        if not customer:
            customer = request.env['md.customer'].sudo().create({
                'store': store.id,
                'shopify_customer_id': kw['client_id'],
                'email': kw.get('email'),
                'phone': kw.get('phone'),
                'ip': request.httprequest.remote_addr,
                'first_name': kw.get('first_name'),
                'last_name': kw.get('last_name'),
            })
        else:
            customer.write({
                'email': kw.get('email'),
                'phone': kw.get('phone'),
                'ip': request.httprequest.remote_addr,
                'first_name': kw.get('first_name'),
                'last_name': kw.get('last_name'),
            })
        request.env['md.event'].sudo().create({
            'customer': customer.id,
            'event': kw['event'],
        })
        order = request.env['md.shopify.order'].sudo().create({
            'total_price': kw['event_data[totalPrice]'],
        })
        journey = request.env['md.journey'].sudo().create({
            'store': store.id,
            'order': order.id,
            'customer': customer.id,
        })
        events_of_journey = request.env['md.event'].sudo().search([('customer','=',customer.id)])
        for event in events_of_journey:
            event.write({
                'journey': journey.id,
            })
        return {}

    @http.route('/pixel/events/checkout_started', methods=['GET'], auth='public')
    def shopify_pixel_checkout_started(self, **kw):
        store = request.env['md.shopify.store'].sudo().search([('store_url', '=', kw['store_url'])])
        customer = request.env['md.customer'].sudo().search([('shopify_customer_id', '=', kw['client_id'])])
        if not customer:
            customer = request.env['md.customer'].sudo().create({
                'store': store.id,
                'shopify_customer_id': kw['client_id'],
            })
        request.env['md.event'].sudo().create({
            'customer': customer.id,
            'event': kw['event'],
        })
        return {}

    @http.route('/pixel/events/product_viewed',methods=['GET'], auth='public')
    def shopify_pixel_product_viewed(self,**kw):
        store = request.env['md.shopify.store'].sudo().search([('store_url', '=', kw['store_url'])])
        customer = request.env['md.customer'].sudo().search([('shopify_customer_id', '=', kw['client_id'])])
        if not customer:
            customer = request.env['md.customer'].sudo().create({
                'store': store.id,
                'shopify_customer_id': kw['client_id'],
            })
        request.env['md.event'].sudo().create({
            'customer': customer.id,
            'event': kw['event'],
        })
        return {}

    @http.route('/pixel/events/cart_viewed',methods=['GET'], auth='public')
    def shopify_pixel_cart_viewed(self, **kw):
        store = request.env['md.shopify.store'].sudo().search([('store_url', '=', kw['store_url'])])
        customer = request.env['md.customer'].sudo().search([('shopify_customer_id', '=', kw['client_id'])])
        if not customer:
            customer = request.env['md.customer'].sudo().create({
                'store': store.id,
                'shopify_customer_id': kw['client_id'],
            })
        request.env['md.event'].sudo().create({
            'customer': customer.id,
            'event': kw['event'],
        })
        return {}

    @http.route('/pixel/events/product_added_to_cart',methods=['GET'], auth='public')
    def shopify_pixel_product_added_to_cart(self, **kw):
        store = request.env['md.shopify.store'].sudo().search([('store_url', '=', kw['store_url'])])
        customer = request.env['md.customer'].sudo().search([('shopify_customer_id', '=', kw['client_id'])])
        if not customer:
            customer = request.env['md.customer'].sudo().create({
                'store': store.id,
                'shopify_customer_id': kw['client_id'],
            })
        request.env['md.event'].sudo().create({
            'customer': customer.id,
            'event': kw['event'],
        })
        return {}

    @http.route("/pixel/connect", methods=['POST'], type='json', auth="public")
    def conect_pixel(self, **kw):
        store = request.env["md.shopify.store"].sudo().search([('store_url', '=', kw.get('store_url'))])
        store.init_merchandising_shopify_session()
        query = '''
        mutation { 
            webPixelCreate(webPixel: { 
                settings: {
                    accountID: "%(accountID)s"
                } 
            }) { userErrors {code field message} webPixel { settings id } } }
        ''' %{'accountID': 123}
        pixel_response = shopify.GraphQL().execute(query=query)
        return {}
