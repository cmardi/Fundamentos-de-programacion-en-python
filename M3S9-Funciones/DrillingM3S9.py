def operaciones(a, b):
    def division(a, b):
        if b == 0:
            return "Error: división por cero no está permitido"
        return round(a / b, 2)
    return {
        "Suma": a + b,
        "Resta": a - b,
        "Multiplicación": a * b,
        "División": division(a, b)
    }
a = int(input(f"Ingrese un número:\n"))
b = int(input(f"Ingrese un número:\n"))

resultado = operaciones(a, b)
print(resultado)

#Otra forma de hacerlo, también funcional:

# def operaciones(a, b):
#     def suma(a, b):
#         return a + b
#     def resta(a, b):
#         return a - b
#     def multiplicacion(a, b):
#         return a * b
#     def division(a, b):
#         if b == 0:
#             return "Error: división por cero no está permitido"
#         return round(a / b, 2)
#     return {
#         "Suma": suma(a, b),
#         "Resta": resta(a, b),
#         "Multiplicación": multiplicacion(a, b),
#         "División": division(a, b)
#     }

# a = int(input(f"Ingrese un número:\n"))
# b = int(input(f"Ingrese un número:\n"))

# resultado = operaciones(a, b)
# print(resultado)
    