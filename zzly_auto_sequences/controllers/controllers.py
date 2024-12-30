# -*- coding: utf-8 -*-
# from odoo import http


# class ZzlyAutoSequences(http.Controller):
#     @http.route('/zzly_auto_sequences/zzly_auto_sequences', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zzly_auto_sequences/zzly_auto_sequences/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('zzly_auto_sequences.listing', {
#             'root': '/zzly_auto_sequences/zzly_auto_sequences',
#             'objects': http.request.env['zzly_auto_sequences.zzly_auto_sequences'].search([]),
#         })

#     @http.route('/zzly_auto_sequences/zzly_auto_sequences/objects/<model("zzly_auto_sequences.zzly_auto_sequences"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zzly_auto_sequences.object', {
#             'object': obj
#         })

