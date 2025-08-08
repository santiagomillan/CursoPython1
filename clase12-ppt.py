tijeras = "t"
Papel = "p"
Piedra = "r"

input_usuario1 = input("Elige tijeras (t), papel (p) o piedra (r): ").lower()
if input_usuario1 == tijeras:
    print("Has elegido tijeras.")
elif input_usuario1 == Papel:
    print("Has elegido papel.")
elif input_usuario1 == Piedra:
    print("Has elegido piedra.")
else:
    print("Opción no válida. Por favor, elige tijeras (t), papel (p) o piedra (r).")


input_usuario2 = input("Elige tijeras (t), papel (p) o piedra (r): ").lower()
if input_usuario2 == tijeras:
    print("Has elegido tijeras.")
elif input_usuario2 == Papel:
    print("Has elegido papel.")
elif input_usuario2 == Piedra:
    print("Has elegido piedra.")
else:
    print("Opción no válida. Por favor, elige tijeras (t), papel (p) o piedra (r).")

eleccion = input_usuario1 + " , " + input_usuario2
print("Eleccion " + eleccion)
if input_usuario1 == input_usuario2:
    print("Empate")
##tijeras gana a papel
##piedra gana a tijeras
##papel gana a piedra
# logica para validar en base a las combinaciones como ver quien gana
if (input_usuario1 == tijeras and input_usuario2 == Papel) or \
   (input_usuario1 == Papel and input_usuario2 == Piedra) or \
   (input_usuario1 == Piedra and input_usuario2 == tijeras):
    print("Jugador 1 gana")
elif (input_usuario2 == tijeras and input_usuario1 == Papel) or \
     (input_usuario2 == Papel and input_usuario1 == Piedra) or \
     (input_usuario2 == Piedra and input_usuario1 == tijeras):
    print("Jugador 2 gana")
else:
    print("Nadie gana")