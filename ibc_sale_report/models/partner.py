# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    fax = fields.Char(string='Fax')
    group = fields.Selection([('end-user','E'),('oem','O'),('jobber','J')])