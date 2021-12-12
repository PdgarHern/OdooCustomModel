# -*- coding: utf-8 -*-
# from odoo import http


# class Animes(http.Controller):
#     @http.route('/animes/animes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/animes/animes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('animes.listing', {
#             'root': '/animes/animes',
#             'objects': http.request.env['animes.animes'].search([]),
#         })

#     @http.route('/animes/animes/objects/<model("animes.animes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('animes.object', {
#             'object': obj
#         })
