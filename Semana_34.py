#Día 232 / 365
"""
Generador de secuencia alternada par/impar
"""
def generar_secuencia(n):
    secuencia = []
    for i in range(1, n + 1):
        secuencia.append(i)
    return secuencia

n = int(input("Ingresa un número: "))
resultado = generar_secuencia(n)
print("Secuencia generada:", ",".join(map(str, resultado)))


#Día 233 / 365
"""
Diccionario con valores de las letras
"""
valores = {
    1: "AEIOULNSTR",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    6: "JX",
    10: "QZ"
}

puntos = {}
for valor, letras in valores.items():
    for letra in letras:
        puntos[letra] = valor

palabra = input("Ingresa una palabra: ").upper()

total = 0
for letra in palabra:
    if letra in puntos:
        total += puntos[letra]

print(f"El puntaje de la palabra '{palabra}' es: {total}")



#Día 234 / 365
"""
Programa que convierte un número (1-7) en día de la semana
"""
dias = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sabado",
    7: "Domingo"
}

numero = int(input("Ingresa un número del 1 al 7: "))

if 1 <= numero <= 7:
    print(f"El día es: {dias[numero]}")
else:
    print("Número fuera de rango")



#Día 235 / 365
"""
Compresor de texto con el algoritmo de Huffman
"""
import heapq
from collections import defaultdict

class Nodo:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.izq = None
        self.der = None
    def __lt__(self, otro):
        return self.freq < otro.freq


def construir_abol(freqs):
    heap = [Nodo(c, f) for c, f in freqs.items()]
    heapq.heapify(heap)
        
    while len(heap) > 1:
        izq = heapq.heappop(heap)
        der = heapq.heappop(heap)
        nodo = Nodo(None, izq.freq + der.freq)
        nodo.izq, nodo.der = izq, der
        heapq.heappush(heap, nodo)

    return heap[0]

def generar_codigos(nodo, prefijo="", codigos={}):
    if nodo is None:
        return
    if nodo.char is not None:
        codigos[nodo.char] = prefijo
    generar_codigos(nodo.izq, prefijo + "0", codigos)
    generar_codigos(nodo.der, prefijo + "1", codigos)
    return codigos

texto = "Compresor de texto con el algoritmo de Huffman"

freqs = defaultdict(int)
for c in texto:
    freqs[c] += 1

raiz = construir_abol(freqs)
codigos = generar_codigos(raiz)

codificado = "".join(codigos[c] for c in texto)

print("Codigos Huffman: ", codigos)
print("Texto original:", texto)
print("Codificado:", codificado)


#Día 236 / 365
"""
Resolver el problema del Sudoku con Backtracking
"""
def mostrar(tablero):
    for i in range(9):
        fila = ""
        for j in range(9):
            fila += str(tablero[i][j]) + " "
        print(fila)

def es_valido(tablero, fila, col, num):
    if num in tablero[fila]:
        return False
    
    for i in range(9):
        if tablero[i][col] == num:
            return False
    
    inicio_fila = (fila // 3) * 3
    inicio_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if tablero[inicio_fila+i][inicio_col+j] == num:
                return False
    return True

def resolver(tablero):
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:
                for num in range(1, 10):
                    if es_valido(tablero, i, j, num):
                        tablero[i][j] = num
                        if resolver(tablero):
                            return True
                        tablero[i][j] = 0
                return False       
    return True

#Ejemplo de Sudoku (0 = vació)

sudoku = [    
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

print("Sudoku inicial: ")
mostrar(sudoku)

if resolver(sudoku):
    print("\nSudoku resuelto:")
    mostrar(sudoku)

else:
    print("No tiene solución")



#Día 237 / 365
"""
Limpieza y análisis de datos de ventas en CSV
"""
import pandas as pd
from io import StringIO

#Simulamos un archivo CSV con errores típicos
data = """
Fecha,Cliente,Producto,Cantidad,Precio
2025-08-01,Juan,Laptop,1,1200
2025-08-02,Ana,Mouse,2,15
2025-08-03,Pedro,Teclado,1,40
2025-08-04,Ana,Laptop,1,1200
2025-08-04,,Monitor,1,300
2025-08-05,Juan,Mouse,2,15
2025-08-05,Juan,Mouse,2,15
2025-08-06,Camila,Laptop,1,1200
,Pedro,Laptop,1,1200
"""
#Carga del CSV simulado
df = pd.read_csv(StringIO(data))

print("=== Datos Originales ===")
print(df)

#Elimina filas vacías
df.dropna(inplace=True)

#Elimina duplicados
df.drop_duplicates(inplace=True)

#Convertir tipos de datos
df["Fecha"] = pd.to_datetime(df["Fecha"])
df["Precio"] = df["Precio"].astype(float)
df["Cantidad"] = df["Cantidad"].astype(int)

#Calcular ventas totales
df["Ventas_Totales"] = df["Cantidad"] * df["Precio"]

ventas_totales = df["Ventas_Totales"].sum()
producto_mas_vendido = df.groupby("Producto")["Cantidad"].sum().idxmax()
promedio_por_cliente = df.groupby("Cliente")["Ventas_Totales"].mean()

#Ranking de productos más vendidos
ranking_productos = df.groupby("Producto")["Cantidad"].sum().sort_values(ascending=False)

print("\n=== Datos Limpios ===")
print(df)

print("\n=== Métrica Clave ===")
print(f"Total de Ventas: ${ventas_totales}")
print(f"Productos más vendidos: {producto_mas_vendido}")
print("\nPromedio de ventas por cliente:")
print(promedio_por_cliente)

print("\n=== Promedio de Productos más Vendidos ===")
print(ranking_productos)


#Día 238 / 365
"""
Análisis de texto con frecuencia de palabras y graficado
"""
import matplotlib.pyplot as plt
import re
from collections import Counter

#Texto de ejemplo
texto = """
Python es un lenguaje poderoso. Python se usa en ciencia de datos, 
inteligencia artificial, automatización y mucho más. Aprender Python abre puertas.
"""

#Preprocesamiento: quitar caracteres raros y pasar a minusculas
palabras = re.findall(r'\b\w+\b', texto.lower())

#Contamos frecuencia de palabras
conteo = Counter(palabras)

#Contamos los 5 más comunes
mas_comunes = conteo.most_common(5)
palabras_top, frecuencias = zip(*mas_comunes)

#Mostrar en consola
print("Frecuencia de palabra más comunes:")
for palabra, freq in mas_comunes:
    print(f"{palabra}: {freq}")

#Graficar
plt.bar(palabras_top, frecuencias)
plt.title("Palabras más frecuentes")
plt.xlabel("Palabra")
plt.ylabel("Frecuencia")
plt.show()
