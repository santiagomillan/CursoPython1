'''¿Qué son las anotaciones en Python?
Las anotaciones en Python son una herramienta que permite agregar información adicional sobre las variables, funciones y métodos que programamos. Aunque no restringen el tipo de datos que se puede almacenar en una variable, proporcionan un contexto más claro sobre el objetivo del código, beneficiando la legibilidad y comprensión, especialmente en entornos de trabajo en equipo.

¿Cómo se utilizan las anotaciones en las variables?
Las anotaciones para las variables consisten en especificar el tipo esperado usando dos puntos seguidos de la declaración del tipo. Por ejemplo, al crear un identificador para empleados, podríamos especificarlo de la siguiente manera:
'''
id1: int = 101
id2: int = 102
'''Al realizar operaciones, también podemos anotar el tipo de resultado:'''

total_id: int = id1 + id2
'''¿Cómo se implementan en funciones y métodos?
En las funciones, las anotaciones ayudan a definir los tipos de datos que los parámetros deben recibir y el tipo de dato que devolverá la función. La sintaxis se asemeja a esto:
'''
def sumar_ids_empleados(id1: int, id2: int) -> int:
    return id1 + id2
'''En este ejemplo, se especifica que los parámetros id1 y id2 deben ser enteros y que el resultado también será un entero.

¿Cómo usar anotaciones en clases?
Al trabajar con clases, las anotaciones ayudan a definir tipos de los atributos y métodos. Veamos un ejemplo de una clase Empleado:
'''
class Empleado:
    def __init__(self, nombre: str, edad: int, salario: float):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def presentarse(self) -> str:
        return f"Hola, me llamo {self.nombre}. Tengo {self.edad} años."
'''Aquí se utilizan anotaciones para definir los tipos de parámetros esperados en el constructor y el tipo de dato que devuelve el método presentarse.

¿Cómo verificar tipos de datos usando librerías?
Además de las anotaciones, es posible utilizar herramientas como MyPy para analizar estáticamente el tipo de datos en un archivo Python, buscando posibles inconsistencias o errores. MyPy no es parte de la biblioteca estándar de Python, por lo que necesitas instalarlo:

pip install mypy
Luego, puedes usarlo para analizar un archivo:

mypy mi_archivo.py
¿Qué son Optional y Union?
Las librerías Optional y Union permiten mayor flexibilidad en las anotaciones al trabajar con funciones que pueden manejar múltiples tipos de datos o retornar None.

Optional: Indica que un valor podría ser del tipo especificado o None.'''
from typing import Optional

def encontrar_empleado(ids: list[int], id_buscado: int) -> Optional[int]:
    if id_buscado in ids:
        return id_buscado
    return None
#Union: Se usa cuando necesitas aceptar múltiples tipos de datos específicos, pero no None.
from typing import Union

def procesar_salario(salario: Union[int, float]) -> float:
    return float(salario)
'''Retos y recomendaciones prácticas
Te animamos a aplicar estos conceptos creando una función que procese diccionarios de empleados y los filtre según el salario. Experimenta con diferentes tipos de anotaciones y comparte tus resultados en los comentarios.

¡Continúa explorando y experimentando con Python! Las anotaciones son solo el comienzo para lograr un código más entendible y fácil de mantener.'''