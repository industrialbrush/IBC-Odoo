# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    ship_via = fields.Char(string="Ship Via")
    fob = fields.Selection([('prepay-add','Prepay and Add'),('prepay','Prepay'),('collect','Collect'),('will-call','Will Call'),('third-party','Third Party')], string='FOB')
    remarks = fields.Text(string="Remarks")