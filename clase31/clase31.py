import csv

#Leer un file
"""with open('products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)"""

#Mostrar info cols
"""with open('products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Producto: {row['name']}, Precio {row['price']}")"""

#Escribir un file
"""new_product = {
    'name': 'Wireless Charger',
    'price': 75,
    'quantity': 100,
    'brand': 'ChargerMaster',
    'category': 'Accessories',
    'entry_date': '2024-07-01'
}

with open('products.csv', mode='a', newline='') as file:
    file.write('\n')
    csv_writer = csv. DictWriter(file, fieldnames = new_product.keys())
    csv_writer.writerow(new_product)"""

#new Col
file_path = 'products.csv'
updated_file_path = 'products_updated.csv'

with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    #Obtener los nombres de las columnas existentes
    fieldnames = csv_reader.fieldnames + ['total_value']
    
    with open(updated_file_path, mode='w', newline='') as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        csv_writer.writeheader() #Escribir los nombres de las columnas en el nuevo archivo
        
        for row in csv_reader:
            row['total_value'] = int(row['price']) * int(row['quantity'])
            csv_writer.writerow(row)