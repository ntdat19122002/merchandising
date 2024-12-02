from odoo import http

class Pixel(http.Controller):
    @http.route('/pixel/view',  auth='public')
    def view_sdfs(self):
        print('view_sdfs')
        return {}