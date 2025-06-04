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


#Día 152/ 365
"""
Gráfico de Distribución de Productos por Categoría
"""
import pandas as pd
import matplotlib.pyplot as plt

def graficar_distribucion_productos(productos, tipo):
    tipos = {
        'barras': 'bar',
        'sectores': 'pies',
        'horizontal' : 'barh'
    }

    if tipo not in tipos:
        print("Tipos de graficos no válidos. Usa: 'barras', 'sectores' o 'horizontales'.")
        return
    
    plt.figure(figsize=(7, 5))

    if tipo == 'sectores':
        productos.plot.pie(autopct='%1.1f%%')
        plt.ylabel('')
        plt.title('Distribución de Productos por Categoría')
    else:
        productos.plot(kind=tipos[tipo])
        plt.title('Cantidad de Productos por Categoría')
        plt.xlabel('Categoria' if tipo == 'barras' else 'Cantidad')
        plt.ylabel('Cantidad' if tipo == 'barras' else 'Categoría')

    plt.tight_layout()
    plt.show()

#Datos de ejemplo
inventario = pd.Series({
    'Ropa': 120,
    'Tecnología': 80,
    'Alimentos': 150,
    'Juguetes': 60,
    'Libros': 90
})

#Llamada a la función
graficar_distribucion_productos(inventario, 'barras')
graficar_distribucion_productos(inventario, 'sectores')
graficar_distribucion_productos(inventario, 'horizontal')


#Día 153 / 365
"""
Cómo leer un 
archivo CSV en Python 📄📬
"""
import csv
def procesar_csv(archivo):
    with open(archivo, mode='r', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        return [fila for fila in lector]
    
#Ejemplo de uso:
datos = procesar_csv('datos_usuarios.csv')
for usuarios in datos:
    print(usuarios['nombre'], usuarios['email'])



#Día 154 / 365
"""
Extrae precios de productos 
desde una página web (web scraping básico)
"""

import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'

response = requests.get(url)
response.encoding = response.apparent_encoding

soup = BeautifulSoup(response.text, 'html.parser')

productos = soup.find_all('article', class_='product_pod')

for producto in productos:
    titulo = producto.h3.a['title']
    precio = producto.find('p', class_='price_color').text
    print(f'{titulo} - {precio}')
