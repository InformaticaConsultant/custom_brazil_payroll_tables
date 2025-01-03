from odoo import models, fields, api

class HrContract(models.Model):
    _inherit = 'hr.contract'

    horas_mes = fields.Integer(
        string='Horas do mês',
        default=220,
        required=True,
        help='Horas trabajadas por mes'
    )

    salario_dia = fields.Float(
        string='Salário por dia',
        compute='_compute_salario_dia',
        store=True,
        help='Salário diário (Salário / 30)'
    )

    salario_hora = fields.Float(
        string='Salário hora',
        compute='_compute_salario_hora',
        store=True,
        help='Salário por hora (Salário / Horas mês)'
    )

    @api.depends('wage')
    def _compute_salario_dia(self):
        for record in self:
            record.salario_dia = (record.wage or 0.0) / 30

    @api.depends('wage', 'horas_mes')
    def _compute_salario_hora(self):
        for record in self:
            if record.horas_mes:
                record.salario_hora = (record.wage or 0.0) / record.horas_mes
            else:
                record.salario_hora = 0.0