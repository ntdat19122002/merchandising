from odoo import http

class Pixel(http.Controller):
    @http.route('/pixel/view123', type='json', auth='public')
    def view_sdfs(self):
        print('view_sdfs')
        return {
            'pixel_view_data': 'Your pixel view data goes here'
        }