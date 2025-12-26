# Día 302 / 365
# 🧲 Simulación de campo magnético con líneas de flujo

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 40)
y = np.linspace(-5, 5, 40)
X, Y = np.meshgrid(x, y)

polo1 = np.array([-2, 0])
polo2 = np.array([2, 0])

def campo_magnetico(x, y):
    Bx, By = 0, 0
    for px, py, signo in [(polo1[0], polo1[1], 1), (polo2[0], polo2[1], -1)]:
        dx, dy = x - px, y - py
        r2 = dx**2 + dy**2 + 1e-5
        Bx += signo * dx / r2
        By += signo * dy / r2
    return Bx, By

Bx, By = np.zeros_like(X), np.zeros_like(Y)
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        Bx[i, j], By[i, j] = campo_magnetico(X[i, j], Y[i, j])

plt.figure(figsize=(6, 6))
plt.streamplot(X, Y, Bx, By, color=np.hypot(Bx, By), cmap="plasma", density=1.5)
plt.scatter(*polo1, color="red", s=100, label="Norte (+)")
plt.scatter(*polo2, color="blue", s=100, label="Sur (-)")
plt.legend()
plt.axis("off")
plt.title("Simulación de campo magnético", fontsize=12)
plt.show()



# Día 306 / 365
# 📦 Generador de códigos de seguimiento de paquetes

import random
import string

def generar_codigo():
    letras = ''.join(random.choices(string.ascii_uppercase, k=2))
    numeros = ''.join(random.choices(string.digits, k=6))
    sufijo = ''.join(random.choices(string.ascii_uppercase, k=1))
    return f"{letras}{numeros}{sufijo}"

print("📦 Códigos de seguimiento generados:")
for _ in range(10):
    print("-", generar_codigo())


# Día 304 / 365
# 🎨 Generador de arte caótico con trayectorias Lissajous

import numpy as np
import matplotlib.pyplot as plt

n = 1000
t = np.linspace(0, 2*np.pi, n)

a, b = np.random.randint(1, 10), np.random.randint(1, 10)
delta = np.random.uniform(0, np.pi)
x = np.sin(a * t + delta)
y = np.sin(b * t)

plt.figure(figsize=(5, 5), facecolor="black")  
plt.plot(x, y, color=np.random.choice(["cyan", "magenta", "yellow", "lime"]), lw=0.8)  
plt.axis("off")
plt.title("🎨 Arte caótico Lissajous", color="white", fontsize=10) 
plt.show()



# Día 305 / 365
# 🌀 Generador de espirales dinámicas con interferencia de ondas


import numpy as np
import matplotlib.pyplot as plt

n = 500
t = np.linspace(0, 10*np.pi, n)

r = np.sin(3*t) + np.cos(5*t) * 0.5
x = r * np.cos(t)
y = r * np.sin(t)

plt.figure(figsize=(5, 5), facecolor="black")
plt.plot(x, y, color=np.random.choice(["lime", "cyan", "magenta", "yellow"]), lw=1)
plt.axis("off")
plt.title("🌀 Espiral de interferencia de ondas", color="white", fontsize=10)
plt.show()


# Día 306 / 365
# 🌈 Movimiento hipnótico con rotación de puntos

import numpy as np
import matplotlib.pyplot as plt
import time

n = 200
r = np.linspace(0.2, 1, n)
theta = np.linspace(0, 2*np.pi, n)
x, y = r * np.cos(theta), r * np.sin(theta)

plt.ion()
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_facecolor("black")

for i in range(100):
    ax.clear()
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_facecolor("black")

    ang = i * 0.1
    x_rot = x * np.cos(ang) - y * np.sin(ang)
    y_rot = x * np.sin(ang) + y * np.cos(ang)

    ax.scatter(x_rot, y_rot, c=np.sin(theta + ang), cmap="plasma", s=20)
    plt.title("Movimiento hipnótico rotacional", color="white", fontsize=10)
    plt.pause(0.05)

plt.ioff()
plt.show()



# Día 307 / 365
# ✍️ Generador de texto simple con Markov (orden 2)

import random
import re

def build_markov(corpus):
    words = re.findall(r"\w+|[^\w\s]", corpus, flags=re.UNICODE)
    model = {}
    for a, b, c in zip(words, words[1:], words[2:]):
        model.setdefault((a.lower(), b.lower()), []).append(c)
    return model

def generate(model, length=30):
    state = random.choice(list(model.keys()))
    out = [state[0], state[1]]
    for _ in range(length - 2):
        key = (out[-2].lower(), out[-1].lower())
        nxt = random.choice(model.get(key, [random.choice(list(model.keys()))[0]]))
        out.append(nxt)
    return " ".join(out)

if __name__ == "__main__":
    with open("corpus.txt", encoding="utf-8") as f:
        text = f.read()
    model = build_markov(text)
    print(generate(model, length=40))




# Día 308 / 365
# 🌀 Simulación de órbitas caóticas con trayectorias armónicas

import numpy as np
import matplotlib.pyplot as plt
import time

plt.ion()
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_facecolor("black")

n = 200
t = np.linspace(0, 20, n)
colors = plt.cm.plasma(np.linspace(0, 1, 5))

for i in range(200):
    ax.clear()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_facecolor("black")

    for j, c in enumerate(colors):
        x = np.sin(t * (1 + 0.1 * j) + i * 0.1)
        y = np.sin(t * (2 + 0.2 * j) + i * 0.15)
        ax.plot(x,y, color=c, lw=1, alpha=0.7)
    plt.title("Órbitas caóticas armónicas", color="white", fontsize=10)
    plt.pause(0.05)

plt.ioff()
plt.show()




