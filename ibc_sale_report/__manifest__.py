# -*- coding: utf-8 -*-
{
    'name': ": Industrial Brush Corp: Custom Sale / Quotation Report",

    'summary': """
         Custom Sale / Quotation Report""",

    'description': """
        This module will add a new dropdown report for the user to print. Original Odoo report will still be available. 
    """,

    'author': "Odoo Inc.",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale','product'],

    # always loaded
    'data': [
        'report/header_footer.xml',
        'report/report_sale.xml',
        'views/sale_order_inherit.xml',
        'views/res_partner_inherit.xml'
    ],

    # 'css': [
    #     'static/src/less/ibc_report.scss'
    # ],

    # 'images': [
    #     'static/src/img/industrial-brush-corporation-100.png',
    # ],

}
