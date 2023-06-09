# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Odoo 16 Accounting',
    'version': '1.0.0',
    'category': 'Accounting',
    'summary': 'Accounting Reports',
    'description': 'Odoo 16 Financial Reports',    
    'sequence': '1',
    'website': 'https://www.churchycodes.co.tz',
    'author': 'Nathaniel Anania',
    'maintainer': 'Nathaniel Anania',
    'license': 'LGPL-3',
    'support': 'shaibulumanya@gmail.com',
    'depends': [
        'accounting_pdf_reports',
        'om_account_asset',
        'om_account_budget',
        'om_fiscal_year',
        'om_recurring_payments',
        'om_account_bank_statement_import',
        'om_account_daily_reports',
        'om_account_followup',
    ],
    'demo': [],
    'data': [
        'security/group.xml',
        'views/menu.xml',
        'views/settings.xml',
        'views/account_group.xml',
        'views/account_tag.xml',
        'views/res_partner.xml',
        'views/account_coa_template.xml',
        'views/fiscal_position_template.xml',
        'views/account_bank_statement.xml',
        'views/payment_method.xml',
        'views/reconciliation.xml',
        'views/account_journal.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/banner.png'],
}

