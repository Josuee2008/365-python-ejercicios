#Día 149 / 365
"""
visualizador de ecuaciones en consola
"""
import math

#Configuración 
ancho = 80 #número de columnas
alto = 25 #número de filas
x_min = -10
x_max = 10
step = (x_max - x_min) / ancho

#Entrada del usuario
expr = input("Ingresa una función f(x): ")

#Crear lista de puntos
puntos = []
y_min, y_max = float('inf'), float('-inf')
for i in range(ancho):
    x = x_min + i * step
    try:
        y = eval(expr, {"x": x, "math": math, "abs": abs})
        puntos.append((x, y))
        y_min = min(y_min, y)
        y_max = max(y_max, y)
    except:
        puntos.append((x, None))

#Normalizar y graficar
for fila in range(alto, -1, -1):
    y_actual = y_min + (y_max - y_min) * fila / alto
    linea = ""
    for x, y in puntos:
        if y is None:
            linea += " "
        elif abs(y - y_actual) < (y_max - y_min) /alto /2:
            linea += "*"
        elif abs(y_actual) < (y_max - y_min) / alto / 2:
            linea += "-" #Eje x
        else:
            linea += " "
    print(linea)

#Etiquetas
print(" " * (ancho // 2 - 4) + f"x ∈ [{x_min}, {x_max}]")


#Día 150 / 365
"""
Verificación de contraseña
"""
#Almacenar la contrasñea en una variable
contraseña_correcta = "python123"

#Solicitar al usuario que ingrese la contraseña
entrada = input("Introduce la contraseña: ")

#Repetir mientras la contraseña ingresada no sea correcta
while entrada != contraseña_correcta:
    print("Contraseña incorrecta. Intentalo de nuevo.")
    entrada = input("Introduce la contrasela: ")

print("¡Contrasñea correcta! Bienvenido.")


#Día 151 / 365
"""
Ventas por año con descuento
 usando Pandas 🐼💸
"""

import pandas as pd

#Solicictar al usuario el año inicial y final
inicio = int(input("Introduce el año inicial: "))
fin = int(input("Introdice el año final: "))

#Creamos un diccionario para guardar las ventas por año
ventas = {}

#Solicitamos al usuario las ventas de cada año en el rango 
for año in range(inicio, fin + 1):
    monto = float(input(f"Introduce las ventas del año {año}: "))
    ventas[año] = monto

#convertir el diccionario a una serie de pandas
serie_ventas = pd.Series(ventas)

#Mostrar las ventas originales
print("\nVentas por año:")
print(serie_ventas)

#Aplicara el descuento del 10%
ventas_descuento = serie_ventas * 0.9

#Mostramos las ventas con descuento 
print("\nVentas con descuento (10%):")
print(ventas_descuento)
