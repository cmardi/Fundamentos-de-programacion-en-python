lista = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]] 
lista2 = []
diccionario = {
    "A": lista[0],
    "B": lista[1],
    "C": lista[2],
    "D": lista[3]
}

for clave, sublista in diccionario.items():
    if sublista[0] == 0:
        continue
    lista2 = [num for num in sublista if num != 0 ]

print(f"{clave}:{lista2}")

print(diccionario)


