#Día 22/365
#función que calcule el área de un triángulo
#Definir la función 
def area_triangula(base, altura):
    return(base * altura) / 2
#Solicitar datos al usuario 
base = float(input("Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))

#Calcular e imprimir el área
print(f"El área del triángulo es: {area_triangula(base, altura)}")


#Día 23/365
#Función que determine si un número es primo
#Definir la funcion 
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
#Solicitar un numero al usuario
numero = int(input("Ingresa un numero: "))

#Verificar e imprimir si es primo 
if es_primo(numero):
    print(f"{numero} es un numero primo.")
else:
    print(f"{numero} no es un numero primo.")


#Dia 24/365
#Función que genera una lista de números aleatorios.
import random

#Definir la función 
def generar_lista_aleatoria(tamano, inicio, fin):

    return[random.randint(inicio, fin) for _ in range(tamano)]

#Solicitar datos al usuario 
tamano = int(input("Cantidad de números en la lista"))
inicio = int(input("Valor mínimo: "))
fin = int(input("Valor máximo: "))

#Generar e imprimir la lista 
lista = generar_lista_aleatoria(tamano, inicio, fin)
print(f"Lista generada: {lista}")


#Día 25/365
"""
Función que reciba una lista 
y devuelva la suma de sus elementos
"""
#Difinir la función 
def suma_elemento(lista):
    return sum(lista)
#Solicitamos datos al usuario 
lista = list(map(int, input("Ingresar una lista de números separados por espacios: "). split()))

#Sumar e imprimir el resultado 
print(f"El resulatso de la suma de los números es: {suma_elemento(lista)}")


#Día 26/365
#Función que invertir una lista 
#Definir la función 
def invertir_lista(lista):
    return lista[::-1]

#Solicitar una lista al usuario
lista = list(map(int, input("Ingresar una lista de números separados por espacios: "). split()))

#Llamar a la función e imprimir el resultado 
print(f"Lista invertisa: {invertir_lista(lista)}")


#Día 27/365
""""
Función que combina dos listas y 
calcula la suma de sus elementos.
"""

#Definimos dos listas con números
lista_1 = [3,5,7,9]
lista_2 = [2, 4, 6, 8]

#Combinamos las listas usandi extend()
lista_combinada = lista_1.copy()
lista_combinada.extend(lista_2)

#Calcular la suma de los elementos de la lista combinada
suma = sum(lista_combinada)

#Mostrar el resultado
print(f"La lista combinada es: {lista_combinada}")
print(f"La suma de los elementos es: {suma}")


#Día 38/365
""""
 Programa que calcule la cantidad total 
 de vocales en una frase ingresada por el usuario.
 """

#Solicitar una frase al usuario
frase = input("Ingresar una frase: ")

#Definir las vocales
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"

#Contar las vocales de la frase
contar = sum(1 for letra in frase if letra in vocales)

#Mostrar el resultado 
print(f"La frase contiene {contar} vocales.")
