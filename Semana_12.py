#Día 78/365
"""
Matriz Transpuesta
"""

def transponer_matriz(matriz):
    #Obtener el número de filas y columnas de la matriz original
    filas = len(matriz)
    columnas = len(matriz[0])

    #Crear una matriz vacia para la transpusta
    transpuesta = [[0] * filas for _ in range (columnas)]

    #Llenar la matriz transpuesta
    for i in range(filas):
        for j in range(columnas):
            transpuesta[j][i] = matriz[i][j]
    return transpuesta

#Ejemplo de uso 
matriz_original = [
    [1, 2, 3],
    [4, 5, 6]
]

matriz_transpuesta = transponer_matriz(matriz_original)
print("Matriz Transpuesta:")
for fila in matriz_transpuesta:
    print(fila)


#Día 78/365
"""
Cálculo de Área de Polígonos
"""
def calcular_area_poligono(vertices):
    n = len(vertices)
    area = 0

    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2
        area -= y1 * y2

    area = abs(area) / 2.0
    return area

#Ejemplo de uso
vertices = [
    (1, 0),
    (4, 0),
    (4, 3),
    (1, 3)
]

area = calcular_area_poligono(vertices)
print(f"El área del poligono es: {area}")


#Día 80/365
"""
Calcular el MCD
"""

def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#ejmplo de iso 
numero1 = 56
numero2 = 98
resultado = mcd(numero1, numero2)
print(resultado)


#Día 81/365
"""
vResolver Ecuaciones Cuadráticas
"""
import math

def resolver_ecuacion_cuadratica(a, b, c):
    # Calcular el discriminante
    discriminante = b**2 - 4*a*c

    # Verificar el valor del discriminante
    if discriminante > 0:
        # Dos soluciones reales distintas
        solucion1 = (-b + math.sqrt(discriminante)) / (2*a)
        solucion2 = (-b - math.sqrt(discriminante)) / (2*a)
        return (solucion1, solucion2)
    elif discriminante == 0:
        # Una solución real (raíz doble)
        solucion = -b / (2*a)
        return (solucion,)
    else:
        # Dos soluciones complejas conjugadas
        parte_real = -b / (2*a)
        parte_imaginaria = math.sqrt(abs(discriminante)) / (2*a)
        solucion1 = complex(parte_real, parte_imaginaria)
        solucion2 = complex(parte_real, -parte_imaginaria)
        return (solucion1, solucion2)

# Ejemplo de uso
a = 1
b = -3
c = 2
soluciones = resolver_ecuacion_cuadratica(a, b, c)
print("Soluciones:", soluciones)



#Día 82/365
"""
Cifrado RSA Básico
"""
import random

def generar_primos_grandes(bits):
    while True:
        num = random.getrandbits(bits)
        if es_primo(num):
            return num
def es_primo(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num %2 == 0 or num % 3 == 0:
        return False
    
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generar_claves(bits = 8):
    p = generar_primos_grandes(bits)
    q = generar_primos_grandes(bits)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = random.randrange(2, phi_n)
    while mcd(e, phi_n) != 1:
        e = random.randrange(2, phi_n)
    d = inverso_modular(e, phi_n)
    return (e, n), (d, n)

def mcd(a,b):
    while b:
        a, b = b, a % b
    return a

def inverso_modular(e, phi):
    for d in range(2, phi):
        if(d * e) % phi == 1:
            return d
    return None
def cifrar(mensaje, clave_publica):
    e, n = clave_publica
    return [pow(ord(char), e, n) for char in mensaje]

def descifrar(mensaje_cifrado, clave_privada):
    d, n = clave_privada
    return " ".join([chr(pow(char, d, n)) for char in mensaje_cifrado])
#Ejemplo de uso
clave_publica, clave_privada = generar_claves()
mensaje = "Hola"
mensaje_cifrado = cifrar(mensaje, clave_privada)
mensaje_descifrada = descifrar(mensaje_cifrado, clave_privada)

print(f"Mensaje original: {mensaje}")
print(f"Mensaje cifrado: {mensaje_cifrado}")
print(f"Mensaje descifrado: {mensaje_descifrada}")


#Día 83/365
"""
Generador de Números Primos Gemelos
"""
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
        
    return True

def primos_gemelos(n):
    primos_gemelos = []
    for i in range(2, n):
        if es_primo(i) and es_primo(i + 2):
            primos_gemelos.append((i, i + 2))
    return primos_gemelos

#Ejmplo de uso
n = 20
pares_primos_gemelos = primos_gemelos(n)
print(pares_primos_gemelos)


#Día 84/365
"""
Cálculo de Área bajo una Curva
"""
def area_bajo_curva(f, a, b, n):
    """
    Calcula el área bajo la curva de la función f en el intervalo [a, b] usando la regla del trapecio.

    :param f: Función matemática que define la curva.
    :param a: Límite inferior del intervalo.
    :param b: Límite superior del intervalo.
    :param n: Número de subintervalos.
    :return: Aproximación del área bajo la curva.
    """
    # Tamaño de cada subintervalo
    h = (b - a) / n

    # Calcular la suma de las áreas de los trapecios
    area = 0.5 * (f(a) + f(b))  # Primer y último término
    for i in range(1, n):
        k = a + i * h
        area += f(k)

    area *= h
    return area

# Ejemplo de uso
# Definimos una función de ejemplo, por ejemplo, f(x) = x^2
def f(x):
    return x ** 2

# Intervalo [a, b]
a = 0
b = 2

# Número de subintervalos
n = 100

# Calcular el área bajo la curva
area = area_bajo_curva(f, a, b, n)
print(f"El área bajo la curva es aproximadamente: {area}")

