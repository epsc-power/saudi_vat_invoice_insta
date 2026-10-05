# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class inherit_res_company(models.Model):
    _inherit= 'res.company'
    
    header_img = fields.Binary("Header Image")
    footer_img = fields.Binary("Footer Image")
    arabic = fields.Char('اسم')
    district = fields.Char('District')
    additional_no = fields.Char('Additional No.')
    account_number = fields.Char(string="Account Number")

class Journal(models.Model):
    _inherit= 'account.journal'

    iban = fields.Char('IBAN')
    branch = fields.Char('Branch')
