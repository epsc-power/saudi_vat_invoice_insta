# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Product(models.Model):
    _inherit = 'product.template'

    discount_product = fields.Boolean(
        string='Is a Discount Product',
        default=False
    )
