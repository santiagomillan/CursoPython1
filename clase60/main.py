#import modulos
from ecommerce.inventory import add_product, remove_product
from ecommerce.sales import process_sales

add_product('Laptop', 10)
remove_product('Laptop')
process_sales('Laptop', 2)