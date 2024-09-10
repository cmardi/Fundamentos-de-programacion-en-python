estudiantes = [ 
{'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]}, 
{'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]}, 
{'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]}, 
{'nombre': 'Ana', 'edad': 18, 'calificaciones': [90, 92, 87]}, 
{'nombre': 'Luis', 'edad': 20, 'calificaciones': [88, 85, 92]}, 
] 

for estudiante in estudiantes:
    if estudiante['edad'] > 18:
        calificaciones = estudiante['calificaciones']
        promedio = sum(calificaciones) / len(calificaciones)
        if promedio > 85:
            print()
            print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Promedio: {promedio}")
            
suma_promedios = 0
contador = 0

for estudiante in estudiantes:
    edad = estudiante['edad']
    if edad > 18:
        if edad <=1:
            est_primo = False
        else: 
            est_primo = True
            for i in range(2, int(edad**0.5) + 1):
                if edad % i == 0:
                    est_primo = False
                    break

        if est_primo:
            calificaciones = estudiante['calificaciones']
            promedio = sum(calificaciones) / len(calificaciones)
            suma_promedios += promedio
            contador += 1

if contador > 0:
    print()
    promedio_general = suma_promedios / contador
    print(f"Promedio general de calificaciones: {promedio_general}")
    print()
else:
    print("No hay estudiantes mayores de 18 años con edad primo")