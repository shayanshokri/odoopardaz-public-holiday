# -*- coding: utf-8 -*-
{
    'name': "odoopardaz public holiday 1404",

    'summary': "This module adds official public holidays in Iran for the year 1404 to the Odoo working calendar",

    'description': """
This module automatically adds all official public holidays in Iran for the year 1404 to Odoo's working calendar. By installing this module, users can plan HR activities, schedule projects, and manage attendance more accurately. It is specifically designed for businesses operating in Iran and is fully compatible with Odoo's HR module.
    """,

    'author': "OdooPardaz",
    'website': "https://odoopardaz.ir",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources/Time Off',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr_work_entry'],

    # always loaded
    'data': [
        'data/hr_work_entry_type_data.xml',
        'data/resource_calendar_leaves_data.xml',
        'data/res_partner_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}

