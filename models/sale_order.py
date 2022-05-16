from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    confirmed_user_id = fields.Many2one('res.users', string='Confirmed User', readonly=True)

    def action_confirm(self):
        # print('Confirm....................................')
        super(SaleOrder, self).action_confirm()
        self.confirmed_user_id = self.env.user.id
