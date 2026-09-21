# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Product(models.Model):
    _inherit = 'product.template'

    discount_product = fields.Boolean(string='Is a Discount Product',default=False)

    _sql_constraints = [
        ('code_discount_product', "CHECK(discount_product is True)", 'Already discount product is assigned!')
    ]