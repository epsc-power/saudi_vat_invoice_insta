# -*- coding: utf-8 -*-
{
    'name': 'Saudi Invoice Format',
    'version': '1.0',
    'depends': ['base','account','sale'],
    'category': 'Accounting',
    'data': [
        'views/res_company.xml',
        'views/invoice.xml',
        'views/res_partner.xml',
        # 'views/product_view.xml',
        'reports/report_saudi_invoice.xml',
        'reports/report_saudi_invoice_b2b.xml',
        # 'reports/report_saudi_pro-forma_invoice.xml',
     ],
    'installable': True,
    'application': False,
}
