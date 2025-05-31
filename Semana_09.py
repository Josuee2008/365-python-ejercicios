#Día 57/365
"""
 Verificar si una cadena de texto es un pangrama.
"""

import string

def es_pangrama(frase):
    letras = set(frase.lower()) #convertir a minuscula y creamos un conjunto
    alfabeto = set(string.ascii_lowercase) #Conjunto de todas las letras del alfabeto
    return alfabeto.issubset(letras) #Verificar si el alfabeto esta en la frase

#Ejemplo de uso 
frase =  "Jovencillo emponzoñado de whisky, ¡qué figurota exhibes!"
print("¿Es un pangrama?", es_pangrama(frase))



#Día 58/365
"""
Extraer los dominios de correos electrónicos 📩
"""

def extraer_dominios(lista_emails):
    return [email.split("@")[1] for email in lista_emails] #Extraemos el dominio

#Ejemplo de uso 
emails = [
    "juan123@gmail.com",
    "ana_perez@hotmail.com",
    "dev_python@empresa.com",
    "carlos.ventas@yahoo.com",
    "maria_tech@proyectos.net",
    "luis_admin@corporativo.org",
    "soporte@midominio.com",
    "cliente.vip@servicio.io",
    "contacto@startup.dev",
    "empleos@trabajos.co",
    "notificaciones@redsocial.app",
    "ventas@tienda.shop",
    "user123@correo.edu",
    "editor@revista.news",
    "marketing@promos.biz",
    "gerencia@empresa.global"
]
print("Dominios encontrados", extraer_dominios(emails))


#Día 58/365
"""
Detectar números repetidos en una lista 🔢✅
"""

def contar_repetidos(lista_numeros):
    conteo = {} #Diccionario para contar ocurrencias

    for num in lista_numeros:
        if num in conteo:
            conteo[num] += 1
        else:
            conteo[num] = 1
    #Filtramos solo los números que se reiten
    repetidos = {num: count for num, count in conteo.items() if count > 1}
    return repetidos
#Ejemplo de uso 
numeros = [4, 2, 8, 4, 3, 2, 8, 8, 10, 2, 5, 4]
print("Números repetidos:", contar_repetidos(numeros))


#Día 60/365
"""
Convertir números a palabras 🔢➡️📝
"""
from num2words import num2words

def numero_a_palabra(numero):
    return num2words(numero, lang= "es") #Convertimos el número a palabra en español

#Ejemplo de uso 
numero = int(input("Ingresa un número: "))

print("En palabras: ", numero_a_palabra(numero))


#Día 61/365
"""
Detectar si un texto es un
 "email válido" 📧✅❌
"""

import re

def es_email_valido(email):
    patron = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$" #Expresión regualar para validar un email
    return "Email válido" if re.match(patron, email) else "Email inválido"

#Ejemplo de uso 
email = input("Ingresa tu email: ")
print(es_email_valido(email))


#Día 62/365
"""
Simular un temporizador 
de cuenta regresiva ⏳⏰
"""

import time

def cuenta_regresiva(segundos):
    while segundos > 0:
        print(f"{segundos} {'segundo' if segundos == 1 else 'segundos'} restantes...")
        time.sleep(1) #Esperar 1 segundo 

        segundos -= 1
    print("Tiempo terminado!")

#Ejemplo de uso 
segundos = int(input("Ingresar el tiempo en segundos: "))
cuenta_regresiva(segundos)


#Día 63/365
"""
Extraer automáticamente
 enlaces de un texto 🔗📜
"""

import re

def extraer_enlaces(texto):
    # Expresión regular para detectar URLs
    patron_url = r"https?://[^\s]+"
    
    # Buscamos las URLs en el texto
    enlaces = re.findall(patron_url, texto)
    
    # Mostramos los resultados
    if enlaces:
        print("Enlaces encontrados:")
        for enlace in enlaces:
            print("-", enlace)
    else:
        print("No se encontraron enlaces.")

# Ejemplo de uso
texto = input("Ingrese un texto: ")
extraer_enlaces(texto)
