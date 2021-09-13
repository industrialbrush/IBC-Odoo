# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    delivery_tolerance = fields.Selection([('1','NE/NL'),('2','OS')], string="Delivery Tolerance")
    due_date = fields.Date(string='Due Date')
    customer_part_number = fields.Char(string="Customer P/N")