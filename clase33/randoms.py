import random

# Generar un número aleatorio
random_number = random.randint(1, 10)
print(f"Random number between 1 and 10: {random_number}")

#Elegir colores aleatorios
colors = ['Rojo', 'Azul', 'Verde']
random_color = random.choice(colors)
print(random_color)

#Barajar una lista de cartas
cards = ['As', 'Rey', 'Reina', 'Jota', '10']
random.shuffle(cards)
print(cards)