# -*- coding: utf-8 -*-

from datetime import timedelta
from odoo import models, fields, api


class OfertaPropiedad(models.Model):
    _name = "estate.property.offer"
    _description = "Tipos de ofertas"
    
    price = fields.Float()
    status = fields.Selection(
        copy=False,
        selection=[('accepted', 'Aceptado'), ('refused', 'Rechazado')],
        help="Indica el estado de la oferta")
    partner_id = fields.Many2one ('res.partner', required=True, string='Cliente')
    property_id = fields.Many2one ('estate.property', required=True)
    validity = fields.Integer (default=7, string='Validity (days)')
    date_deadline = fields.Date (compute="_compute_date_deadline", inverse="_inverse_date_deadline")
    
    @api.depends("validity")
    def _compute_date_deadline(self):
        for record in self:
            if record.validity:
                record.date_deadline = fields.Date.today() + timedelta(days=record.validity)
            else:
                record.date_deadline = False
    
    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline:
                today = fields.Date.today()
                delta = record.date_deadline - today
                record.validity = delta.days
            else:
                record.validity = 0