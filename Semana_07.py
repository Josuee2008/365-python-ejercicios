#Día 43/365
"""
Programa que convierte la edad de una persona en días.
"""
def edad_en_dias(edad):
    return edad * 365 #Aproximamos sin contar años bisiestos

#Pedir la edad al usuario
edad = int(input("Ingresar tu edad en años: "))

#Calcular y mostrar el resultado
print(f"HAs vivido aproximadamente: {edad_en_dias(edad)}")


#Día 44/365
"""
Generador de nombres y apellidos
aleatorios
"""

import random

#Lista de nombres y apellidos
nombres = ["Carlos", "Ana", "Luis", "Sofía", "Diego", "María", "Fernando", "Elena"]
apellidos = ["García", "Pérez", "Rodríguez", "López", "Fernández", "Martínez", "Gómez", "Díaz"]

#Generar un nombre aleatorio
nombre_completo = random.choice(nombres) + " " + random.choice(apellidos)

#Mostrar el resultado
print(f"Nombre generado: {nombre_completo}")


#Día 45/365
"""
 Programa que genere un mensaje
   romántico personalizado.
"""
import random

def generar_mensaje(nombre):
    frase = [
         f"{nombre}, eres la razón por la que sonrío cada día. ❤️",
        f"Cada momento contigo, {nombre}, es un regalo que atesoro. 💖",
        f"{nombre}, si el amor tuviera un nombre, llevaría el tuyo. 💕",
        f"No hay palabras suficientes para decir cuánto te quiero, {nombre}. 😍",
        f"{nombre}, mi mundo es más bonito desde que estás en él. 🌹"

    ]
    return random.choice(frase)
#Pedir el nombre de la persona especial
nombre = input("Ingresar el nombre de la persona especial: ")
print("\n💌 Mensaje especial para San Valentín: 💌")
print(generar_mensaje(nombre))


#Día 46/365
"""
Adivina la palabra oculta 
"""

import random
#Lista de palabras posibles
palabras = ["python", "programa", "computadora", "teclado", "mause"]

#Seleccionar una palabra
palabra_secreta = random.choice(palabras)
palabra_oculta = ["_"] * len(palabra_secreta)
intentos = 7

print("¡Adivina la palabra secreta!")
print(" ".join(palabra_oculta))

while "_" in palabra_oculta and intentos > 0:
    letra = input("\nIngresa una letra: ").lower()

    if letra in palabra_secreta:
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] == letra:
                palabra_oculta[i] = letra
    else:
        intentos -= 1
        print(f"Letra incorrecta. Te queda {intentos}")
    print(" ".join(palabra_oculta))

#Resultado final
if "_" not in palabra_oculta:
    print("\n¡Felicidades! Adivinaste la palabra")
else:
    print(f"\nPerdiste. La palabra era: {palabra_secreta}")


#Día 47/365
"""
Conversor de tiempo
"""
# Pedir al usuario la cantidad de minutos
minutos = int(input("Ingresa la cantidad de minutos: "))

#Convertir a horas y minutos
hora = minutos // 60 #División entera para obtener las horas
min_restante = minutos % 60 #Módulo para obtener los minutos restantes

#Mostrar el resultado
print(F"{minutos} minutos son {hora} horas y {min_restante} minutos.")


#Día 48/365
"""
Conversor de Unidades de Longitud 📏
"""
#Pedir al usuario una cantidad en metros
metros = float(input("Ingresar una cantidad en metros: "))

#convertir a otras unidades
kilometros = metros / 1000
centimetros = metros * 100
milimetros = metros * 1000

#Mostrar resultados
print(f"{metros} metros equivalen a: ")
print(f"{centimetros} centímetros")
print(f"{kilometros} Kilometros")
print(f"{milimetros} Milímetros")


#Día 49/365
"""
Contador de Dígitos en un Número 🔢
"""
#Pedir un número al usuario
numero = input("Ingrese un número: ")

#Contar cuántos dígitos tiene
cantidad_digitos = len(numero)

#Mostrar el resultado
print(f" 🔢 El número {numero} tiene {cantidad_digitos} digitos.")
