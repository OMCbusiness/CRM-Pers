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
        string='Presupuesto',
        currency_field='company_currency',
    )

    # Operación deseada: venta o alquiler
    operation_type = fields.Selection(
        selection=[
            ('sale', 'Vender'),
            ('rent', 'Alquilar'),
        ],
        string='Operación',
        default='sale',
    )

    # Exclusividad del encargo
    exclusive = fields.Boolean(
        string='Exclusiva',
        default=False,
    )
