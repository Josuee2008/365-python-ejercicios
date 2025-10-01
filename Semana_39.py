# Día 267 / 365
# Organizador automático de fotos por año y mes

import os, shutil
from datetime import datetime

EXTS = (".jpg", ".jpeg", ".png", ".gif", ".heic", ".bmp", ".tiff", ".webp")

def organizar(origen, destino=None):
    if not destino: destino = origen
    for f in os.listdir(origen):
        ruta = os.path.join(origen, f)
        if os.path.isfile(ruta) and f.lower().endswith(EXTS):
            fecha = datetime.fromtimestamp(os.path.getmtime(ruta))
            carpeta = os.path.join(destino, fecha.strftime("%Y"), fecha.strftime("%m"))
            os.makedirs(carpeta, exist_ok=True)
            base, ext = os.path.splitext(f)
            nuevo = os.path.join(carpeta, f)
            i = 1

            while os.path.exists(nuevo):
                nuevo = os.path.join(carpeta, f"{base}_{i}{ext}")
                i += 1
            shutil.move(ruta, nuevo)
            print(f"Mover: {ruta} -> {nuevo}")

if __name__ == "__main__":
    origen = input("Carpeta con fotos: ").strip()
    destino = input("Carpeta destino (enter = misma): ").strip() or None
    organizar(origen, destino)
    print("Organización completa.")


#Día 268 / 365
#mini-backups automáticos 🚀

import os 
import shutil
from datetime import datetime

origen = input("Ingresa la ruta de la carpeta de origen: ")
destino = input("Ingresa la ruta de la carpeta de respaldo: ")

if not os.path.exists(destino):
    os.makedirs(destino)

fecha_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

contador = 0

for archivo in os.listdir(origen):
    ruta_archivo = os.path.join(origen, archivo)

    if os.path.isfile(ruta_archivo):
        nombre, extension = os.path.splitext(archivo)
        nuevo_nombre = f"{nombre}_{fecha_hora}{extension}"
        ruta_nueva = os.path.join(destino, nuevo_nombre)

        shutil.copy2(ruta_archivo, ruta_nueva)
        print(f"Archivo {archivo} → {nuevo_nombre}")
        contador += 1

print(f"\nBackup completado: {contador} archivos copiados en {destino}")


#Día 269 / 365
#Clasificador de sentimiento

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = [
    "Me encanta la película",
    "Fue una experiencia increíble",
    "Odié la película",
    "Qué aburrida y mala",
    "Estuvo más o menos"
]

labels = ["pos", "pos", "neg", "neg", "neu"]

vec = TfidfVectorizer()
X = vec.fit_transform(texts)
clf = MultinomialNB()
clf.fit(X, labels)

print("Clasificador listo. Escribe 'exit' para salir." )
while True:
    s = input("Reseña: ").strip()
    if s.lower() in ("exit", "salir", "quit", ""):
        break
    print("Predicción: ", clf.predict(vec.transform([s]))[0])


#Día 270 / 365
#Sistema de Gestión de Biblioteca

biblioteca = {}

while True:
    op = input("\nOpciones: 1.Agregar 2.Prestar 3.Ver 4.Salir\nElige: ").strip()
    
    if op=="1":
        t = input("Título: ").strip()
        c = int(input("Cantidad: "))
        biblioteca[t] = biblioteca.get(t,0) + c
        print(f"{t} agregado. Total: {biblioteca[t]}")

    elif op=="2":
        t = input("Libro a prestar: ").strip()
        if biblioteca.get(t,0)>0:
            biblioteca[t] -= 1
            print(f"{t} prestado. Quedan: {biblioteca[t]}")
        else:
            print("No disponible")

    elif op=="3":
        if not biblioteca:
            print("Biblioteca vacía")
        else:
            for t,c in biblioteca.items():
                print(f"{t}: {c} copias disponibles")

    elif op=="4":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")


# Día 271 / 365
# Conversor de divisas simple con API

import requests

url = "https://open.er-api.com/v6/latest/USD"
data = requests.get(url).json()
rates = data["rates"]

while True:
    monto  = input("MOnto en USD (o 'salir'): ")
    if monto.lower() in ("salir", "exit", ""):
        break
    monto = float(monto)
    moneda = input("Convertir a (EUR, MXN, COP, etc.): ").upper()    
    if moneda in rates:
        print(f"{monto} USD = {monto * rates[moneda]:.2f} {moneda}")
    else:
        print("Moneda no encontrada.")


# Día 272 / 365
"""
Programa que convierta una palabra
 en un patrón de estrellas.
"""
def marco_palabra(palabra):
    borde = "*" * (len(palabra) + 4)
    print(borde)
    print(f"* {palabra} *")
    print(borde)

palabra = input("Escribe una  palabra: ")
marco_palabra(palabra)


# Día 273 / 365
# Generador Sopa de Letras 
import random, string

N = 10

palabras = ["PYTHON", "JUEGO", "CODIGO"]

sopa = [[" " for _ in range(N)] for _ in range(N)]

for palabra in palabras:
    fila = random.randint(0, N-1)
    col = random.randint(0, N-len(palabra))
    for i, letra in enumerate(palabra):
        sopa[fila][col+i] =  letra

for f in range(N):
    for c in range(N):
        if sopa[f][c] == " ":
            sopa[f][c] = random.choice(string.ascii_uppercase)
    
print("\nSopa de Letras:\n")
for fila in sopa:
    print(" ".join(fila))

print("\nPalabras a buscar:")
for p in palabras:
    print("-", p)
