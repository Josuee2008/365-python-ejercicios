#Day eight / Día 8/365
#Imprimir los números del 1 al 100
for numeros in range(1,101):
    print(numeros)


#Día 9/365
"""
Imprime la tabla de multiplicar 
de un número ingresado por el usuario
"""
#Solicita un número al usuario 

numero = int(input("Introduce un número, para ver su tabla de multiplicar: "))

#Genera la tabla de multiplicar

print(f"Tabla de multiplicar de {numero}:")
for i in range(1,11):
    print(f"{numero} x {i} = {numero * i} ")


#Día 10/365
#Programa que verifique si un año es bisiesto
#Solicita el año al usuario
año = int(input("Introduce un año: "))

#Verifica si el año es bisiesto 

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año}, es bisiesto.")
else: 
    print(f"El año {año}, no es bisiesto.")


#Día 11/365
#Adivina el número
import random
#Generar un número aleatorio entre el 1 y el 100
numero_secreto = random.randint(1,100)
intentos = 0
print("Bienvenido, Este es un juego sobre Adivinar un número entre 1 y 100")
print("Adivina el numero entre el rango de 1 y 100")

#Bucle para que el jugador intente adivinar 
while True:
    intento = int(input("Introduce tu adivinanza: "))
    intentos += 1
    if intento < numero_secreto:
        print("El numero es mas alto.")
    elif intento > numero_secreto:
        print("El numero es mas bajo")
    else:
        print(f"Felizidades, adivinaste el número secreto {numero_secreto}, en {intentos}, intentos")
        break


#Día 12/356
#Calcula el factorial de un número 
#Solicitar un número al usuario 
numero = int(input("Indtroduce un número, para calcular su factorial:"))

#Inicializar el factorial en 1
factorial = 1

#calcular el factrorial usando un bucle for
for i in range(1, numero + 1):
    factorial *= i #Multiplicar el valor actual por i
#Mostrar el resultado 

print(f"El factorial de {numero}, es {factorial}.")


#Día 13/365
#Imprimir los números primos menores a 100
print("Números primos menores a 100")

#Iterar del 2 al 99
for num in range(2,100):
    es_primo = True #Asumimos que el número es primo 

    #Verificar si num tiene divisores 
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            es_primo = False
            break #Salir del bucle 

#Si no tiene divisores, es primo 
    if es_primo:
        print(num, end=" ")


#Día 14/365
#Crea un programa que simule el lanzamiento de un dado.
import random

#Generamos un número aleatorio entre 1 y 6

dado = random.randint(1,6)

#Imprimimos el resultado 

print(f"El dado cayo en: {dado}")
