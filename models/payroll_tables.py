from odoo import models, fields

class PayrollINSSRate(models.Model):
    _name = 'payroll.inss.rate'
    _description = 'INSS Rates'
    _order = 'range_min asc'

    range_min = fields.Float(string="Minimum Range")
    range_max = fields.Float(string="Maximum Range")
    rate = fields.Float(string="Rate (%)")

class PayrollIRRFRate(models.Model):
    _name = 'payroll.irrf.rate'
    _description = 'IRRF Rates'

    range_min = fields.Float(string="Minimum Range")
    range_max = fields.Float(string="Maximum Range")
    rate = fields.Float(string="Rate (%)")
    deduction = fields.Float(string="Deduction")

class PayrollFGTSRate(models.Model):
    _name = 'payroll.fgts.rate'
    _description = 'FGTS Rates'

    rate = fields.Float(string="Rate (%)", default=8.0)

class PayrollDependentDeduction(models.Model):
    _name = 'payroll.dependent.deduction'
    _description = 'Dependent Deduction'

    num_dependents = fields.Integer(string="Number of Dependents")
    deduction_per_dependent = fields.Float(string="Deduction per Dependent")

class PayrollAdditionalTable(models.Model):
    _name = 'payroll.additional.table'
    _description = 'Additional Payroll Tables'

    name = fields.Char(string="Description")
    value = fields.Float(string="Value")
    percentage = fields.Float(string="Percentage")
    
class PayrollMinimumSalary(models.Model):
    _name = 'payroll.minimum.salary'
    _description = 'Minimum Salary by Year'

    year = fields.Integer(string="Year")
    minimum_salary = fields.Float(string="Minimum Salary")
