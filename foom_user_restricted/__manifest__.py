# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Foom User Restricted',
    'version': '1.0',
    'depends': ['base', 'product', 'stock', 'resource'],
    'description': "",
    'data': [
        'security/ir.model.access.csv',
        'security/foom_user_group_security.xml',
        'views/product_template_views.xml'
    ],
    'test': [],
    'application': False,
    'license': 'LGPL-3',
}
