import asyncio

async def process_data(data):
    print(f"Processing {data}...")
    await asyncio.sleep(10)  # Simula una operación que toma tiempo
    print(f"Finished processing {data}")
    return data * 2

async def main():
    print("Starting main function")
    result = await process_data("archivo.txt")
    print(f"Result: {result}")
    
asyncio.run(main())