# contador de palabras


# Se ingresa un string
text = input("Ingresa una oración: ")

# Contar el número de palabras, separar con split
number_words = len(text.split())

print(f"La oración que has ingresado : \'{text}\' tiene {number_words} palabras.")