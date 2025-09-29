import multiprocessing

# Función para calcular el cuadrado de un número
def calculate_square(n):
    return n * n

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    
    # Crear un pool de procesos
    with multiprocessing.Pool() as pool:
        # Mapear la función a los números
        results = pool.map(calculate_square, numbers)

    print("Cuadrados:", results)

"""¿Qué diferencia al procesamiento secuencial del concurrente y el paralelo?
Procesamiento secuencial: Cada tarea se completa por completo antes de iniciar la siguiente.
Concurrencia: Comenzamos fragmentos de diversas tareas, pausándolas y retomándolas de forma alterna.
Paralelismo: Las tareas se ejecutan simultáneamente en diversos núcleos de procesamiento, requiriendo tantos núcleos como tareas en paralelo."""