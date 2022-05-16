# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class openacademy_youtube_inh(models.Model):
#     _name = 'openacademy_youtube_inh.openacademy_youtube_inh'
#     _description = 'openacademy_youtube_inh.openacademy_youtube_inh'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
