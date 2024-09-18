"""
Nota: Los comentarios añadidos al final corresponden al formato inicial y es totalmente funcional.

"""
nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pelé", "Juanes"]

nombres_magos, nombres_cientificos = {0, 2, 5}, {1, 3, 6}

magos= [nombres[i] for i in range(len(nombres)) if i in nombres_magos]
cientificos = [nombres[i] for i in range(len(nombres)) if i in nombres_cientificos]
otros = [nombres[i] for i in range(len(nombres)) if i not in nombres_magos and i not in nombres_cientificos]

print(f"\nMagos: {", ".join(magos)} \nCientíficos: {", ".join(cientificos)} \nOtros: {", ".join(otros)}\n")
#join() toma la lista y crea una nueva cadena concatenando cada elemento con el separador especificado.

def hacer_grandioso(*args):
    for args in magos:
        print("El gran " + args)
    
def imprimir_nombres(*args):

    print("\nTodos los nombres antes de ser modificados:\n", *[f"* {args}" for args in nombres], sep="\n")
    print("\nLos nombres de los magos grandiosos:\n", *[f"* {args}" for args in magos], sep="\n")
    print("\nLos nombres de los científicos:\n", *[f"* {args}" for args in cientificos], sep="\n")
    print("\nLos nombres restantes:\n", *[f"* {args}" for args in otros], sep="\n")
    print()

hacer_grandioso(magos)
imprimir_nombres(nombres, magos, cientificos, otros) 

# nombres = [
#     "Harry Houdini",
#     "Newton",
#     "David Blaine",
#     "Hawking",
#     "Messi",
#     "Teller",
#     "Einstein",
#     "Pele",
#     "Juanes"
# ]

# magos = []
# cientificos = []
# otros = []

# nombres_magos = {0, 2, 5}
# nombres_cientificos = {1, 3, 6}

# for nombre in range(len(nombres)):          
#     if nombre in nombres_magos:
#         magos.append(nombres[nombre])
#     elif nombre in nombres_cientificos:
#         cientificos.append(nombres[nombre])
#     else:
#         otros.append(nombres[nombre])

# print()
# print(f"Magos: ",magos)
# print(f"Científicos: ",cientificos)
# print(f"Otros: ",otros)
# print()
##print(f"\nMagos: {magos} \nCientíficos: {cientificos} \nOtros: {otros}\n")

# def hacer_grandioso(magos):
#     for nombre in range(len(magos)):
#         print("El gran " + magos[nombre])

# def imprimir_nombres(*args):
#     print("\nTodos los nombres antes de ser modificados:\n")
#     for args in nombres:
#         print("* " + args)
#     print("\nLos nombres de los magos grandiosos:\n")
#     for args in magos:
#         print("* " + args)
#     print("\nLos nombres de los científicos:\n")
#     for args in cientificos:
#         print("* " + args)
#     print("\nLos nombres restantes:\n")    
#     for args in otros:
#         print("* " + args)
#     print()
    
# hacer_grandioso(magos)
# imprimir_nombres(nombres, magos, cientificos, otros)  