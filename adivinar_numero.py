# Programa adivina el numero - Guess the number

import random

num_oculto = random.randint(1,50)
intentos = 0
continuar_jugando = True

while continuar_jugando:
    intentos += 1
    num_u = int(input("\ncaptura  un número entre 1 y 50: "))

    if intentos >= 10:
        print(f"\nlo siento, ya se te acabo tus oportunidades  lo has intentado muchas veces, el numero buscabas era era {num_oculto}.")
        respuesta = input("\n¿Quieres iniciar de nuevo? (s/n)")
        if respuesta.lower() == "s":
            num_oculto = random.randint(1,50)
            intentos = 0
        else:
            continuar_jugando = False
    else:
        if num_u < 1 or num_u > 50:
            print("Error: el número debe estar entre 1 y 50")
        elif num_u < num_oculto:
            print("El número que buscas  es mayor")
        elif num_u > num_oculto:
            print("El número que buscas  es menor")
        else:
            print("\n¡muchas felicidades, has logrado adivinar el unmero en  ", intentos, "intentos!")
            respuesta = input("\n¿Quieres seguir jugando? (s/n)")
            if respuesta.lower() == "s":
                num_oculto = random.randint(1,50)
                intentos = 0
            else:
                continuar_jugando = False

print("espero vuelvas pronto, gracias!")