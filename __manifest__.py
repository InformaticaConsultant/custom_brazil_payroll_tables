{
    'name': 'Custom Brazil Payroll Tables',
    'version': '1.0',
    'author': 'Diego Benitez',
    'category': 'Human Resources',
    'summary': 'Adds customizable tables for payroll calculations (INSS, IRRF, FGTS) in Brazil.',
    'depends': [
        'hr_payroll',
        'hr_contract',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/payroll_tables_views.xml',
        'views/payroll_menuitems.xml',
        'views/contract_view.xml',
        'data/payroll_default_data.xml',
    ],
    'installable': True,
    'application': False,
}
