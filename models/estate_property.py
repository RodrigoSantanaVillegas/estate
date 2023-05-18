# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class PublicidadInmobiliaria(models.Model):
    _name = "estate.property"
    _description = "Campo ejemplo odoo"
    
    
    name = fields.Char(required=True)
    description = fields.Text()
    postcore = fields.Char()
    date_availability = fields.Date(copy=False, default=lambda self: fields.Date.to_string(datetime.datetime.now() + datetime.timedelta(days=3*30)))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="Indica la orientacion del jardin")
    state = fields.Selection(
        copy=False,
        selection=[('nuevo', 'Nuevo'), ('recibida', 'Oferta recibida'), ('aceptada', 'Oferta aceptada'), ('Vendido', 'Vendido'), ('cancelado', 'Cancelado')],
        default='nuevo',
        help="Indica el estado de la vivienda")
    salesman = fields.Many2one("res.partner", string="Salesman", copy=False)
    buyer = fields.Many2one("res.users", string="Buyer", default=lambda self: self.env.user)
    tag_ids = fields.Many2many("estate.property.tag", string="Etiqueta")
    offer_ids = fields.One2many('estate.property.offer', 'property_id')
    total_area = fields.Float(compute="_compute_total")
    best_price = fields.Float(compute="_compute_max")
    
    @api.depends("living_area", "garden_area")
    def _compute_total(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
            
    @api.depends("offer_ids")
    def _compute_max(self):
        for record in self:
            if record.offer_ids:
                record.best_price = max(record.offer_ids.mapped('price'))
            else:
                record.best_price = 0

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = False
            self.garden_orientation = False