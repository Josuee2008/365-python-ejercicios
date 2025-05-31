#Día 85
"""
Juego de Ruleta
"""

import random

def girar_ruleta():
    return random.randint(0, 36)

def determinar_resultado(apuesta, resultado):
    if apuesta == resultado:
        return "¡Felicidades! Haz ganado."
    else:
        return "Lo siento, has perdido. El número ganador es" + str(resultado) + "."
    
def jugar_ruleta():
    apuesta = int(input("Haz tu apuesta (número entre 0 y 36): "))

    resultado = girar_ruleta()

    mensaje = determinar_resultado(apuesta, resultado)

    print(mensaje)

#Ejecutar el juego
jugar_ruleta()


#Día 86/365
"""
Intersección de Listas
"""
def interseccion_listas(lista1, lista2):
    return list(set(lista1) & set(lista2))

#Ejemplo de uso
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

resultado = interseccion_listas(lista1, lista2)
print("Elemento en común: ", resultado)


#Día 87/365
"""
Rotación de Lista en Python 🚀🐍
"""

def rotar_lista(lista, pasos, direccion):
    if direccion == "derecha":
        return lista[-pasos:] + lista[:-pasos]
    elif direccion == "izquierda":
        return lista[pasos:] + lista[:pasos]
    else:
        return "Dirección inválida. Usa 'izquierda' o 'derecha'."

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5]
pasos = int(input("¿Cuántos pasos quieres rotar? "))
direccion = input("¿Hacia dónde? (izquierda/derecha): ").lower()

resultado = rotar_lista(numeros, pasos, direccion)
print(f"Lista rotada: {resultado}")


#Día 88/365
"""
Filtrar Números Pares e Impares
"""
def separar_pares_impares(lista):
    pares = [num for num in lista if num % 2 == 0]
    impares = [num for num in lista if num % 2 != 0]
    return pares, impares
#Lista de ejemplos
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Llamar a la función
pares, impares = separar_pares_impares(numeros)

#Mostrar reusltados
print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impares}")


#Día 89/365
"""
Extraer solo los números 
de una cadena de texto
"""
def extraer_numeros(texto):
    numeros = "".join(caracter for caracter in texto if caracter.isdigit())
    return numeros

#Ejemplo de uso 
texto = input("Ingresa un texto con números: ")
resultado = extraer_numeros(texto)
print("Números extraídos:", resultado)

#Día 90/365
"""
Calculadora de IMC en Python
"""
def calcular_imc(peso, altura):
    return peso/ (altura ** 2)

#Solicitar datos al usuario
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresar tu altura en metros: "))

#Calcular el IMC
imc = calcular_imc(peso, altura)
print("Tu IMC es:", round(imc, 2))

#Calificar el IMc
if imc < 18.5:
    print("Clasificación: Bajo peso")

elif imc < 25:
    print("Clasificación: Normal")

elif imc < 30:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")
    
#Día 92/365
"""
Convertir una lista 
en un diccionario con índices
"""
def lista_a_diccionario(lista):
    return{i: lista[i] for i in range (len(lista))}
#Ejemplo de uso
lista = ["Manzana", "Banana", "Cereza", "Durazno"]
diccionario = lista_a_diccionario(lista)
print(diccionario)
