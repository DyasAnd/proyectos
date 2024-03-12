import random

# JUEGO: PIEDRA PAPEL O TIJERA

aleatoria = random.randrange(0,3)
pc = ""
print("OPCIONES\n")
print("1) Piedra \n2) Papel\n Tijera")
opcion = int(input("elige una opcion"))

if opcion == 1:
    usuario = "piedra"
elif opcion == 2:
    usuario = "papel"
elif opcion ==3:
    usuario = "Tijera"
print("tu seleccionaste  ",usuario)


if aleatoria == 1:
    pc = "piedra"
elif aleatoria == 2:
    pc = "papel"
elif aleatoria ==3:
    pc = "Tijera"
print("la, maquina eligio  ", pc)



if pc == "piedra" and usuario == "papel":
    print("has ganado, el papel envuelve piedra")
elif pc == "papel" and usuario == "tijera":
    print("has ganado, tijera corta papel")
elif pc == "tijera" and usuario == "[piedra]":
    print("has ganado, piedra despedaza a la tijera")


f pc == "papel" and usuario == "piedra":
    print("has perdiddo, el papel envuelve piedra")
elif pc == "tijera" and usuario == "papel":
    print("has ganado, tijera corta papel")
elif pc == "piedra" and usuario == "[tijera]":
    print("has ganado, piedra despedaza a la tijera")
elif pc == usuario:
    print("Empate")


