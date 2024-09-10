numeros = [20,17,2,0,24,-55,36,97,-8,13]

for numero in numeros:
    if numero == 0:
        print(f"El número {numero} es cero y es par.\n")
    elif numero % 2 == 0:
        print(f"El número {numero} es par.\n")
    else:
        print(f"El número {numero} es impar.\n")
