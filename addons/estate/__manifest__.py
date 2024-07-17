# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Estate',
    'version': '1.8',
    'category': 'Sales/Estate',
    
    'depends': [
        'base_setup',        
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
        # weitere Dateien
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'crm/static/src/**/*',
        ],
        'web.assets_tests': [
            'crm/static/tests/tours/**/*',
        ],
        'web.qunit_suite_tests': [
            'crm/static/tests/**/*',
            ('remove', 'crm/static/tests/tours/**/*'),
        ],
    },
    'license': 'LGPL-3',
}
