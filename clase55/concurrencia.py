import threading
import time

#simula el procesamiento de una solicitud
def process_request(request_id):
    print(f"Procesando solicitud {request_id}...")
    time.sleep(3)  # Simula un procesamiento que toma tiempo
    print(f"Solicitud {request_id} procesada.")

threads = []

for i in range(3):
    #crea nuevo hilo que ejecuta la funcion process_request
    thread = threading.Thread(target=process_request, args=(i,))
    threads.append(thread)
    thread.start()

#espera a que todos los hilos terminen
for thread in threads:
    #asegura que el hilo principal espere a que cada hilo termine
    thread.join()

print("Todas las solicitudes han sido procesadas.")