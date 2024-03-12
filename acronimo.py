# Pedir al usuario que ingrese una oracion
nombre = input("escribe un nombre con apellidos para conocer su acronimo: ")


acróni = ''.join(word[0].upper() for word in nombre.split())

# Imprimir el acrónimo
print("El acrónimo de '" + nombre + "' es: " + acróni)