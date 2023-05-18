# -*- coding: utf-8 -*-

from odoo import models, fields


class EtiquetaPropiedad(models.Model):
    _name = "estate.property.tag"
    _description = "Tipos de etiquetas"
    
    name = fields.Char(required=True)