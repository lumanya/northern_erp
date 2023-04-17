# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Odoo 16 Fiscal Year & Lock Date',
    'version': '16.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Odoo 16 Fiscal Year, Fiscal Year in Odoo 16, Lock Date in Odoo 16',
    'description': 'Odoo 16 Fiscal Year, Fiscal Year in Odoo 16',
    'sequence': '1',
    'website': 'https://churchycodes.co.tz',
    'author': 'Nathaiel Anania',
    'maintainer': 'Nathaniel Anania',
    'license': 'LGPL-3',
    'support': 'shaibulumanya@gmail.com',
    'depends': ['account'],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'security/account_security.xml',
        'wizard/change_lock_date.xml',
        'views/fiscal_year.xml',
        'views/settings.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': ['static/description/banner.png'],
}
