#Día 135 / 365
"""
 Buscador de Archivos por Tamaño
"""
import os
def buscar_archivos_por_tamaño(directorio, tamaño_min_kb):
    for raiz, _, archivos in os.walk(directorio):
        for archivo in archivos:
            ruta = os.path.join(raiz, archivo)
            tamaño = os.path.getsize(ruta) / 1024 #KB
            if tamaño > tamaño_min_kb:
                print(f"{ruta} - {tamaño:.2f} KB")

#Ejemplo: Buscar archivos > 500KB en el directorio actual
buscar_archivos_por_tamaño(".", 500)



#Día 136 / 365
"""
Visualizador de Datos en Terminal
(Gráficos ASCII con datos)
"""
def grafico_barras(datos):
    max_val = max(datos.values())
    for k, v in datos.items():
        barra = '█' * int(50 * v/max_val)
        print(f"{k.ljust(10)}: {barra} {v}")

grafico_barras({'Manzanas': 35, 'Naranjas': 20, 'Plátanos': 45})



#Día 137 / 365
"""
Adivina el Número (vs la Computadora)
"""
import random
numero = random.randint(1, 10)
intentos = 3

print("Adivina un número entre 1 y 10. Tienes 3 intentos")


while intentos > 0:
    guess = int(input("Tu intento: "))
    if guess == numero:
        print("¡Correcto!")
        break
    print("Más alto" if guess < numero else "Más bajo")
    intentos -= 1

if intentos == 0:
    print(f"¡Perdiste! El número esra {numero}")



#Día 138 / 365
"""
Generador de QR 
"""
# pip install qrcode

import qrcode

qr = qrcode.make(input("Texto/URL: "))
qr.save("qr.png")
print("¡QR generado!")


#Día 139 / 365
"""
Calendario Personalizado con Eventos
"""

import calendar
from datetime import datetime

eventos = {
    (2025, 5, 19): "Reunión importante",
    (2025, 5, 20): "Cumpleaños de Andres"
}

año, mes = 2025, 5
cal = calendar.monthcalendar(año, mes)

print(f"\nEventos de {calendar.month_name[mes]} {año}: ")
for semana in cal:
    for dia in semana:
        if dia != 0 and (año, mes, dia) in eventos:
            print(f"Día {dia}: {eventos[(año, mes, dia)]}")



#Día 149 / 365
"""
¿Cuántas veces puedes 
presionar ESPACIO en 10 segundos?
"""

import time
import msvcrt #Solo funciona en Windows

print("¡Presiona la barra ESPACIADORA tantas veces como puedas en 10 segundos!")
print("Comenzando en 3 segundos...")
time.sleep(3)
print("¡YA!")

contador = 0
tiempo_limite = 10 #Segundos
inicio = time.time()

while True:
    if msvcrt.kbhit():
        tecla = msvcrt.getch()
        if tecla == b' ':
            contador += 1

    if time.time() - inicio > tiempo_limite:
        break

print("\nTiempo terminado.")
print(f"Presionaste la barra ESPACIADORA {contador} veces en 10 segundos.")


#Día 141 / 365
"""
Calculadora de Edad de Mascotas
"""
 
edad_humana = int(input("Edad de tu perro/gato (en años humanos): "))
tipo = input("¿Es perro (P) o es gato (G)? ").upper()

if tipo == "P":
    edad_mascota = edad_humana * 7
else:
    edad_mascota = edad_humana * 5

print(f"Tu mascota tiene aproximadamente {edad_mascota} años 'animales'")

