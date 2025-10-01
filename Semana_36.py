# Día 246 / 365
"""
Análisis de logs para detectar intentos sospechosos
"""

from collections import Counter

#Ejemplo de archivo de logs
logs = """
2025-09-03 10:22:01 - LOGIN FAIL - IP: 192.168.1.10
2025-09-03 10:22:05 - LOGIN FAIL - IP: 192.168.1.11
2025-09-03 10:22:07 - LOGIN FAIL - IP: 192.168.1.10
2025-09-03 10:22:10 - LOGIN FAIL - IP: 192.168.1.10
2025-09-03 10:22:20 - LOGIN SUCCESS - IP: 192.168.1.12
2025-09-03 10:22:25 - LOGIN FAIL - IP: 192.168.1.11
2025-09-03 10:22:28 - LOGIN FAIL - IP: 192.168.1.11
"""

#Extraer IPs de intetntos fallidos
ips = []
for linea in logs.splitlines():
    if "LOGIN FAIL" in linea:
        ip = linea.split("IP: ")[1]
        ips.append(ip)

#Contar intentos por IP
conteo = Counter(ips)

#Definir umbral
umbral = 2

print("Intentos fallidos por IP:")
for ip, intentos in conteo.items():
    print(f"{ip}: {intentos} intentos")
    if intentos >umbral:
        print(f"⚠️ POsible ataque de fuerza bruta desde {ip}")



# Día 247 / 365
"""
Monitoreo de uso de CPU y memoria en Python
"""
import psutil
import time

def monitorear():
    while True:
        cpu = psutil.cpu_percent(interval=1)

        memoria = psutil.virtual_memory().percent

        print(f"CPU: {cpu}% | Memoria: {memoria}%")

        if cpu > 80:
            print(f"⚠️ Alerta: Uso de CPU muy alto")
        if memoria > 80:
            print("⚠️ Alerta: Uso de memoria muy alta")

        time.sleep(2)

monitorear()



# Día 248 / 365
"""
Detección de archivos duplicados en una carpeta usando hash MD5
"""
import os
import hashlib

def hash_archivo(ruta, bloque=65536):
    md5 = hashlib.md5()
    with open(ruta, "rb") as f:
        while chunk := f.read(bloque):
            md5.update(chunk)
    return md5.hexdigest()

def buscar_duplicados(carpeta):
    hashes = {}
    duplicados = {}

    for raiz, _, archivos in os.walk(carpeta):
        for archivo in archivos:
            ruta = os.path.join(raiz, archivo)
            try:
                h = hash_archivo(ruta)
                if h in hashes:
                    duplicados.setdefault(h, []).append(ruta)
                else:
                    hashes[h] = ruta
            except Exception as e:
                print(f"Error con {ruta}: {e}")

    return duplicados

carpeta_objetivo = "Mini_Reporte_Ventas.xlsx"
resultado = buscar_duplicados(carpeta_objetivo)

if resultado:
    print("Archivos duplicados encontrados:\n")
    for h, rutas in resultado.items():
        print(f"Hash: {h}")
        print(" - Original:", rutas[0])
        for dup in rutas[1:]:
            print(" - Duplicado:", dup)
        print()
else:
    print("No se encontraron duplicados")


# Día 249 / 365
# Organizador de ideas rápidas en consola

from datetime import datetime

archivo = "ideas.txt"

print("=== Organizador de Ideas en Terminal ===")
print("Escribe tus ideas (escribe 'fin' para salir)\n")

while True:
    idea = input("💡 Idea: ")
    if idea.lower() == "fin":
        print("✅ Todas tus ideas han sido guardadas en 'ideas.txt'")
        break

    with open(archivo, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {idea}\n")
    print("✔ Idea guardadas\n")


# Día 250 / 365
# Generador de reportes PDF de ventas

import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

#Leer archivo CSV
archivo_csv = "ventas.csv"
df = pd.read_csv(archivo_csv)

#Calcular estadísticas
total_ventas = df["Monto"].sum()
promedio = df["Monto"].mean()
mejor_producto = df.groupby("Producto")["Monto"].sum().idxmax()
venta_maximas = df["Monto"].max()

#Crear pdf
archivo_pdf = "reporte_ventas.pdf"
c = canvas.Canvas(archivo_pdf, pagesize=letter)
c.setFont("Helvetica", 12)

c.drawString(100, 750, "📊 Reporte de Ventas")
c.drawString(100, 720, f"Total de ventas: ${total_ventas:.2f}")
c.drawString(100, 700, f"Promedio de venta: ${promedio:.2f}")
c.drawString(100, 680, f"Producto más vendido: {mejor_producto}")
c.drawString(100, 660, f"Venta más alta registrada: ${venta_maximas}")

c.save()

print("✅ Reporte generado en 'reporte_ventas.pdf'")



# Día 251 / 365
# Detector de anomalías en temperaturas

import pandas as pd

df = pd.read_csv("temperaturas.csv")

media = df["temperatura"].mean()
desviacion = df["temperatura"].std()

umbral_inferior = media - 2 * desviacion
umbral_superior = media + 2 * desviacion

anomalias = df[(df["temperatura"] < umbral_inferior) | (df["temperatura"] > umbral_superior)]

print("Promedio de temperatura:", round(media, 2))
print("Desviación estándar:", round(desviacion, 2))
print("\nAnomalías detectadas:")
print(anomalias)

anomalias.to_csv("anomalías.csv", index=False)
print("\n✅ Archivo 'anomalías.csv' creado con los registros fuera de lo normal")


# Temperaturas.csv
fecha,temperatura
2025-01-01,22
2025-01-02,23
2025-01-03,22
2025-01-04,21
2025-01-05,24
2025-01-06,23
2025-01-07,22
2025-01-08,45
2025-01-09,22
2025-01-10,21
2025-01-11,22
2025-01-12,23
2025-01-13,50
2025-01-14,21
2025-01-15,22
2025-01-16,23
2025-01-17,22
2025-01-18,21
2025-01-19,24
2025-01-20,22




# Día 252 / 365
# Reporte PDF de empleados (versión corta)

import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

#Leer datos
df = pd.read_csv("empleados.csv")

#Crear pdf
doc = SimpleDocTemplate("reporte_empleados.pdf")
tabla = Table([df.columns.to_list()] + df.values.tolist())

#Estilo de tabla
tabla.setStyle(TableStyle([
    ("BACKGROUND", (0, 0),(-1, 0), colors.grey ),
    ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ("GRID", (0,0), (-1,-1), 1, colors.black)

]))

doc.build([tabla])
print("✅ Reporte PDF generado con éxito")

# empleados.csv
Nombre,Puesto,Salario
Ana López,Gerente,2500
Carlos Pérez,Analista,1800
María Gómez,Desarrolladora,2200
Luis Torres,Diseñador,1700
Elena Ruiz,Soporte,1500


