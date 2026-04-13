# -*- coding: utf-8 -*-
{
    'name': 'CRM Personalizado - Inmobiliaria',
    'version': '19.0.1.0.0',
    'summary': 'Módulo CRM adaptado para agencias inmobiliarias',
    'description': """
        Personalización del módulo CRM nativo de Odoo para agencias inmobiliarias.
        - Widget visual de nivel de urgencia (1-5 estrellas)
        - Campo: ¿Ya trabaja con otra agencia?
        - Campo: Vender o alquilar
        - Campo: Exclusiva
        - Diseño mejorado y limpio
    """,
    'category': 'Sales/CRM',
    'author': 'Personalizado',
    'depends': ['crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'crm_personalizado/static/src/css/crm_personalizado.css',
            'crm_personalizado/static/src/xml/urgency_widget.xml',
            'crm_personalizado/static/src/js/urgency_widget.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
