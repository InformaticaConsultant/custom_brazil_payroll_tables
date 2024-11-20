{
    'name': 'Custom Brazil Payroll Tables',
    'version': '1.0',
    'author': 'Diego Benitz',
    'category': 'Human Resources',
    'summary': 'Adds customizable tables for payroll calculations (INSS, IRRF, FGTS) in Brazil.',
    'depends': ['hr_payroll'],
    'data': [
        'security/ir.model.access.csv',
        'views/payroll_tables_views.xml',
        'views/payroll_menuitems.xml',
        'data/payroll_default_data.xml',
    ],
    'installable': True,
    'application': False,
}
