#Día 29/365
""""
Hoy creamos un programa que genera una contraseña aleatoria segura.
"""
import random
import string

#Definimos las caracteres permitidos
caracteres = string.ascii_letters + string.digits + string.punctuation

#Solicitar la longuitud de la contraseña 
longitud = int(input("Ingresar la longuitud de la contraseña: "))

#Generar la contraseña aleatoria 
contraseña = "".join(random.choices(caracteres, k=longitud))

#Mostramos la contraseña generada
print(f"Contraseña generada: {contraseña}")

#Día 30/365
#Calcular propina

def calcular_propina(cuenta, porcentaje_propina, persona):
    #Calcular la propina 
    propina = cuenta * (porcentaje_propina / 100)

    #Calcular el total a pagar
    total = cuenta + propina

    #Calcular cuanto debe pagar cada persona si se divien entre varios
    pago_por_persona = total / persona

    return propina, total, pago_por_persona
#Solicitar al usuario la cuenta y el porcentaje de la propina
cuenta = float(input("Ingresar el total de la cuenta: "))
porcentaje_propina = float(input("Ingresar el porcentaje de la propina: "))
persona = int(input("¿Cuantas personas van a paga? "))

#Calcular la propina y el total
propina, total, pago_por_persona = calcular_propina(cuenta, porcentaje_propina, persona)

#Mostrar los resultados
print(f"\nPropina: {propina:.2f}")
print(f"Total a pagar: {total:.2f}")
print(f"Cada persona debe pagar: {pago_por_persona:.2f}")


#Día 31/365
#Calcular la media de una lista de números

def calcular_media(lista):
    return sum(lista)/ len (lista)

numeros = list(map(float, input("Ingresa una lista de números separado por espacios: ").split()))
print(f"La media es: {calcular_media(numeros)}")


#Día 32/365
"""
Encontrar el número más grande y 
el más pequeño de una lista
"""
#Pedir al usuario que ingrese una lista de números 
numeros = list(map(int , input("Ingresa una lista de número separados por espacios: ").split()))

#Paso 2: Encontrar el número más grande
maximo = max(numeros)

#Paso 3: Encontrar el número más pequeño
minimo = min(numeros)

#Paso 4: Mostrar los resultasdos
print(f"El número más grande es: {maximo}")
print(f"El número más pequeño es: {minimo}")


#Día 33/365
#Programa que simule el lanzamiento de una moneda

import random

def lanzar_moneda():
    return random.choice(["Cara", "Cruz"])
input("Presiona Enter para lanzar la moneda...")
print(f"La moneda cayó en: {lanzar_moneda()}")


#Día 34/365
#Programa que verifica si una palabra es un palíndromo.

def es_palindromo(palabra):
    palabra = palabra.lower() #Convertimos a minuscula par evitar errores
    return palabra == palabra[::-1] #Comparamos con su versión invertida

palabra = input("Ingresa una palabra: ")

if es_palindromo(palabra):
    print("Es un palíndromo!")

else:
    print("No es un palíndormo.")


#Día 35/365
""""
 Programa que cuenta cuántas
    Palabras tiene una frase
 """
def contar_palabra(frase):
    return len(frase.split()) #Dividimos la frase en palabras y contamos la cantidad

frase = input("Ingresa una frase: ")
print(f"La frase tiene {contar_palabra(frase)} palabras.")
