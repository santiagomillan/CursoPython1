import reports

#genera reporte de ventas y gastos usando el modulo reports
sales_report = reports.generate_sales_report('January', 15000)
expenses_report = reports.generate_inventory_report('January', 5000)
print(sales_report)
print(expenses_report)