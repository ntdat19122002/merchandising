import shopify

from odoo import http
from odoo.http import request


class Pixel(http.Controller):
    @http.route('/pixel/view', auth='public', cors="*")
    def view_sdfs(self):
        print('view_sdfs')
        return {}

    @http.route('/pixel/events/page_viewed', auth='public', cors="*")
    def shopify_pixel_page_viewed(self):
        print('page_viewed')
        return {}

    @http.route('/pixel/events/checkout_completed', auth='public', cors="*")
    def shopify_pixel_checkout_complete(self):
        print('checkout_complete')
        return {}

    @http.route('/pixel/events/product_viewed', auth='public', cors="*")
    def shopify_pixel_product_viewed(self):
        print('product_viewed')
        return {}

    @http.route('/pixel/events/cart_viewed', auth='public', cors="*")
    def shopify_pixel_cart_viewed(self):
        print('cart_viewed')
        return {}

    @http.route('/pixel/events/product_added_to_cart', auth='public', cors="*")
    def shopify_pixel_product_added_to_cart(self):
        print('product_added_to_cart')
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
