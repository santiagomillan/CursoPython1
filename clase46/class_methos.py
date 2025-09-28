class Counter:
    count = 0  # Variable de clase

    @classmethod
    def increment(cls):
        cls.count += 1  # Incrementa el contador cada vez que se crea una instancia


Counter.increment()
Counter.increment()
print(Counter.count)  # Muestra el valor del contador