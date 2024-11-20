# Custom Brazil Payroll Tables

Este módulo de Odoo está diseñado para manejar las tablas salariales personalizadas necesarias para la gestión de nóminas en Brasil. Incluye configuraciones específicas para cumplir con las normativas locales como el **INSS**, **IRRF**, y otras tasas relacionadas.

## Características

- Gestión de tablas de tasas para:
  - **INSS (Instituto Nacional do Seguro Social)**: Tasas progresivas de contribución.
  - **IRRF (Impuesto de Renta Retenido en la Fuente)**: Tasas y deducciones aplicables.
  - **FGTS (Fondo de Garantía por Tiempo de Servicio)**: Contribuciones patronales.
  - **Deducciones por dependientes**.
  - **Salario mínimo por año**.
- Configuración predefinida de las tasas para el año 2024.
- Compatible con la versión 17 de Odoo.

## Instalación

1. Clona este repositorio en tu carpeta `custom_addons`:
   git clone git@github.com:DiegoZata/custom_brazil_payroll_tables.git

2. Reinicia tu servidor de Odoo:
   sudo service odoo restart

3. Ve a **Aplicaciones** en el backend de Odoo, busca `Custom Brazil Payroll Tables` e instálalo.

## Uso

1. Una vez instalado, navega a **Payroll > Payroll Tables** para gestionar las tablas:
   - INSS Rates
   - IRRF Rates
   - FGTS Rates
   - Minimum Salary

2. Modifica o agrega tasas según las necesidades de tu empresa.

## Requisitos

- **Odoo 17**.
- Módulo base de nóminas (`hr_payroll`) instalado.

## Contribuir

¡Las contribuciones son bienvenidas! Si deseas colaborar:

1. Haz un fork de este repositorio.

2. Crea una nueva rama:
   git checkout -b feature/nueva_funcionalidad

3. Haz tus cambios y crea un pull request.

## Licencia

Este módulo está disponible bajo los términos de la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Contacto

Si tienes dudas o sugerencias, puedes contactar a:
- **Autor**: DiegoZata
- **Email**: dgbv_@hotmail.com
