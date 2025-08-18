# generator
def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4

for value in my_generator():
    print(value)

# Fibonacci generator
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)