numero = int(input("Ingrese un número: "))

if numero > 0:
    if numero % 2 == 0:
        print(f"El número {numero} es positivo y es un número par.")
    else:
        print(f"El número {numero} es positivo y es un número impar.")
elif numero < 0:
    if numero % 2 == 0:
        print(f"El número {numero} es negativo y es un número par.")
    else:
        print(f"El número {numero} es negativo y es un número impar.")
else:
    print(f"El número es cero y por definición es par")


