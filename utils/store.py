from odoo.http import request


def get_store_by_url(store_url):
    return request.env["md.shopify.store"].sudo().search([("store_url", "=", store_url)], limit=1)