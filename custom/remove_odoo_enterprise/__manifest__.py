# Copyright 2018 Eska Yazılım ve Danışmanlık A.Ş (www.eskayazilim.com.tr)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Remove Odoo Enterprise",
    "summary": "Remove enterprise modules and setting items",
    "version": "16.0.2.0.0",
    'sequence': '1',
    "category": "Maintenance",
    "author": "Nathaniel",
    "website": "https://github.com/OCA/server-brand",
    "license": "AGPL-3",
    "depends": ["base_setup"],
    "data": ["views/res_config_settings_views.xml"],
    "installable": True,
     'application': True,
    'auto_install': False,
}
