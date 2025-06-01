#Día 120 / 365
"""
"Simulador de Lluvia en Consola" 
    (Rain Animation)
"""
import random
import time
import os
from colorama import init, Fore, Style

init(autoreset=True)

def rain_simulator_colored(width=60, height = 20, chars ='01', delay = 0.1):
    columns = [0] * width
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            for row in range(height):
                line = ''
                for col in range(width):
                    if random.random() > 0.975:
                        columns[col] = height
                    if columns[col] > 0:
                        char = random.choice(chars)
                        line += Fore.GREEN + char
                        columns[col] -= 1
                    else:
                        line += ' '
                print(line)
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\nAnimación detenida")
rain_simulator_colored()


#Día 121 / 365
"""
Calculadora de comisión 
    para vendedores
"""
ventas = float(input("¿Cuánto vendiste este mes?: "))

comisione_porcentaje = float(input("¿Cuál es tu porcentaje de comison?: "))

comision = ventas * (comisione_porcentaje / 100)

print(f"Tu comisión del mes es: ${comision:.2f}")


#Día 122 / 365
"""
Calculadora de consumo eléctrico
"""

watts = float(input("¿Cuántos watts consume el aparato?: "))
horas_por_dia = float(input("¿Cuántas horas al día lo usaras?: "))
dias_por_mes = int(input("¿Cuántos días al mes lo usas?: "))

consumo_kwh = (watts * horas_por_dia * dias_por_mes) / 100

precio_kwh = float(input("¿Cuál es el precio por kWh en tu ciudad?: "))

costo_total = consumo_kwh * precio_kwh

print(f"Consumo mensual: {consumo_kwh:.2f} KWh")
print(f"Costo total mensual: ${costo_total:.2f}")


#Día 123 / 365
"""
Simulador de aumento de sueldo anual
"""

habitaciones = int(input("¿Cuántas habitaciones alquilas? "))
dias_alquiladas = int(input("¿Cuántos días al mes alquilas cada habitación? "))
precio_noche = float(input("¿Cuánto cobras por noche? "))

ganancias_mesnuales = habitaciones * dias_alquiladas * precio_noche

ganancias_anuales = ganancias_mesnuales * 12

print(f"Ganancias mensuales: ${ganancias_mesnuales:.2f}")
print(f"Ganancias anuales: ${ganancias_anuales:.2f}")


#Día 124 / 365
"""
Calculadora de salario 
por horas trabajadas con extras
"""
horas_trabajadas = float(input("¿Cuántas horas trabajaste esta semana? "))
pago_por_hora = float(input("¿Cuánto ganas por hora? "))

if horas_trabajadas <= 4:
    salario = horas_trabajadas * pago_por_hora
else:
    horas_normales = 40
    horas_extras = horas_trabajadas - 40
    salario = (horas_normales * pago_por_hora) + (horas_extras * pago_por_hora * 1.5)

print(f"Tu salario total es: ${salario:.2f}")


#Día 125 / 365
"""
Calculando el costo total de 
una suscripción con descuentos
"""
precio_mensual = 15.0

meses = int(input("¿Cuántos meses de suscripción deseas pagar? "))

subtotal = precio_mensual * meses

if 3 <= meses <= 5:
    descuento = 0.10
elif meses >= 6:
    descuento = 0.20
else:
    descuento = 0.0

total_decuento = subtotal * descuento
total = subtotal - total_decuento

print(f"Subtotal: ${subtotal:.2f}")
print(f"Descuento aplicado: ${total_decuento:.2f}")
print(f"Total a pagar: ${total:.2f}")


#Día 126 / 365
"""
 Mini agenda de contactos con SQLite
"""
import sqlite3

conn = sqlite3.connect("agenda.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS contactos (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          nombre TEXT,
          telefono TEXT)''')

nombre = input("Nombre del contacto: ")
telefono = input("Teléfono: ")
c.execute("INSERT INTO contactos (nombre, telefono) VALUES (?, ?)", (nombre, telefono))
conn.commit()

print("\nLista de contactos:")
for fila in c.execute("SELECT * FROM contactos"):
    print(f"{fila[0]} - {fila[1]}: {fila[2]}")
conn.close()


#Día 127 / 365
"""
Control de aforo en una tienda
"""
aforo_maximo = 20
personas_ectuales = 0

while True:
    print(f"\Personas actuales en la tienda: {personas_ectuales}/{aforo_maximo}")
    accion = input("¿Qué quieres hacer? (entrar/salir/salir del sistema): ").lower()

    if accion == "entrar":
        cantidad = int(input("¿Cuántas personas quieres entrar?"))
        if personas_ectuales + cantidad <= aforo_maximo:
            personas_ectuales += cantidad
            print(f"Entraron {cantidad} personas.")
        else:
            print("No se puede superar el aforo máximo.")
    elif accion == "salir":
        cantidad = int(input("¿Cuántas personas van a salir? "))
        if cantidad <= personas_ectuales:
            personas_ectuales -= cantidad
            print(f"Salieron {cantidad} personas.")
        else:
            print("No pueden salir más personas de las que hay.")
    elif accion == "salir del sistema":
        print("Saliendo del sistema. Gracias!")
    else:
        print("Opción no válida. Usa: entrar, salir o salir del sistema.")
