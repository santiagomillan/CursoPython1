import asyncio
import time
import random
import multiprocessing

#fun asincrona para verificar inventario
async def check_inventory(item):
    print(f"Verificando inventario para {item}...")
    await asyncio.sleep(random.uniform(3, 6))  # Simula tiempo de verificación
    print(f"Inventario verificado para {item}.")
    # Simula que el item está en inventario
    return random.choice([True, False])

#fun asincrona para procesar pago
async def process_payment(order_id):
    print(f"Procesando pago para la orden {order_id}...")
    await asyncio.sleep(random.uniform(3, 6))  # Simula tiempo de procesamiento
    print(f"Pago procesado para la orden {order_id}.")
    return True

#fun intensiva en cpu para calcular el costo total del pedido
def calcylate_total(items):
    print(f"Calculando total para {len(items)} articulos...")
    time.sleep(5)  # Simula tiempo de cálculo
    total = sum(item["price"] for item in items)
    print(f"Total calculado: ${total:.2f}")
    return total


async def process_order(order_id, items):
    print(f"Iniciando procesando orden {order_id}...")
    # Verificar inventario asincronamente
    inventory_checks = [check_inventory(item["name"]) for item in items]
    inventory_results = await asyncio.gather(*inventory_checks)
    if not all(inventory_results):
        print(f"Orden {order_id} no puede ser procesada debido a falta de inventario.")
    with multiprocessing.Pool() as pool:
        total = pool.apply(calcylate_total, (items,))
    # Procesar pago asincronamente
    payment_result = await process_payment(order_id)

    if payment_result:
        print(f"Orden {order_id} procesada exitosamente. Total: ${total}")
    else:
        print(f"Orden {order_id} falló durante el procesamiento de pago.")


async def main():
    orders = [
        {'order_id': 1, 'items': [{'name': 'Laptop', 'price': 1000}, {'name': 'Mouse', 'price': 50}]},
        {'order_id': 2, 'items': [{'name': 'Teclado', 'price': 80}, {'name': 'Monitor', 'price': 300}]},
        {'order_id': 3, 'items': [{'name': 'Smartphone', 'price': 700}, {'name': 'Funda', 'price': 20}]}
    ]

    #Procesar múltiples órdenes concurrentemente
    tasks = [process_order(order['order_id'], order['items']) for order in orders]
    await asyncio.gather(*tasks)

#Creamos el event loop
if __name__ == '__main__':
    asyncio.run(main())