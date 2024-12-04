import shopify, werkzeug, logging, traceback, json
from odoo import http
from odoo.http import request, Response
from datetime import datetime
from urllib.parse import urlencode
from .auth import verify_request
from ..utils.utils import get_scope_shopify

_logger = logging.getLogger(__name__)

SCOPES = ["read_products", "read_themes", 'write_pixels', 'read_customer_events']


class MerchandisingAuthentication(http.Controller):
    @staticmethod
    def is_shop_auth(self, kw):
        timestamp = kw["timestamp"]
        shop = request.env["md.shopify.store"].sudo().search([
            ("store_url", "=", kw["shop"]), ("install_status", "=", True)
        ], limit=1)
        is_shop_login = "md_shop_login" in request.session and request.session["md_shop_login"] == kw["shop"]
        is_shop_login = is_shop_login and shop and not self.expire_session(timestamp)
        return is_shop_login

    @staticmethod
    def expire_session(timestamp):
        try:
            if "last_login" not in request.session:
                return False
            last_login = request.session.get("last_login")
            if last_login and timestamp:
                current_timestamp = datetime.now().timestamp()
                # check last shop last login by field last_login in shop, > 30m return False
                if last_login >= current_timestamp - 1800:
                    return False
        except Exception as e:
            _logger.error(traceback.format_exc())
        return False

    @http.route("/shopify/merchandising", auth="public")
    def nest_merchandising_index(self, **kw):
        try:
            if self.is_shop_auth(self, kw):
                return werkzeug.utils.redirect(f"/shopify/merchandising/main?{urlencode(request.params)}")
            else:
                request.params["session_id"] = request.session.sid
                shop = request.env['md.shopify.store'].sudo().search([
                    ('store_url', '=', kw['shop']), ('install_status', '=', True)
                ], limit=1)
                base_url = request.env["ir.config_parameter"].sudo().get_param("web.base.url")
                redirect_uri = base_url + "/shopify/merchandising/auth?" + urlencode(request.params)
                if shop:
                    api_key = request.env['ir.config_parameter'].sudo().get_param('merchandising.md_api_key')
                    headers = {'Content-Security-Policy': "frame-ancestors https://" +
                                                          request.params['shop'] + " https://admin.shopify.com;"}
                    return request.render('nestprdvariant.merchandising_redirect', {
                        'url': redirect_uri,
                        'md_settings': json.dumps({'k': api_key})
                    }, headers=headers)
                else:
                    return request.render('nestprdvariant.shopify_connect', {'auth_url': redirect_uri})
        except Exception as e:
            _logger.error(traceback.format_exc())
        return werkzeug.utils.redirect("https://nestscale.com")

    @http.route("/shopify/merchandising/auth", auth="public")
    def nest_merchandising_auth(self, **kw):
        if "shop" in kw:
            api_key = request.env["ir.config_parameter"].sudo().get_param("merchandising.md_api_key")
            api_secret = request.env["ir.config_parameter"].sudo().get_param("merchandising.md_api_secret_key")
            api_version = request.env["ir.config_parameter"].sudo().get_param("merchandising.md_api_version")
            base_url = request.env["ir.config_parameter"].sudo().get_param("web.base.url")
            try:
                shopify.ShopifyResource.clear_session()
                shopify.Session.setup(api_key=api_key, secret=api_secret)
                shopify_session = shopify.Session(request.params["shop"], api_version)
                scope = SCOPES
                redirect_uri = base_url + "/shopify/merchandising/finalize"
                permission_url = shopify_session.create_permission_url(scope, redirect_uri)
                return werkzeug.utils.redirect(permission_url)
            except Exception as e:
                _logger.error(traceback.format_exc())
        return werkzeug.utils.redirect("https://nestscale.com")

    @http.route("/shopify/merchandising/finalize", auth="public")
    def nest_merchandising_finalize(self, **kw):
        if "shop" not in request.params:
            raise Exception("Missing shop url parameter")

        api_key = request.env["ir.config_parameter"].sudo().get_param("merchandising.md_api_key")
        api_secret = request.env["ir.config_parameter"].sudo().get_param("merchandising.md_api_secret_key")
        base_url = request.env["ir.config_parameter"].sudo().get_param("web.base.url")
        api_version = request.env["ir.config_parameter"].sudo().get_param("merchandising.md_api_version")
        try:
            shopify.Session.setup(api_key=api_key, secret=api_secret)
            shopify_session = shopify.Session(kw["shop"], api_version)
            token = shopify_session.request_token(kw)
            store = request.env["md.shopify.store"].sudo().search([("store_url", "=", request.params["shop"])], limit=1)
            action = False
            if not store:
                store = request.env["md.shopify.store"].sudo().create({
                    "store_url": request.params["shop"],
                    "shopify_access_token": token,
                    "plan_version": request.env['md.plan'].sudo().get_current_plan_version()
                })
                store.update_store_info()
                action = 'install_app'
            else:
                store.shopify_access_token = token
                if not store.install_status:
                    store.install_status = True
                    action = 'install_app'
                store.update_store_info()

            try:
                if action:
                    request.env['marketing.action.history'].sudo().create_customer_trace(store, 'nestprdvariant',
                                                                                         action)
            except Exception as e:
                _logger.error(traceback.format_exc())

            request.session["last_login"] = datetime.now().timestamp()
            request.session["md_shop_login"] = request.params["shop"]
            store.register_webhook()

            return werkzeug.utils.redirect(base_url + "/shopify/merchandising/main?" + urlencode(request.params))
        except Exception as e:
            _logger.error(traceback.format_exc())
        return werkzeug.utils.redirect("https://nestscale.com")

    @http.route("/shopify/merchandising/main", auth="public")
    def nest_merchandising_main(self, **kw):
        try:
            # verify_request()
            store = request.env["md.shopify.store"].sudo().search([("store_url", "=", request.params["shop"])], limit=1)
            api_key = request.env["ir.config_parameter"].sudo().get_param("merchandising.md_api_key")
            password_master = request.env['ir.config_parameter'].sudo().get_param('merchandising.md_password_master')
            if store:
                headers = {"Content-Security-Policy": "frame-ancestors https://" + request.params[
                    "shop"] + " https://admin.shopify.com;"}

                value = {
                    "store_url": store.store_url,
                    'store_name': store.name,
                    'store_id': store.id,
                    "k": api_key,  # Shopify API Key dùng để tạo App Bridge
                    "current_plan": store.get_current_plan(),
                }
                return request.render("merchandising.merchandising_index", {
                    "md_settings": json.dumps(value),
                    'md_password_master': json.dumps(password_master)
                }, headers=headers)

        except Exception as e:
            _logger.error(traceback.format_exc())
        return werkzeug.utils.redirect("https://nestscale.com")

    @http.route('/shopify/merchandising/internal_admin', auth='user')
    def check_internal(self, **kw):
        try:
            password_master = request.env['ir.config_parameter'].sudo().get_param('merchandising.md_password_master')
            if "shop" in kw and kw['password_master'] == password_master:
                current_user = request.env.user
                if current_user.has_group('base.group_user'):
                    request.session['last_login'] = datetime.now().timestamp()
                    request.session['md_shop_login'] = request.params['shop']
                    request.params['session_id'] = request.session.sid
                    redirect_url = '/shopify/merchandising/main?' + urlencode(request.params)
                    return werkzeug.utils.redirect(redirect_url)
            else:
                return request.render('http_routing.404')
        except Exception as e:
            _logger.error(traceback.format_exc())
        return werkzeug.utils.redirect('https://nestscale.com')
