#Día  155 / 365
"""
Mostrar los días festivos de 
un país en un año específico
"""

import holidays

año = int(input("Ingresa un año (por ejemplo, 2025): "))

feriados = holidays.country_holidays('EC', years=año)

print(f"Días festivos en Ecuador para el año {año}: \n")
for fecha, nombre in sorted(feriados.items()):
    print(f"{fecha}: {nombre}")



#Día 156 / 365
"""
Calculadora de diferencia 
entre zonas horarias
"""
from datetime import datetime
import pytz


zona1= pytz.timezone('America/Mexico_City')
zona2 = pytz.timezone('Asia/Tokyo')

#Obtener hora actual en UTC
utc = datetime.now(pytz.utc)

hora1= utc.astimezone(zona1)
hora2 = utc.astimezone(zona2)

print(f"Hora en Ciudad de México: {hora1.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Hora en Tokio: {hora2.strftime('%Y-%m-%d %H:%M:%S')}")

diferencia = (hora2.utcoffset().total_seconds() - hora1.utcoffset().total_seconds()) / 3600
print(f"Diferencia horaria: {abs(diferencia)} horas")



#Día 157 / 365
"""
Cuenta cuántos caracteres especiales 
hay en una cadena de texto
"""

texto = input("Escribe una frase: ")

caracteres_especiales = "!@#$%^&*()_+-=[]{}|;:'\",.<>?/`~"

contador = 0

for caractere in texto:
    if caractere in caracteres_especiales:
        contador += 1

print(f"Caracteres especiales encontrados: {contador}")




#Día 158 / 365
"""
"Filtrador de Números Únicos"
"""
from collections import defaultdict

numeros = [int(num.strip()) for num in input("Ingresa números separados por comas: ").split(",")]
contador = defaultdict(int)

for num in numeros:
    contador[num] += 1

unicos = [num for num in numeros if contador[num] == 1]
print("Números únicos:", unicos)




# Día 159 / 365
"""
Verifica si un número es positivo, negativo o cero
"""

numero = int(input("Ingresa un número: "))

if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")


# Día 160 / 365
"""
Cuenta cuántas letras mayúsculas
y minúsculas hay en una frase
"""
frase = input("Escribe una frase:")
mayusculas = 0
minusculs = 0
for letras in frase:
    if letras.isupper0:
        mayusculas += 1
    elif letras.islower:
        minusculas += 1
print (f"Mayúsculas: (mayusculas)")
print(f"Minusculas: (minusculas)")

# Día 161 / 365
"""
Cuenta cuántas palabras en una frase
comienzan con una vocal
"""
frase = input ("Escribe una frase:")
palabras = frase.split()
vocales = 'aeiouáéíóúAEIOUÁÉÍÓÚ'
contador = 0
for palabra in palabras:
 if palabra and palabra[0] in vocales:
    contador += 1
print(f"Palabras que comienzan con vocal:{contador}")
