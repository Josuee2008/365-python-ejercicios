# Día 260 / 365
# Analizador de consumo de espacio en disco

import os
def obtener_tamano(ruta):
    total = 0
    for dirpath, _, filenames in os.walk(ruta):
        for f in filenames:
            try:
                fp = os.path.join(dirpath, f)
                total += os.path.getsize(fp)
            except:
                pass 
    return total

def analizar_especial(ruta):
    carpetas = {}
    for elemento in os.listdir(ruta):
        ruta_elemento = os.path.join(ruta, elemento)
        if os.path.isdir(ruta_elemento):
            carpetas[elemento] = obtener_tamano(ruta_elemento)
    return sorted(carpetas.items(), key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    ruta = input("Ingresa la ruta de la carpeta a analizar: ")
    print("\nAnalizando...")

    resultado = analizar_especial(ruta)

    print("Carpeta - Tamaño en MB")
    for carpeta, tamano in resultado:
        print(f"{carpeta} - {tamano / (1024*1024):.2f} MB")

#Día 261 / 365
"""
Limpieza de archivos temporales
"""

import os

def buscar_archivos_temporales(ruta, extensiones):
    encontrados = []
    total_size = 0
    for dirpath, _, filenames in os.walk(ruta):
        for f in filenames:
            if f.lower().endswith(tuple(extensiones)):
                fp = os.path.join(dirpath, f)
                try:
                    size = os.path.getsize(fp)
                    encontrados.append((fp, size))
                    total_size += size
                except:
                    pass
    return encontrados, total_size

if __name__ == "__main__":
    ruta = input("Ingresa la ruta de la carpeta a analizar: ")
    extensiones = [".tmp", ".log", ".bak"]

    print("\nBuscando archivos temporales...")
    archivos, total = buscar_archivos_temporales(ruta, extensiones)

    if not archivos:
        print("No se encontraron archivos temporales.")
    else:
        print(f"\nArchivos temporales encontrados: {len(archivos)}")
        print(f"Espcio total ocupado: {total / (1024*1024):.2f} MB")

        opcion = input("¿Quieres eliminarlos? (s/n): ").lower()
        if opcion == "s":
            liberado = 0
            for archivo, size in archivos:
                try:
                    os.remove(archivo)
                    liberado += size
                except:
                    pass
            
            print(f"\nLimpieza completa. Espacio liberado: {liberado / (1024*1024):.2f} MB")
        else:
            print("Limpieza cancelada.")


#Día 262 / 265
#Renombrador de fotos por fecha EXIF
import os
import shutil
from PIL import Image, ExifTags
from datetime import datetime

def obtener_fecha(ruta):
    try:
        img = Image.open(ruta)
        exif = img.getexif()
        for tag, val in exif.items():
            if ExifTags.TAGS.get(tag) in ("DateTimeOriginal", "DateTime"):
                return datetime.strptime(val, "%Y:%m:%d %H:%M:%S")
    except:
        return None
    
def procesar(carpeta):
    sin_fecha = os.path.join(carpeta, "sin_fecha")
    os.makedirs(sin_fecha, exist_ok=True)

    for archivo in os.listdir(carpeta):
        if archivo.lower().endswith((".jpg", ".jpeg")):
            ruta = os.path.join(carpeta, archivo)
            fecha = obtener_fecha(ruta)
            if fecha:
                nuevo = fecha.strftime("%Y-%m-%d_%H-%M-%S") + ".jpg"
                destino = os.path.join(carpeta, nuevo)
            else:
                destino = os.path.join(sin_fecha, archivo)
            contador = 1
            base, ext = os.path.splitext(destino)
            while os.path.exists(destino):
                destino = f"{base}_{contador}{ext}"
                contador += 1
            shutil.move(ruta, destino)

if __name__ == "__main__":
    carpeta = input("Ruta de la carpeta con fotos: ").strip()
    procesar(carpeta)
    print("Fotos organizados por fecha EXIF")


#Día 263 / 265
"""
Analizador de gastos personales 
a partir de un archivo CSV"""

import csv

archivo = "gastos.csv"

gastos_por_categoria = {}

with open(archivo, newline="", encoding="utf-8") as f:
    lector = csv.DictReader(f)
    for fila in lector:
        categoria = fila["Categoria"]
        monto = float(fila["Monto"])

        gastos_por_categoria[categoria] = gastos_por_categoria.get(categoria, 0) + monto

print("Gastos por categoría:")
total = 0
for categoria, monto in gastos_por_categoria.items():
    print(f"-{categoria}: ${monto:.2f}")
    total += monto

print(f"\nGasto total del mes: ${total:.2f}")

# Gastos.csv
Categoria,Descripcion,Monto
Alimentación,Compra supermercado,45.20
Transporte,Taxi,10.00
Alimentación,Restaurante,22.50
Ocio,Cine,8.00
Transporte,Bus,1.50



# Día 264 / 365
# Mini monitor de cambios en carpeta

import os, time

def estado(carpeta):
    return {f: os.path.getmtime(os.path.join(carpeta, f)) for f in os.listdir(carpeta)}

carpeta = input("Ruta de carpeta a monitorear: ").strip()
anterior = estado(carpeta)

print("Monitoreando cambios... (Ctrl+C para salir)\n")
try: 
    while True:
        time.sleep(2)
        actual = estado(carpeta)

        for f in actual.keys() - anterior.keys():
            print(f"Nuevo: {f}")
        for f in anterior.keys() - actual.keys():
            print(f"Eliminado: {f}")
        for f in actual.keys() & anterior.keys():
            if actual[f] != anterior[f]:
                print(f"Modificado: {f}")
        anterior = actual
except KeyboardInterrupt:
    print("\nMonitoreo detenido.")



#Día 265 / 365
#Conciliación bancaria automática con archivos CSV

import pandas as pd
from datetime import timedelta

DIAS_TOL = 1
MONTO_TOL = 0.01

ventas = pd.read_csv("ventas.csv", parse_dates=["fecha"])
banco = pd.read_csv("banco.csv", parse_dates=["fecha"])

conciliados = []
usadas_v, usadas_b = set(), set()

for i, b in banco.iterrows():
    candidatos = ventas[~ventas.index.isin(usadas_v)]
    candidatos = candidatos[(abs(candidatos["monto"] - b["monto"]) <= MONTO_TOL) &
                            (candidatos["fecha"].between(b["fecha"] - timedelta(DIAS_TOL),
                                                         b["fecha"]+timedelta(DIAS_TOL)))]
    if not candidatos.empty:
        v = candidatos.iloc[0]
        usadas_v.add(v.name); usadas_b.add(i)
        conciliados.append([b["id_banco"], b["fecha"], b["monto"],
                            v["id_venta"], v["fecha"], v["monto"]])

pd.DataFrame(conciliados, columns=["id_banco", "fecha_banco", "monto_banco",
                                   "id_venta", "fecha_venta", "monto_venta"]).to_csv("conciliados.csv", index=False)

ventas[~ventas.index.isin(usadas_v)].to_csv("ventas_no_conciliadas.csv", index=False)
banco[~banco.index.isin(usadas_b)].to_csv("banco_no_conciliadas.csv", index=False)

print("Conciliación lista")



#Día 266 / 265
#Generador de contraseñas únicas sin repetir

import random
import string
import os

archivo = "passwords.txt"

def generar_password(longitud=10):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(caracteres) for _ in range(longitud))

def cargar_existentes():
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            return set(line.strip() for line in f)
    return set()

def guardar_password(passwords):
    with open(archivo, "a", encoding="utf-8") as f:
        for p in passwords:
            f.write(p + "\n")

if __name__ == "__main__":
    cantidad = int(input("¿Cuántas contraseñas deseas generar? "))
    existentes = cargar_existentes()
    nuevas = []

    while len(nuevas) < cantidad:
        pwd = generar_password()
        if pwd not in existentes and pwd not in nuevas:
            nuevas.append(pwd)
            print(f"Contraseña creada: {pwd}")

    guardar_password(nuevas)
print(f"Todas las contraseñas se guardaron en {archivo}")


