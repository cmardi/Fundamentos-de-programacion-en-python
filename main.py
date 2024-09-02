def clasificar_producto():

    tipo_producto = input("Ingrese el código de tipo del producto (A, B, C): \n").upper()
    peso = float(input("Ingrese el peso del producto (kg): \n"))
    fragilidad = input("Ingrese la fragilidad del producto (F o N): \n").upper()
   
    if peso >= 20:
        peso_categoria = "Pesado"
    elif peso >= 10:
        peso_categoria = "Mediano"
    else:
        peso_categoria = "Ligero"
      

    if tipo_producto == "A":
        if peso_categoria == "Pesado" and fragilidad == "F":
            print("Producto alimenticio pesado y frágil: Manejar con extremo cuidado")
        elif peso_categoria == "Mediano" and fragilidad == "F":
            print( "Producto alimenticio mediano y frágil: Manejar con cuidado")
        else:
            print("Producto alimenticio ligero: Manejar con cuidado estándar")
    
    if tipo_producto == "B":
        if fragilidad == "F":
            print("Producto electrónico frágil: Manejar con cuidado")
        elif fragilidad == "N" and peso_categoria != "Pesado":
            print("Producto electrónico pesado y no frágil: Manejar con precaución")
        else:
            print("Producto electrónico no frágil: Manejo estándar")
    
    if tipo_producto == "C":
        if peso_categoria == "Pesado" and fragilidad == "F":
            print("Manejar con precaución adicional")
        elif peso_categoria == "Pesado" and fragilidad == "N":
            print("Manejo estándar")
        elif peso_categoria != "Pesado":
            print("Producto no pesado: Manejo estándar")
  


clasificar_producto()



        





