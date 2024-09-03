Problema: Sistema de Clasificación de Productos en un Almacén

 Descripción:

 Estás encargado de desarrollar un sistema para clasificar productos en un almacén.
 Cada producto tiene un código que identifica su tipo, su peso y su categoría de
 fragilidad. Tu tarea es escribir un programa que clasifique cada producto según estos
 criterios utilizando sentencias condicionales anidadas y operadores lógicos.
 Requerimientos:

 1. Tipo de Producto:
 El código de tipo del producto puede ser 
"A" : Productos alimenticios.
 "B" : Productos electrónicos.
 "C" : Otros productos.

 2. Peso del Producto:
 "A" , 
"B" o 
"C" .
 Si el peso del producto es mayor o igual a 20 kg, se considera "Pesado".
 Si el peso es menor a 20 kg pero mayor o igual a 10 kg, se considera
 "Mediano".
 Si el peso es menor a 10 kg, se considera "Ligero".

 3. Fragilidad del Producto:
 La categoría de fragilidad puede ser 
Clasificación Final:
 Tu programa debe:
 "F" (Frágil) o 
"N" (No frágil).
 Imprimir la categoría final del producto según las siguientes reglas:

 1. Productos alimenticios ( A ):

 Si es pesado y frágil, imprimir "Producto alimenticio pesado y
 frágil: Manejar con extremo cuidado".
 Si es mediano y frágil, imprimir "Producto alimenticio mediano y
 frágil: Manejar con cuidado".
 Si es ligero, sin importar si es frágil o no, imprimir "Producto
 alimenticio ligero: Manejar con cuidado estándar".
 2. Productos electrónicos ( B ):

 Si es frágil, sin importar el peso, imprimir "Producto electrónico
 frágil: Manejar con cuidado".
 Si no es frágil y pesado, imprimir "Producto electrónico pesado y
 no frágil: Manejar con precaución".
 Si no es frágil y mediano o ligero, imprimir "Producto electrónico
 no frágil: Manejo estándar".
 3. Otros productos ( C ):

 Si es pesado y frágil, imprimir "Producto pesado y frágil: Manejar
 con precaución adicional".
 Si es pesado y no frágil, imprimir "Producto pesado y no frágil:
 Manejo estándar".
Si es mediano o ligero, sin importar la fragilidad, imprimir
 "Producto no pesado: Manejo estándar".
 Ejemplo de Entrada y Salida:
 
 1. Entrada:
 Código de tipo: 
Peso: 
25
 Fragilidad: 
Salida:
 "A"
 "F"
 "Producto alimenticio pesado y frágil: Manejar con extremo cuidado"
 2. Entrada:
 Código de tipo: 
Peso: 8
 Fragilidad: 
Salida:
 "B"
 "N"
 "Producto electrónico no frágil: Manejo estándar"
 3. Entrada:
 Código de tipo: 
Peso: 
15
 Fragilidad: 
Salida:
 "C"
 "F"
 "Producto no pesado: Manejo estándar"
 Puntos a tener en cuenta:
 Debes utilizar sentencias condicionales anidadas y operadores lógicos (
 and ,
 or ) para manejar las distintas combinaciones de condiciones.
 Asegúrate de manejar correctamente todos los posibles casos de entrada.
 Puedes agregar validaciones adicionales para asegurarte de que las entradas
 sean correctas, como verificar que el peso sea un número positivo y que los
 códigos de tipo y fragilidad sean válidos