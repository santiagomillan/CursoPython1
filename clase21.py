def sum_numbers(n):
    # Caso base: si n es 0, la suma es 0
    if n == 0:
        return 0
    # Caso recursivo: n + suma de (n-1)
    else:
        return n + sum_numbers(n - 1)

# Llamada a la funciÃ³n
result = sum_numbers(5)
print(f"Suma de los primeros 5 numeros es: {result}")


def fibo(n):
    # Caso base: si n es 0, la suma es 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

# Llamada a la funciÃ³n
number = 3
print(f"Fibonacci de {number} es: {fibo(number)}")