'''¿Qué son las variables locales y globales?
En el fascinante mundo de la programación, comprender la vida útil de una variable es vital para evitar errores comunes y mejorar el rendimiento del código. Las variables locales y globales juegan un papel crucial en este ámbito. Mientras que las variables locales existen sólo dentro de un bloque de código determinado, las variables globales pueden ser accedidas desde cualquier parte del programa.

¿Cómo trabajan las variables locales?
Para ilustrar este concepto, imaginemos una función que crea una variable local en Python. Aquí, la variable x es asignada al número 10. Esta variable es de tipo local porque solo persiste y puede ser accesada dentro del cuerpo de la función donde se define.
'''
def funcion_local():
    x = 10  # Variable local
    print("El valor de la variable es", x)

funcion_local()
'''Al llamar a funcion_local(), se imprime el valor de x. Sin embargo, intentar acceder a x fuera de la función genera un error, ya que x no está definida globalmente.

¿Cómo se comportan las variables globales?
En contraste, una variable global x puede ser definida fuera de cualquier función, lo que permite que su valor sea accedido o modificado desde cualquier parte del programa.'''

x = 100  # Variable global

def mostrar_variable_global():
    print("El valor de la variable global es", x)

mostrar_variable_global()
'''En este caso, imprimir x desde la función mostrar_variable_global() no genera errores, mostrando su valor globalmente definido.

¿Cómo combinar funciones internas y externas?
Las funciones pueden anidar otras funciones internamente. En tal caso, se debe prestar especial atención al alcance de las variables definidas.

Usando variables globales con funciones internas
Supongamos que tenemos una variable global y deseamos modificar sus valores a través de funciones interiores y exteriores.'''

x = "global"  # Variable global

def funcion_externa():
    x = "externa"  # Redefine 'x' en el ámbito de la función externa

    def funcion_interna():
        x = "local"  # Redefine 'x' en el ámbito de la función interna
        print(x)

    funcion_interna()
    print(x)

funcion_externa()
print(x)
'''Al ejecutar este código, se observa cómo los distintos valores de x son imprimidos dependiendo del ámbito de la función donde se encuentren.

¿Qué son las variables nonlocal?
Las variables nonlocal actúan como un puente entre variables locales y globales, permitiendo que las funciones internas accedan y modifiquen variables en funciones 'encapsulantes' externas.'''

def funcion_externa():
    x = "inicial"

    def funcion_interna():
        nonlocal x
        x = "modificado"
        print("El valor en inner es", x)

    funcion_interna()
    print("El valor afuera es", x)

funcion_externa()
'''En este ejemplo, la variable x se marca como nonlocal, permitiendo que la función interna modifique su valor, y se refleja tanto dentro como fuera de funcion_interna().

¡Nunca dejes de explorar nuevos conceptos en programación! El entendimiento profundo de variables locales, globales y nonlocal refuerza una base sólida para construir aplicaciones más sofisticadas y robustas. ¡Sigue aprendiendo y realizando retos que pongan a prueba tus habilidades!'''