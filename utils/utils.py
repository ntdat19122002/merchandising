import shopify

from odoo.http import request


def active_shopify_pixel_app():
    shopify.GraphQL.execute('''mutation {
        {
            code
            field
            message
        }
        webPixel
            {
                settings
                id
            }
        }
    }''')

def get_scope_shopify():
    store = request.env["md.shopify.store"].sudo().search()
    store.init_merchandising_shopify_session()
    print(shopify.AccessScope.find())
