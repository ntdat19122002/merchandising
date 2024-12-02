import shopify


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
