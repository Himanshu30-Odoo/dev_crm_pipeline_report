

# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle 
#
##############################################################################

from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta
import itertools
import operator
from itertools import groupby
from operator import itemgetter



class CrmPiplineReport(models.AbstractModel):
    _name = 'report.dev_crm_pipeline_report.pipline_template1'


    def pipline_history(self, obj):
        domain = [('create_date','>=',obj.start_date),('create_date','<=',obj.end_date),('type','=','opportunity')]  
        
        if obj.stage_ids:
            domain.append(('stage_id', '=', obj.stage_ids.ids))

        records = self.env['crm.lead'].search(domain)
        box = []

        for rec in records:
            vals = {'name': rec.name if rec.name else "All Partners Data",
                    'partner_id': rec.partner_id.name,
                    'stage_id': rec.stage_id.name if rec.stage_id else "No Stage",
                    'expected_revenue': rec.expected_revenue,}
            box.append(vals)

        print("Without group_by dictionary is:",box)

        box = sorted(box, key=itemgetter('stage_id'))
        groups = itertools.groupby(box, key=operator.itemgetter('stage_id'))
        group_lines = [{'stage_id': k, 'values': [x for x in v]} for k, v in groups]
        print("now the main dict is=================:", group_lines)
        return group_lines
       
        
    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['crm.lead.wizard'].browse(docids)
        pipline_history = self.pipline_history(docs[0])
        return {
            'doc_ids': docs.ids,
            'doc_model': 'crm.lead.wizard',
            'docs': docs,
            'pipline_history':self.pipline_history,
        }

    
      
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:




