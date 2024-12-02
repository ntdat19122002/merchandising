import shopify, logging, traceback, hmac, hashlib, json, base64
from urllib import parse
from urllib.parse import parse_qs
from odoo.http import request

_logger = logging.getLogger(__name__)


def verify_request():
    current_user = request.env.user
    if current_user.has_group('base.group_user'):
        return True
    try:
        if request.httprequest.referrer and "hmac" in request.httprequest.referrer:
            query = parse.urlsplit(request.httprequest.referrer).query
        elif request.params.get("hmac"):
            query = parse.urlsplit(request.httprequest.url).query
        else:
            query = parse.urlsplit(request.params.get("referer")).query
        shopify.Session.secret = request.env["ir.config_parameter"].sudo().get_param("merchandising.md_api_secret_key")
        dict_params = dict(parse_qs(query))
        params = {k: v[0] for k, v in dict_params.items()}
        session_hmac = shopify.Session.calculate_hmac(params)
        if session_hmac == params["hmac"]:
            return True
        raise Exception("Unauthorized request")
    except Exception as e:

        _logger.error(traceback.format_exc())
    raise Exception("Unauthorized request")


def verify_app_proxy_request():
    secret_key = request.env["ir.config_parameter"].sudo().get_param("merchandising.md_api_secret_key")
    query_params = dict(parse.parse_qs(request.httprequest.query_string))
    params = {key.decode("utf-8"): value[0].decode("utf-8") for (key, value) in query_params.items() if key.decode("utf-8") != "signature"}
    if "logged_in_customer_id" not in params:
        params["logged_in_customer_id"] = ""

    def encoded_params(params):
        encoded_params = ""
        for key in sorted(params):
            encoded_params += key + "=" + params[key]
        return encoded_params

    hexdigest = hmac.new(secret_key.encode("utf-8"), encoded_params(params).encode("utf-8"), hashlib.sha256).hexdigest()
    if not hmac.compare_digest(hexdigest.encode("utf-8"), query_params["signature".encode("utf-8")][0]):
        _logger.error("Secret key is not verified." + json.dumps(request.params))
        raise Exception("Secret key is not verified")
    return True


def verify_webhook():
    try:
        secret_key = request.env['ir.config_parameter'].sudo().get_param('merchandising.md_api_secret_key')
        digest = hmac.new(secret_key.encode('utf-8'), request.httprequest.data, hashlib.sha256).digest()
        computed_hmac = base64.b64encode(digest)
        if not hmac.compare_digest(computed_hmac, request.httprequest.headers.get('X-Shopify-Hmac-Sha256').encode('utf-8')):
            _logger.error('Secret key is not verified' + json.loads(request.httprequest.data.decode('utf-8')))
            return False
        return True
    except Exception as e:
        a = 0
    return False
