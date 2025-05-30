#Día 36/365
"""
Programa que genera un número aleatorio entre 
    1 y 100 y le pide al usuario adivinarlo.
"""
import random
def adivina_numero():
    numero_aleatorio = random.randint(1, 100)
    intento = None
    intentos = 0

    print("Bienvenido al juego de adivinar un número entre 1 y 1000")

    while intentos != numero_aleatorio:
        intento = int(input("Ingresa tu intento: "))
        intentos += 1

        if intento < numero_aleatorio:
            print("El número es mayor, intenta de nuevo. ")
        elif intento > numero_aleatorio:
            print("El número es menor, intenta de nuevo.")
        else:
            print(f"Felicidades, adivinaste el npumero en {intentos} intentos.")
        
adivina_numero()


#Día 37/365
"""
 Programa que calcula el total a 
    pagar en una tienda después de aplicar un descuento.
"""
def calcular_descuento(precio, descuento):
    precio_final = precio - (precio * descuento / 100)
    return precio_final

precio_original = float(input("Ingresa el precio original del producto: "))
descuento = float(input("Ingresa el porcentaje de descuento: "))

precio_con_descuento = calcular_descuento(precio_original, descuento)
print(f"El precio final después del descuento es: ${precio_con_descuento:.2f}")


#Día 38/365
"""
Programa que convierte una oración en "código Morse"
"""
#Diccionario con el alfabeto en código Morse
morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': ' / ' #Espacios entre palabras
}

def texto_a_morse(texto):
    texto = texto.upper() #Convertimos a mayúsculas para que coincida con el diccionario
    morse = " ".join(morse_dict[letra] for letra in texto if letra in morse_dict)
    return morse

#Pedir al usuario una oración 
texto = input("Ingresa un texto: ")
codigo_morse = texto_a_morse(texto)

#Mostrar la traducción en Morse
print(f"Código Morse: {codigo_morse}")


#Día 39/365
"""
Pograma que cuenta cuántas 
veces aparece cada palabra en un texto.
"""
def contar_palabras(texto):
    palabras = texto.lower().split()  # Convertimos a minúsculas y dividimos en palabras
    frecuencia = {}  # Diccionario para almacenar la frecuencia de cada palabra

    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1  # Contamos cada palabra

    return frecuencia

# Pedir al usuario un texto
texto = input("Ingresa un texto: ")
frecuencia_palabras = contar_palabras(texto)

# Mostrar el resultado ordenado
print("\nFrecuencia de palabras:")
for palabra, cantidad in sorted(frecuencia_palabras.items()):
    print(f"{palabra} -> {cantidad}")


#Día 40/365
"""
Simulador de lanzamiento de monedas para 
contar cuántas veces sale cara o cruz
en una serie de lanzamientos.
"""
import random
def lanzar_moneda(cantidad):
    resultados = {"Cara": 0, "Cruz": 0 }

    for _ in range(cantidad):
        lanzamiento = random.choice(["Cara", "Cruz"])
        resultados[lanzamiento] += 1

    return resultados

#Pedimos al usuario cuántas veces lanza la moneda
cantidad = int(input("¿Cuántas veces quieres lanzar la moneda? "))
resultados = lanzar_moneda(cantidad)

#Mostrar los resultados
print("\nResultados: ")
print(f"Cara: {resultados["Cara"]} veces")
print(f"Cruz: {resultados["Cruz"]} veces")


#Día 41/365
"""
Creamos un verificador de contraseñas seguras 
 que analiza qué tan fuerte
 es una contraseña según su longitud 
 y los tipos de caracteres que contiene.
"""

import re

def evaluar_contraseña(contraseña):
    if len(contraseña):
        return "Débil"
    elif len(contraseña) >= 6 and re.search(r"[a-zA-Z]", contraseña) and re.search(r"\d", contraseña):
        if len(contraseña) > 8 and re.search(r'[!@#$%^&*(),.?":{}|<>]', contraseña):
            return "Fuerte"
        else:
            return "Media"
    else:
        return "Débil"
    
#pedirle al usuario que ingrese una contraseña
contraseña = input("Ingresa tu contraseña: ")
seguridad = evaluar_contraseña(contraseña)

#Mostramos el resultado
print(f"Seguridad: {seguridad}")


#Día 42/365
"""
Programa que simule el cambio de luces 
de un semáforo (rojo, amarillo y verde).
"""
import time

def semaforo():
    while True:
        print("🔴 ROJO - Detente")
        time.sleep(3) #Esperar 3 segundos

        print("🟡 AMARILLO - Precaución")
        time.sleep(2) #Esperamos 2 segundos

        print("🟢 VERDE - Avanzar")
        time.sleep(3) #Esperar 3 segundos

#Llamar a la función para la iniciar el semáforo
semaforo()
