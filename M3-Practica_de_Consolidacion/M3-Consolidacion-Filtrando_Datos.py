nombres = [
    "Harry Houdini",
    "Newton",
    "David Blaine",
    "Hawking",
    "Messi",
    "Teller",
    "Einstein",
    "Pele",
    "Juanes"
]

magos = []
cientificos = []
otros = []

nombres_magos = {0, 2, 5}
nombres_cientificos = {1, 3, 6}

# for nombre in range(len(nombres)):          
#     if nombre in nombres_magos:
#         magos.append(nombres[nombre])
#     elif nombre in nombres_cientificos:
#         cientificos.append(nombres[nombre])
#     else:
#         otros.append(nombres[nombre])

magos= [nombres[i] for i in range(len(nombres)) if i in nombres_magos]
cientificos = [nombres[i] for i in range(len(nombres)) if i in nombres_cientificos]
otros = [nombres[i] for i in range(len(nombres)) if i not in nombres_magos and i not in nombres_cientificos]

print()
print(magos)
print(cientificos)
print(otros)
print()

def hacer_grandioso(magos):
    for nombre in range(len(magos)):
        print("El gran " + magos[nombre])

def imprimir_nombres(nombres, magos, cientificos, otros):
    print("\nTodos los nombres antes de ser modificados:\n")
    for nombre in nombres:
        print("* " +nombre)
    print("\nLos nombres de los magos grandiosos:\n")
    for nombre in magos:
        print("* " +nombre)
    print("\nLos nombres de los científicos:\n")
    for nombre in cientificos:
        print("* " +nombre)
    print("\nLos nombres restantes:\n")    
    for nombre in otros:
        print("* " +nombre)
    print()

hacer_grandioso(magos)
imprimir_nombres(nombres, magos, cientificos, otros)       
