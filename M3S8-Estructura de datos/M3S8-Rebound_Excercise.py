
mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15] 

#Eliminar los elementos duplicados:
print("\n--------------------------------\n")
mi_lista2 = set(mi_lista)
print(mi_lista2)
mi_lista = list(mi_lista2)
print(mi_lista)
print("\n--------------------------------\n")

#Ordenar la lista resultante en orden ascendente:
mi_lista.sort()
print(mi_lista)
print("\n--------------------------------\n")