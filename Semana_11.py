#Día 71/365
"""
Contar la frecuencia de 
cada letra en una cadena de texto
"""
def frecuencia_letras(cadena):
    frecuencia = {}
    for letra in cadena.lower():
        if letra.isalpha():
            frecuencia[letra] = frecuencia.get(letra, 0) + 1
    return frecuencia

#Ejemplo de uso 
texto = "Pythhon es increíble"
print(frecuencia_letras(texto))


#Día 72/365
"""
Verificar si dos 
palabras son anagramas
"""
def es_anagrama(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())
#Ejemplo de uso 
print(es_anagrama("amor", "roma"))
print(es_anagrama("python", "typhon"))
print(es_anagrama("hola", "mundo"))


#Día 73/365
""""
Generar todos los subconjuntos 
de una lista usando recursión
"""

def subconjuntos(lista):
    if not lista:
        return[[]]
    
    elemento = lista[0]
    subconjuntos_sin_elemento = subconjuntos(lista[1:])
    subconjuntos_con_elementos = [subconjunto + [elemento] for subconjunto in subconjuntos_sin_elemento]
    return subconjuntos_sin_elemento + subconjuntos_con_elementos

#Ejemplo de uso
lista = [1, 2, 3]
print(subconjuntos(lista))


#Día 74/365
"""
Búsqueda Binaria
"""

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) -1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor_medio = lista[medio]

        if valor_medio == objetivo:
            return medio #Ejemplo encotrado
        elif valor_medio < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio -1
    
    return -1

#Ejemplo de uso 
lista_ordenada = [1, 2, 3, 5, 8, 12, 15]
objetivo = 8
indice = busqueda_binaria(lista_ordenada, objetivo)

if indice != -1:
    print(f"El elemento {objetivo} se encuentra en el índice {indice}")
else:
    print(f"El elemento {objetivo}, no se encuatra en la lista.") 


#Día 75/365
"""
Conversión de Bases Numéricas
"""
def conversion_bases(numero):
    binario = bin(numero)[2:] #Convertir a binario y eliminar "0b"
    ocatl = oct(numero)[2:] #Convertir a octal y eliminar "0o"
    hexadecimal = hex(numero)[2:] #Convertir a hexadecimal y eliminar "0x"

    return f"Binario: {binario}, Octal: {ocatl}, Hexadecimal: {hexadecimal}"

#ejemplo de uso 
numero = int(input("Ingresa un número decimal: "))
print(conversion_bases(numero))


#Día 76/365
"""
Árbol de Decisiones Simple
"""

def decidir_actividad(clima):
    if clima == "soleado":
        return "Puedes ir a la playa o hacer una caminata."
    elif clima == "nublado":
        return "Puedes ir al cine o leer un libro en casa."
    elif clima == "lluvioso":
        return "Puedes quedarte en casa viendo una pelicula o ir a un museo."
    else:
        return "Clima no reconocido. Por favor, elige entre 'soleado', 'nublado', 'lluvioso'."

#Ejemplo de uso
clima_actual = "soleado"
actividad_sugerida = decidir_actividad(clima_actual)
print(actividad_sugerida)


#Día 77/365
"""
Cálculo de Factorial con Recursión
"""
def factorial(n):
    #Caso base: 0! = 1
    if n == 0:
        return 1
    else:
        # Llamada recursiva
        return n * factorial(n - 1)
    
#Ejemplo de uso 
numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")
