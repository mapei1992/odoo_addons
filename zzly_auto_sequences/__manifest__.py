# -*- coding: utf-8 -*-
{
    'name': "Product & Partner automatic coding",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Set automatic coding rules for product categories
1. Enable developer mode,
2. Define encoding rules in Settings Technology Sequence,
3. Set coding rules in Inventory Settings Product Category
    """,
'images': ['static/images/main_2.png', 'static/images/main_1.png', 'static/img/log.png'],
    'author': "My Company",
    'website': "https://odoo.com/",
'icon': '/student/static/img/logo.png',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',

    'version': '0.3',
    'version': '0.2',


    # any module necessary for this one to work correctly
    'depends': ['base','product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_category_auto_sequence.xml',
        'views/partner_auto_sequence.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    "license": "AGPL-3",
"application": True,
"installable": True,
"support":"mapei1992@live.com",
"price":19.9
}

