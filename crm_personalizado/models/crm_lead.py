# -*- coding: utf-8 -*-
from odoo import models, fields


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    # Nivel de urgencia del cliente (1 = baja, 5 = máxima urgencia)
    urgency_level = fields.Integer(
        string='Nivel de Urgencia',
        default=1,
    )

    # Presupuesto del cliente
    budget = fields.Monetary(
        string='Precio estimado',
        currency_field='company_currency',
    )

    # Operación deseada: venta, alquiler o solo valoración
    operation_type = fields.Selection(
        selection=[
            ('sale', 'Vender'),
            ('rent', 'Alquilar'),
            ('valuation', 'Solo valoración'),
        ],
        string='Operación',
        default='sale',
        required=True,
    )

    # Tipo de propiedad
    property_type = fields.Selection(
        selection=[
            ('piso', 'Piso / Apartamento'),
            ('casa', 'Casa / Chalet'),
            ('local', 'Local comercial'),
            ('terreno', 'Terreno / Solar'),
            ('garaje', 'Garaje / Trastero'),
            ('oficina', 'Oficina'),
            ('otro', 'Otro'),
        ],
        string='Tipo de propiedad',
    )

    # Estado de la propiedad
    property_state = fields.Selection(
        selection=[
            ('new', 'Nueva construcción'),
            ('second_hand', 'Segunda mano'),
            ('needs_reform', 'A reformar'),
            ('reformed', 'Reformado'),
        ],
        string='Estado de la propiedad',
    )

    # Zona donde se encuentra la propiedad
    property_zone = fields.Char(
        string='Zona de la propiedad',
    )

    # Exclusividad del encargo
    exclusive = fields.Boolean(
        string='Exclusiva',
        default=False,
    )
