# Día 309 / 365
# Mensaje oculto en imagen

from PIL import Image

def ocultar(img_in, img_out, msg):
    img = Image.open(img_in).convert("RGB")
    bits = ''.join(f'{ord(c):08b}' for c in msg) + '00000000'
    data = list(img.getdata())
    i = 0
    new_data = []
    for px in data:
        rgb = []
        for c in px:
            if i < len(bits):
                rgb.append((c & ~1) | int(bits[i]))
                i += 1
            else:
                rgb.append(c)
        new_data.append(tuple(rgb))
    img.putdata(new_data)
    img.save(img_out)
    print(f"✅ Mensaje oculto en {img_out}")

def mostrar(img_in):
    bits = ''
    for px in Image.open(img_in).getdata():
        for c in px[:3]:
            bits += str(c & 1)
    texto = ''.join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8))
    print("📩 Mensaje:", texto.split('\x00')[0])

# Ejemplo:
# ocultar("foto.png", "secreto.png", "Hola mundo!")
# mostrar("secreto.png")


# Día 310 / 365
# 🧊 Cubo 3D rotatorio con Matplotlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1,1,1])

# Vértices del cubo
r = [-1, 1]
X, Y = np.meshgrid(r, r)
ones = np.ones_like(X)

caras = [
    (X, Y, ones), (X, Y, -ones), 
    (X, ones, Y), (X, -ones, Y),
    (ones, X, Y), (-ones, X, Y)
]

plt.ion()
for ang in range(180):
    ax.clear()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)
    ax.set_facecolor("black")

    for X, Y, Z in caras:
        ax.plot_surface(X, Y, Z, color="cyan", alpha=0.6, edgecolor="white")

    ax.view_init(elev=20, azim=ang)
    plt.title("🧊 Cubo 3D Rotatorio", color="white", fontsize=10)
    plt.pause(0.05)

plt.ioff()
plt.show()


# Día 311 / 365
# 🌌 Simulación de partículas orbitando un punto central
import numpy as np
import matplotlib.pyplot as plt
import time

plt.ion()
fig, ax = plt.subplots(figsize=(6,6))
ax.set_facecolor("black")

n = 60
r = np.linspace(0.2, 3, n)
a = np.random.rand(n) * 2 * np.pi
v = 0.02 / (r + 0.2)
colors = plt.cm.plasma(np.linspace(0, 1, n))

for frame in range(800):
    ax.clear()
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_facecolor("black")
    ax.scatter(0, 0, color="yellow", s=80)

    x = r * np.cos(a)
    y = r * np.sin(a)
    ax.scatter(x, y, c=colors, s=20)

    a += v
    plt.title("Sistema de partículas orbitales", color="white")
    plt.pause(0.02)

plt.ioff()
plt.show()


# Día 312 / 365
# 🌀 Espiral 3D dinámica con rotación continua

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

plt.ion()
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor("black")

t = np.linspace(0, 8*np.pi, 500)
r = np.linspace(0.1, 2, 500)
x = r * np.cos(t)
y = r * np.sin(t)
z = np.linspace(-2, 2, 500)
colors = plt.cm.plasma(np.linspace(0, 1, len(t)))

for angle in range(360):
    ax.clear()
    ax.set_facecolor("black")
    ax.plot(x, y, z, color="cyan", lw=1.5)
    ax.scatter(x, y, z, c=colors, s=10)
    ax.view_init(30, angle)  # rota la cámara
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_zlim(-2.5, 2.5)
    plt.title("Espiral 3D dinámica", color="white", fontsize=10)
    plt.pause(0.03)

plt.ioff()
plt.show()


# Día 313 / 365
# 🫀 ECG sintético + detección de picos R (simple)

import numpy as np
import matplotlib.pyplot as plt

fs = 250                
dur = 8                 
t = np.linspace(0, dur, dur*fs)
beat = np.exp(-((np.linspace(-0.5,0.5, int(0.6*fs)))**2)/(2*(0.03**2)))
beat = np.concatenate([np.zeros(int(0.2*fs)), beat, np.zeros(int(0.2*fs))])
rr_mean = 0.8  
signal = np.zeros_like(t)
pos = 0.0
i = 0
while pos < dur:
    idx = int(pos*fs)
    end = idx + len(beat)
    if end < len(signal):
        signal[idx:end] += beat * (0.8 + 0.4*np.random.rand())  
    pos += rr_mean + 0.1*(np.random.rand()-0.5)  
    i += 1

signal += 0.05*np.sin(2*np.pi*0.5*t) + 0.02*np.random.randn(len(t))
umbral = signal.mean() + 0.6*signal.std()
peaks = []
for k in range(1, len(signal)-1):
    if signal[k] > umbral and signal[k] > signal[k-1] and signal[k] > signal[k+1]:
        if not peaks or (k - peaks[-1]) > 0.2*fs:
            peaks.append(k)

bpm = len(peaks) / (dur/60)

plt.figure(figsize=(10,3))
plt.plot(t, signal, label="ECG sintético")
plt.scatter(t[peaks], signal[peaks], color="red", label="Picos R")
plt.title(f"ECG sintético — Latidos detectados: {len(peaks)} — BPM ≈ {bpm:.1f}")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (u.a.)")
plt.legend()
plt.tight_layout()
plt.show()



# Día 314 / 365
# 🌪️ Simulador del atractor caótico de Clifford

import numpy as np
import matplotlib.pyplot as plt

a, b, c, d = -1.4, 1.6, 1.0, 0.7

n = 50000
x, y = np.zeros(n), np.zeros(n)
x[0], y[0] = 0.1, 0.1

for i in range(1, n):
    x[i] = np.sin(a * y[i-1]) + c * np.cos(a * x[i-1])
    y[i] = np.sin(b * x[i-1]) + d * np.cos(b * y[i-1])

plt.figure(figsize=(6, 6), facecolor="black")
plt.scatter(x, y, s=0.2, color="cyan")
plt.axis("off")
plt.title("Atractor caótico de Clifford", color="white", fontsize=12)
plt.show()


# Día 315 / 365
"""
Detector de estrés en texto basado 
en frecuencia de palabras
"""
import re

# Palabras asociadas a estrés o calma
estres = ["presión", "agotado", "estresado", "cansado", "problema", "urgente", "difícil", "miedo", "caos"]
calma = ["tranquilo", "paz", "descanso", "relajado", "fácil", "feliz", "controlado", "seguro", "bien"]

def limpiar_texto(texto):
    return re.findall(r'\b\w+\b', texto.lower())

def analizar_estres(texto):
    palabras = limpiar_texto(texto)
    puntaje = 0
    for palabra in palabras:
        if palabra in estres:
            puntaje += 1
        elif palabra in calma:
            puntaje -= 1
    return puntaje

texto = input("Escribe cómo te sientes hoy: ")
puntaje = analizar_estres(texto)

print("\n🧠 Análisis emocional del texto:")
if puntaje > 2:
    print("😰 Nivel alto de estrés detectado.")
elif puntaje > 0:
    print("😟 Ligero nivel de tensión.")
elif puntaje == 0:
    print("😐 Emoción neutral.")
else:
    print("😌 Nivel de calma detectado.")
