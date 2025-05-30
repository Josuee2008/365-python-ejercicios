#Día 15/365
#Crear una lista de tus colores favoritos

colores = ["Amarillo", "Verde", "Azul", "Naranja"]

#Imprimir la lista

print(f"Mis colores favoritos son: {colores}")


#Día 16/365
#Ordena una lista de números de forma ascendente

#Lista de números desordenados

numeros = [56,3,67,8,21,14,10,16]

#Ordenar la lista

numeros.sort()

#imprimir la lista ordenada

print(f"La lista de números en orden: {numeros}")


#Día 17/365
#Cuantas vecez aparece una letra 
#Cadena de texto 
cadena = "Esta es una cadena de un ejemplo para contar letras"

#Letra a contar 
letra = "e"

#contar laletra en la cadena
cantidad = cadena.count(letra)

#Imprimir el resultado 
print(f"La letra {letra}, aparece {cantidad} veces en la cadena.")


#Día 18/365
#Invierte una cadena de texto 
#Cadena de texto 
cadena = "Python es increíble"

#Invertir la cadena
cadena_invertida = cadena[::-1]

#Imprimir la cadena invertida
print(f"Cadena original:{cadena}")
print(f"Cadena invertida: {cadena_invertida}")


#Día 19
#Cuantas palabras tiene 3 letras, en una lista
#Lista de palabras
palabras = ["sol", "Casa", "perro", "luz", "mar", "gato"]

#Filtrar palabras con exactamente 3 letras
tres_letras = [palabra for palabra in palabras if len(palabra) == 3]

#Imprimir el resultado 
print(f"hay {len(tres_letras)} palabras con exactamente 3 letras.")


#Día 20/365
#Elimina los duplicados de una lista
#Lista con duplicados
numeros = [1,2,2,3,4,4,5]

#Eliminar duplicados 
sin_duplicados = list(set(numeros))

#Imprimir resultado 
print(f"Lista sin duplicados: {sin_duplicados}")


#Día 21/365
""""
Creamos una matriz como lista de listas y
Realizamos operaciones básicas, como acceder a elementos
y sumar filas.

"""
#Crear una matriz 3x3
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#Acceder al elemento de la fila 1, columna 2
elemento = matriz[0][1]

#Sumar los elementos de la primera fila 
suma_fila = sum(matriz[0])

#Imprimir resultado 
print(f"Elemento en la fila 1, columna 2: {elemento}")
print(f"Suma de los elementos de la primera fila: {suma_fila}")
