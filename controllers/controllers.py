# -*- coding: utf-8 -*-
# from odoo import http


# class OpenacademyYoutubeInh(http.Controller):
#     @http.route('/openacademy_youtube_inh/openacademy_youtube_inh', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openacademy_youtube_inh/openacademy_youtube_inh/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('openacademy_youtube_inh.listing', {
#             'root': '/openacademy_youtube_inh/openacademy_youtube_inh',
#             'objects': http.request.env['openacademy_youtube_inh.openacademy_youtube_inh'].search([]),
#         })

#     @http.route('/openacademy_youtube_inh/openacademy_youtube_inh/objects/<model("openacademy_youtube_inh.openacademy_youtube_inh"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openacademy_youtube_inh.object', {
#             'object': obj
#         })
