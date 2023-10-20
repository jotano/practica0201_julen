frase = input("Introduce una frase:")
vocal = input("Introduce una vocal:")
if len(vocal) == 1 and vocal in "aeiouAEIOU":
    frase_modificada = frase.replace(vocal.lower(), vocal.upper())
    print("Aquí tienes tu frase modificada: ", frase_modificada)
input("Pulsa enter para salir")
