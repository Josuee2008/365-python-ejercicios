#Day One / Día uno de 366
#Hola muando 

print("Hola mundo!")

#Day two/ Día dos de 365
#Programa que pida al usuario su nombre y lo salude

nombre = input("Introduce tu nombre")

print(f"Saludos, {nombre}!")

#Day three/ Día tres de 365
#Calcular el área de un círculo dado su radio

import math

radio = float(input("Introduce el radio dek curculo: "))

area = math.pi * radio**2

print(f"El area dek circulo con radio {radio} es: {area:.2f5}")

#Day four/ Día 4/365
#Convierte una temperatura de Celsius a Fahrenheit.

#Solicitamos la temperatura en Celsius al usuario 

celsius = float(input("Introduce la temperatura en Celsius: "))

#Convertir la temperatura a Fahrenheit
fahrenheit = (celsius * 9/5) + 32

#Mostramos el resultado 

print(f"{celsius}°C equivale a {fahrenheit:.2f}°F")


#Day five / Día 5/366
"""
operaciones aritméticas básicas 
(suma, resta, multiplicación, división) 
con números ingresados por el usuario.

"""

#Solicita dos números al usuario 
numero1 = float(input("Introduce el primer número:"))
numero2 = float(input("Introduce el segundo número:"))

#Realiza las operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2


#Mostrar los resultados

print(f"\nResultados:")
print(f"Suma: {numero1} + {numero2} = {suma}")
print(f"Resta: {numero1} - {numero2} = {resta}")
print(f"Multiplicación: {numero1} x {numero2} = {multiplicacion}")
print(f"División: {numero1} / {numero2} = {division}")

#Day six / Día 6/356
#Programa que determine si un número es par o impar.

#Solicitar un número al usuario

numero = int(input("Introduce un número: "))

#Determinar si es par o impar

if numero % 2 == 0:
    print(f"El número {numero}, es par.")
else: 
    print(f"El número {numero}, es impar.")


#Day seven / Día 7/365
#Programa que determine el mayor de tres números.

#Solicitar tres números al usuario 

numero1 = float(input("Intoduce el primer número: "))
numero2 = float(input("Intoduce el segundo número: "))
numero3 = float(input("Intoduce el tercer número: "))

#Determine el mayor de los números

if numero1 >= numero2 and numero3:
    mayor = numero1
elif numero2 >= numero1 and numero3:
    mayor = numero2
else:
    mayor = numero3

#Mostrar el resultado 
print(f"El número mayor es: {mayor}")



