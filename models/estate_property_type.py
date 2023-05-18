# -*- coding: utf-8 -*-

from odoo import models, fields


class TipoPropiedad(models.Model):
    _name = "estate.property.type"
    _description = "Tipos de propiedades"
    
    name = fields.Char(required=True)