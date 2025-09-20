#Leer file linea por linea
# with open('cuento.txt' , 'r') as file:
#     for lineas in file:
#         print(lineas.strip())

#Leer file todas las lineas en una lista
"""with open('cuento.txt' , 'r') as file:
    lineas = file.readlines()
    print(lineas)"""

#Escribir en un archivo 
"""with open('cuento.txt' , 'a') as file:
    file.write('\n\nFin del cuento')"""

#sobrescribir en un archivo 
"""with open('cuento.txt' , 'w') as file:
    file.write('\n\nFin del cuento')"""

#conteo lineas
with open('cuento.txt' , 'r') as file:
    lineas = file.readlines()
    print(f'El archivo tiene {len(lineas)} lineas')

### Modos de apertura de archivos

# - 'r': **Lectura**. Da error si el archivo no existe.

# - 'w': **Escritura**. Sobrescribe el archivo si ya existe o lo crea si no.

# - 'a': **Agregar**. Añade al final del archivo si existe o lo crea si no.

# - 'x': **Crear**. Da error si el archivo ya existe.

# - 'b': **Modo binario** (se combina con los otros modos, por ejemplo, 'rb' para leer un archivo binario).