# Día 295 / 365
# 🌌 Simulador de galaxia con puntos aleatorios en espiral
import numpy as np
import matplotlib.pyplot as plt

n = 800

theta = np.linspace(0, 6 * np.pi, n)
r = np.linspace(0, 1, n)

x = r * np.cos(theta) + np.random.normal(0, 0.05, n)
y = r * np.sin(theta) + np.random.normal(0, 0.05, n)
color = np.sqrt(x**2 + y**2)

plt.figure(figsize=(5, 5))
plt.scatter(x, y, c=color, cmap="plasma", s=5)
plt.axis("off")
plt.title("🌌 Simulador de galaxia espiral", fontsize=10)
plt.show()  



# Día 296 / 365
# 🌧️ Simulador de lluvia con Matplotlib

import matplotlib.pyplot as plt
import numpy as np
import time
import os

plt.ion()
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_facecolor("black")

drops = np.random.rand(50, 2) * 100

for _ in range(100):
    ax.clear()
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_facecolor("black")

    drops[:, 1] -= np.random.rand(50) * 5
    drops[drops[:, 1] < 0, 1] = 100

    ax.scatter(drops[:, 0], drops[:, 1], color="cyan", s=10)
    plt.title("🌧️ Simulador de lluvias", color="white", fontsize=10)
    plt.pause(0.10)

plt.ioff()
plt.show()


# Día 297 / 365
# 🧠 Generador de laberinto con algoritmo DFS
import numpy as np
import matplotlib.pyplot as plt
import random
import time

n = 15
maze = np.ones((n, n))

dirs = [(-2, 0), (2, 0), (0, -2), (0, 2)]

def generar(x,y):
    maze[x, y] = 0
    random.shuffle(dirs)
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and maze[nx, ny] == 1:
            maze[x +  dx//2, y + dy//2] = 0
            generar(nx, ny)

            plt.imshow(maze, cmap="binary")
            plt.axis("off")
            plt.pause(0.05)

plt.figure(figsize=(5, 5))
generar(0, 0)
plt.title("🧠 Generador de laberinto aleatorio (DFS)", fontsize=10)
plt.show()



# Día 298 / 365
# 🔥 Simulación de difusión de calor en una placa

import numpy as np
import matplotlib.pyplot as plt
import time

n = 30
m = np.zeros((n, n))

m[n//2, n//2] = 100

plt.ion()
fig, ax = plt.subplots()

for t in range(100):
    ax.clear()
    m[1:-1, 1:-1] = (
        m[0:-2, 1:-1] + m[2:, 1:-1] +
        m[1:-1, 0:-2] + m[1:-1, 2:]
    ) / 4

    m[n//2, n//2] = 100

    ax.imshow(m, cmap="hot", interpolation="nearest")
    plt.title(f"🔥 Difusión de calor - Paso {t}", fontsize=10)
    plt.axis("off")
    plt.pause(0.05)

plt.ioff()
plt.show()



# Día 299 / 365
# ⚡ Simulación de rayos eléctricos (líneas fractales)
import matplotlib.pyplot as plt
import numpy as np
import random

def rayo(x1, y1, x2, y2, desvio, nivel):
    if nivel == 0:
        plt.plot([x1, x2], [y1, y2], color="cyan", linewidth=1)
    else:
        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2
        mx += random.uniform(-desvio, desvio)
        my += random.uniform(-desvio, desvio)
        rayo(x1, y1, mx, my, desvio / 2, nivel - 1)
        rayo(mx, my, x2, y2, desvio / 2, nivel - 1)

plt.figure(figsize=(5, 5), facecolor="black")
plt.axis("off")
for _ in range(3):
    rayo(0, 1, 1, 0, 0.2, 8)
plt.title("⚡ Simulación de rayos eléctricos", color="cyan", fontsize=10)
plt.show()



# Día 300 / 365
# 🧬 Algoritmo genético: adivinar una contraseña

import random
import string

objetivo = "PYTHON"
caracteres = string.ascii_uppercase

tam_poblacion = 100
tasa_mutacion = 0.1
generacion = 0

def generar_cadena():
    return ''.join(random.choice(caracteres) for _ in range(len(objetivo)))

def fitness(cadena):
    return sum (1 for a, b in zip(cadena, objetivo) if a == b)

poblacion = [generar_cadena() for _ in range(tam_poblacion)]

while True:
    poblacion = sorted(poblacion, key=fitness, reverse=True)
    mejor = poblacion[0]
    print(f"Generación {generacion:3d} | Mejor: {mejor} | Precisión: {fitness(mejor)}")

    if mejor == objetivo:
        print("\n🎉 Contraseña encontrada:", mejor)
        break

    padres = poblacion[:20]

    nueva_poblacion = []
    for _ in range(tam_poblacion):
        p1, p2 = random.sample(padres, 2)
        punto = random.randint(0, len(objetivo) - 1)
        hijo = p1[:punto] + p2[punto:]

        if random.random() < tasa_mutacion:
            pos = random.randint(0, len(objetivo) -1)
            hijo = hijo[:pos] + random.choice(caracteres) + hijo[pos + 1:]

        nueva_poblacion.append(hijo)

    poblacion = nueva_poblacion
    generacion += 1



# Día 301 / 365
# 🌍 Simulador de partículas gravitacionales simples

import matplotlib.pyplot as plt
import numpy as np

n = 20
pos = np.random.rand(n, 2) * 10  
vel = np.zeros((n, 2))           
masa = np.random.rand(n) * 2 + 1 

G = 0.1 

plt.ion()
fig, ax = plt.subplots(figsize=(5, 5))

for paso in range(150):
    ax.clear()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_facecolor("black")

    for i in range(n):
        fuerza = np.zeros(2)
        for j in range(n):
            if i != j:
                dir = pos[j] - pos[i]
                dist = np.linalg.norm(dir) + 0.1
                fuerza += G * masa[i] * masa[j] * dir / dist**3
        vel[i] += fuerza / masa[i]
    pos += vel * 0.1

    ax.scatter(pos[:, 0], pos[:, 1], color="white", s=20)
    plt.title("🌍 Simulación gravitacional simple", color="white", fontsize=10)
    plt.pause(0.05)

plt.ioff()
plt.show()
