numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

numero = int(input("\nIngrese un número positivo (1 a 999): "))
if 1 <= numero <= 9:
    print("El número tiene un dígito.")
elif 10 <= numero <= 99:
    print("El número tiene dos dígitos.")
elif 100 <= numero <= 999:
    print("El número tiene tres dígitos.")
else:
    print("Número fuera del rango solicitado.")


n = int(input("\n¿Cuántos empleados tiene la empresa? "))
conta1 = conta2 = gastos = 0
for x in range(1, n + 1):
    sueldo = float(input(f"Ingrese el sueldo del empleado {x}: "))
    gastos += sueldo
    if 1000000 <= sueldo <= 3000000:
        conta1 += 1
    elif sueldo > 3000000:
        conta2 += 1

print(f"\nEmpleados con sueldo entre $1,000,000 y $3,000,000: {conta1}")
print(f"Empleados con sueldo mayor a $3,000,000: {conta2}")
print(f"Total gastado en sueldos: ${gastos:,.2f}")

cant1 = cant2 = cant3 = cant4 = 0
n = int(input("\nIngrese la cantidad de puntos a procesar: "))
for f in range(n):
    x = int(input(f"Ingrese la coordenada x del punto {f + 1}: "))
    y = int(input(f"Ingrese la coordenada y del punto {f + 1}: "))
    if x > 0 and y > 0:
        cant1 += 1
    elif x < 0 and y > 0:
        cant2 += 1
    elif x < 0 and y < 0:
        cant3 += 1
    elif x > 0 and y < 0:
        cant4 += 1

print(f"\nPuntos en el primer cuadrante: {cant1}")
print(f"Puntos en el segundo cuadrante: {cant2}")
print(f"Puntos en el tercer cuadrante: {cant3}")
print(f"Puntos en el cuarto cuadrante: {cant4}")

calificaciones = {
    "Juan": 4.8,
    "Ana": 5.0,
    "Luis": 4.7
}

nombre_max = max(calificaciones, key=calificaciones.get)
print(f"\nEl estudiante con la calificación más alta es {nombre_max} con una calificación de {calificaciones[nombre_max]}.")


estudiantes = {
    "Juan": 5.0,
    "Ana": 4.2,
    "Luis": 4.5
}

while True:
    nombre = input("\nIngrese el nombre del estudiante (o 'salir' para terminar): ").strip()
    if nombre.lower() == "salir":
        break
    calificacion = float(input(f"Ingrese la calificación de {nombre}: "))
    if nombre in estudiantes:
        print(f"Actualizando calificación de {nombre}.")
    else:
        print(f"Agregando nuevo estudiante: {nombre}.")
    estudiantes[nombre] = calificacion

print("\nLista de estudiantes y sus calificaciones:")
for nombre, calificacion in estudiantes.items():
    print(f"{nombre}: {calificacion:.2f}")
