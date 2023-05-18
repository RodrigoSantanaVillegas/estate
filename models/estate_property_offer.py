# -*- coding: utf-8 -*-

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
    date_deadline = fields.Date ()