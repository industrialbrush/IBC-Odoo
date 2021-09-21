# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    delivery_tolerance = fields.Selection([('1','NE/NL'),('2','OS')], string="Delivery Tolerance")
    due_date = fields.Date(string='Due Date')
    customer_part_number = fields.Char(string="Customer P/N")

    @api.onchange('product_id')
    def product_id_change(self):
        res = super(SaleOrderLine, self).product_id_change()
        if self.product_id.description_sale:
            self.name = self.product_id.description_sale
        else:
            self.name = self.product_id.name
        return res