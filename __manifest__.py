# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

{
    'name':'Crm pipeline report',
    'version': '17.0.1.1',
    'sequence': 1,
    'category': 'Generic Modules/Tools',
    'description':
        """
        This Module add below functionality into odoo

        - Crm pipeline report\n

    """,
    'summary': 'Crm pipeline report',
    'author': 'DevIntelle Consulting Service Pvt.Ltd',
    'website': 'http://www.devintellecs.com',
    'depends': ['crm','base'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/crm_wizard.xml',
        'report/report_menu.xml',
        'report/pipline_history_report.xml',
    ],
    'demo': [],
    'test': [],
    'css': [],
    'qweb': [],
    'js': [],
    'images': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:








