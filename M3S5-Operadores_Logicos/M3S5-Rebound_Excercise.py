n = int(input("Ingrese el número para calcular el factorial: "))
resultado = 1
while n > 0:
    resultado *= n
    n -= 1
   
print(f"El factorial es {resultado}")


