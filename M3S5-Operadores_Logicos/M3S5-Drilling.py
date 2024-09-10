palabra = "paralelepípedo"
vocales = "aeiouáéíóú"

i = 0

while i < len(palabra):
    consonante = palabra[i]

    if consonante.lower() in vocales:
        i += 1
        continue

    print(f"Consonante: {consonante}, Posición: {i}")
    i += 1