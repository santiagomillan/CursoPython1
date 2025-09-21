import json

#Lectura de un archivo JSON
"""with open('products.json', 'r') as file:
    products = json.load(file)

#Mostrar los productos
for product in products:
    print(f"Product:  {product['name']}, Price: {product['price']}")"""


file_path = 'products.json'

new_product = {
    "name": "Charger",
    "price": 55,
    "quantity": 100,
    "brand": "Charger",
    "category": "Accessories",
    "entry_date": "2024-07-01"
}

with open(file_path, mode='r') as file:
    products = json.load(file)

products.append(new_product)

with open(file_path, mode='w') as file:
    json.dump(products, file, indent=4)