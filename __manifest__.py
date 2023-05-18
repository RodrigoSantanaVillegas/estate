# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'ESTATE',
    'version': '0.1',
    'category': 'UNDECLARED',
    'summary': 'Track leads and close opportunities',
    'description': "Modulo prueba odoo",
    'website': 'https://paginaswebmp.com/',
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_menus.xml',        
        'views/search_view.xml',        
    ],
    'license': 'LGPL-3',
}