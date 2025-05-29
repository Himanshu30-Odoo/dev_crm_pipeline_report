# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

from odoo import models, fields,api,_
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError


class CrmPiplineWizard(models.TransientModel):
    _name = 'crm.lead.wizard'
    _description = 'CRM Lead Wizard'


    start_date = fields.Date(string='Start Date',default=fields.Datetime.today(), required=True)
    end_date = fields.Date(string='End Date',required=True)
    currency_id = fields.Many2one('res.currency', string="Currency", default=lambda self: self.env.company.currency_id)
    stage_ids = fields.Many2many('crm.stage','crm_lead_stage_rel','lead_id','stage_id', string='Stages')


    @api.onchange('end_date','start_date')  
    def onchange_of_end_date(self):
        if self.start_date and self.end_date:
            if self.end_date < self.start_date:
                    raise ValidationError(_("End date must be greater than the start date."))
            
    def print_pipline_report(self):
        return self.env.ref('dev_crm_pipeline_report.pipline_report_menu').report_action(self)

    

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
