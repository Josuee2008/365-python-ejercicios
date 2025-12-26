# Día 288 / 365
# 😴 Registro de horas de sueño (SQLite + Matplotlib)

import sqlite3, datetime, random
import matplotlib.pyplot as plt

conn = sqlite3.connect("sueno.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS descanso(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT,
    horas REAL
)
""")

hoy = datetime.date.today()
horas = round(random.uniform(4, 9), 1)
cur.execute("INSERT INTO descanso(fecha, horas) VALUES (?, ?)", (hoy, horas))
conn.commit()

cur.execute("SELECT fecha, horas FROM descanso ORDER BY id")
datos = cur.fetchall()
conn.close()

fechas = [d[0] for d in datos]
valores = [d[1] for d in datos]

plt.plot(fechas, valores, marker="o", color="blue")
plt.title("😴 Horas de sueño registradas")
plt.xlabel("Fechas")
plt.ylabel("Horas dormidas")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

prom = sum(valores) / len(valores)
print(f"🌙 Hoy dormiste {horas} horas")
print(f"🧮 Promedio histórico: {prom:.1f} horas")


# Día 289 / 365
# ⌨️ Detector de velocidad de escritura (WPM Test)

import time

texto = "Python es increíble para automatizar y crear cosas útiles."
print("🧠 Escribe exactamente el siguiente texto y presiona Enter:\n")
print(f"👉 {texto}\n")

input("Presiona Enter cuando estés listo...")
inicio = time.time()
escrito = input("\n✍️ Escribe aquí: ")
fin = time.time()

tiempo = fin - inicio
palabras = len(escrito.split())
wpm = (palabras / tiempo) * 60

print(f"\n⌛ tiempo: {tiempo:.1f}s")
print(f"📝 Palabras: {palabras}")
print(f"⚡ Velocidad: {wpm:.1f} palabras por minuto")

if escrito == texto:
    print("✅ Texto correcto.")
else:
    print("❌ Texto con errores.")



# Día 290 / 365
# 📅 Calendario mensual en consola

import calendar
import datetime

hoy = datetime.date.today()
anio = hoy.year
mes = hoy.month

print(f"📆 Calendario de {calendar.month_name[mes]} {anio}\n")
print(calendar.month(anio, mes))



# Día 291 / 365
# 🌀 Triángulo de Sierpinski en consola

import random

tamano = 32
matriz = [[" " for _ in range(tamano*2)] for _ in range(tamano)]

x, y = tamano, 0
matriz[y][x] = "*"

interaciones = 5000

vertice = [(0, tamano-1), (tamano, 0), (tamano*2, tamano-1)]

for _ in range(interaciones):
    vx, vy = random.choice(vertice)
    x = (x + vx)//2
    y = (y + vy)//2
    matriz[y][x] = "*"

for fila in matriz:
    print("".join(fila))


# Día 292 / 365
# 🧲 Simulador de atracción magnética

import time
import os

p1, p2 = 0, 30
while p1 < p2:
    os.system("cls" if os.name == "nt" else "clear")
    lineas = [" "] * 31
    lineas[p1] = "🔵"
    lineas[p2] = "🔴"
    print("".join(lineas))
    time.sleep(0.1)

    p1 += 1
    p2 -= 1

os.system("cls" if os.name == "nt" else "clear")
print("💥 Las partículas se han unido en el centro 💥")



# Día 293 / 365
# Recomendador item-based simple (cosine similarity)

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

data = {
    "prod_A": [5, 4, 0, 0, 3],
    "prod_B": [4, 0, 0, 2, 3],
    "prod_C": [0, 0, 5, 4, 0],
    "prod_D": [0, 3, 4, 0, 0],
    "prod_E": [1, 0, 0, 0, 2],
}
users = ["u1","u2","u3","u4","u5"]
R = pd.DataFrame(data, index=users)

# 1) matriz item-feature (productos como filas)
items = R.T
# 2) similitud entre productos (coseno)
sim = pd.DataFrame(cosine_similarity(items), index=items.index, columns=items.index)

def recomendar(usuario_id, top_n=3):
    user_ratings = R.loc[usuario_id]
    # calcular score estimado = suma(similaridad * rating) / suma(similaridad)
    scores = {}
    for item in items.index:
        if user_ratings[item] != 0:
            continue  # ya lo vio
        # consideramos contribución de todos los items que el usuario calificó
        numer = 0.0
        denom = 0.0
        for rated_item, rating in user_ratings[user_ratings > 0].items():
            s = sim.loc[item, rated_item]
            numer += s * rating
            denom += abs(s)
        scores[item] = numer / denom if denom != 0 else 0
    # ordenar y devolver top N
    recs = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return recs[:top_n]

# Ejemplo: recomendaciones para el usuario u1
print("Matriz de ratings (usuarios x productos):")
print(R, "\n")
print("Similitud entre productos (parcial):")
print(sim.round(2), "\n")

usuario = "u1"
print(f"✅ Recomendaciones para {usuario}:")
for item, score in recomendar(usuario, top_n=3):
    print(f"- {item}  (score: {score:.3f})")



# Día 294 / 365
# 🎨 Generador de arte abstracto sin Perlin Noise
import numpy as np
import matplotlib.pyplot as plt
import random, math

ancho, alto = 200, 200

color = random.choice(["plasma", "magma", "viridis", "cividis", "inferno"])

x = np.linspace(0, 5, ancho)
y = np.linspace(0, 5, alto)
X, Y = np.meshgrid(x, y)

Z = np.sin(X * 2 + np.cos(Y * 3)) + np.cos(X * Y) * 0.5
Z += np.random.normal(0, 0.1, (alto, ancho))

Z = (Z - Z.min()) / (Z.max() - Z.min())

plt.imshow(Z, cmap=color)
plt.axis("off")
plt.title("🎨 Arte abstracto generado con funciones matemáticas", fontsize=10)
plt.show()
