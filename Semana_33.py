# Día 225 / 365
"""
Simulador de Carrera de Números 🏁
"""
import random
import time
import os
#Configuración 
meta = 50
pos1 = 0
pos2 = 0

while pos1 < meta and pos2 < meta:
    os.system("cls" if os.name == "nt" else "clear")

    pos1 += random.randint(1, 3)
    pos2 += random.randint(1, 3)

    print(f"Corredor 1: {'█' * pos1}")
    print(f"Corredor 2: {'█' * pos2}")

    time.sleep(0.3)

if pos1 >= meta and pos2 >= meta:
    print("\n🏆 ¡Empate!")
elif pos1 >= meta:
    print("\n🏆 ¡Corredor 1 gana!")
else:
    print("\n🏆 ¡Corredor 2 gana!")



#Día 226 / 365
"""
Detector de palabras más largas en un texto
"""
texto = input("Escribe una frase o párrafo: ")

for simbolo in ",.;:¡!¿?":
    texto = texto.replace(simbolo, "")

palabra = texto.split()

max_len = max(len(p) for p in palabra)

mas_largas = [p for p in palabra if len(p) == max_len]

print(f"\nLonguitud máxima: {max_len} letras")
print("Palabras(s) más larga(s): ", ", ".join(set(mas_largas)))



#Día 227 / 365
"""
Contador de vocales y consonantes en un texto 🔤
"""
def contador_vocales_consonantes(texto):
    texto = texto.lower()
    vocales = 'aeiou'
    num_vocales = 0
    num_consonantes = 0
    conteo_vocales = {}

    for letras in texto:
        if letras.isalpha():
            if letras in vocales:
                num_vocales += 1
                conteo_vocales[letras] = conteo_vocales.get(letras, 0) + 1
            else:
                num_consonantes += 1

    print(f"Vocales: {num_vocales}")
    print(f"Consonantes: {num_consonantes}")

    if conteo_vocales:
        mas_frecuentes = max(conteo_vocales, key=conteo_vocales.get)
        print(f"La vocal más usada es '{mas_frecuentes}' con {conteo_vocales[mas_frecuentes]} apariciones.")

    else:
        print("No se encontro vocales.")
    
frase = input("Escibe una frase: ")
contador_vocales_consonantes(frase)



#Día 228 / 365
"""
Detector de Vocales Faltantes
"""
def detector_vocales_faltantes(texto):
    vocales = {"a", "e", "i", "o", "u"}
    texto = texto.lower()
    presentes = set([letra for letra in texto if letra in vocales])
    faltantes = vocales - presentes

    if faltantes:
        print(f"Faltan las vocales: {', '.join(sorted(faltantes))}")    
    else:
        print("¡Tiene todas las vocales!")

Frase = input("Ingresa una palabra o frase: ")
detector_vocales_faltantes(Frase)



# Día 229 / 365
"""
Detector de secuencias ascendentes en un número
"""
def detector_secuencias(numero):
    numero = str(numero)
    secuencia = numero[0]
    encontrado = False

    for i in range(1, len(numero)):
        if int(numero[i]) == int(numero[i - 1]) +1:
            secuencia += numero[i]

        else:
            if len(secuencia) > 1:
                print(f"Secuencia ascendente encontrasa: {secuencia}")
                encontrado = True
            secuencia = numero[i]
        
    if len(secuencia) > 1:
        print(f"Secuencia ascendente encontrada: {secuencia}")
        encontrado = True
    if not encontrado:
        print("No contiene secuencias ascendentes.")


numero = input("Ingresa un número: ")
detector_secuencias(numero)



#Día 230 / 365
"""
Detector de números espejo
"""
def es_numero_espejo(numero):
    espejo = {"0": "0", "1": "1", "8":"8", "6": "9", "9": "6"}

    num_str = str(numero)

    reflejo = ""
    for digitos in reversed(num_str):
        if digitos in espejo:
            reflejo += espejo[digitos]
        else:
            return False
        
    return reflejo == num_str

num = input("Ingresa un número: ")
if es_numero_espejo(num):
    print(f"Sí, {num} es un número espejo.")
else:
    print(f"No, {num} no es un número espejo.")


#Día 231 / 365
"""
Compresor RLE (Run-Length Encoding) simple
"""
def comprimir(cadena):
    if not cadena:
        return ""
    
    resultado = ""
    contador = 1

    for i in range(1, len(cadena)):
        if cadena[i] == cadena[i - 1]:
            contador += 1

        else:
            resultado += cadena[i - 1] + str(contador)
            contador = 1

    
    resultado += cadena[-1] + str(contador)
    return resultado


def descomprimir(cadena):
    resultado = ""
    i = 0

    while i < len(cadena):
        letra = cadena[i]
        i += 1
        numero = ""

        while i < len(cadena) and cadena[i].isdigit():
            numero += cadena[i]
            i += 1

        resultado += letra * int(numero)

    return resultado

texto = input("Ingresa una cadena: ")

comprimido = comprimir(texto)
print("Comprimido:", comprimido)

descomprimido = descomprimir(comprimido)
print("Descomprimido:", descomprimido)
