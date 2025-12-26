# Día 316 / 365
# ⚛️ Simulador de colisiones de partículas en 1D

import random
import time

num_particulas = 5
posiciones = [random.randint(0, 20) for _ in range(num_particulas)]
velocidades = [random.choice([-1, 1]) * random.uniform(0.2, 1.0) for _ in range(num_particulas)]

print("⚙️ Simulador de colisiones 1D\n")
print("Partículas iniciales:")
for i in range(num_particulas):
    print(f"  P{i+1}: posición = {posiciones[i]}, velocidad = {velocidades[i]:.2f}")
print("\nIniciando simulación...\n")

for paso in range(30):
    for i in range(num_particulas):
        posiciones[i] += velocidades[i]
        for j in range(i + 1, num_particulas):
            if abs(posiciones[i] - posiciones[j]) < 0.5:
                velocidades[i], velocidades[j] = velocidades[j], velocidades[i]
                print(f"💥 Colisión entre P{i+1} y P{j+1} en paso {paso+1}")
    
    estado = " ".join(f"P{i+1}:{posiciones[i]:.1f}" for i in range(num_particulas))
    print(f"Paso {paso+1:02d} → {estado}")
    time.sleep(0.3)



# Día 317 / 365
"""
 Simulador de ue recrea cómo se propaga
 una enfermedad en una red de personas
"""
import random

num_personas = 20
prob_conexion = 0.2
prob_contagio = 0.3
tiempo_infeccion = 3

red = {i: [] for i in range(num_personas)}

for i in range(num_personas):
    for j in range(i+1, num_personas):
        if random.random() < prob_conexion:
            red[i].append(j)
            red[j].append(i)

estados = ["S"] * num_personas  
tiempos = [0] * num_personas

paciente_cero = random.randint(0, num_personas - 1)
estados[paciente_cero] = "I"
print(f"Paciente cero: Persona {paciente_cero}\n")

for ronda in range(10):
    print(f"--- Ronda {ronda+1} ---")

    nuevos_infectados = []

    for persona in range(num_personas):
        if estados[persona] == "I":
            tiempos[persona] += 1

            for vecino in red[persona]:
                if estados[vecino] == "S" and random.random() < prob_contagio:
                    nuevos_infectados.append(vecino)

            if tiempos[persona] >= tiempo_infeccion:
                estados[persona] = "R"

    for p in nuevos_infectados:
        estados[p] = "I"

    print("Estados:",
          " ".join(f"{i}:{estados[i]}" for i in range(num_personas)))
    print()



# Día 318 / 365
"""
Sorteo con pesos adaptativos:
los ganadores pierden probabilidad
y los demás ganan probabilidad.
"""
import random

personas = ["Ana", "Luis", "Dani", "Sofi", "Marco", "Elena"]
pesos = [1] * len(personas)
num_rondas = 10

print("Pesos iniciales", dict(zip(personas, pesos)), "\n")

for ronda in range(1, num_rondas + 1):
    ganador = random.choices(personas, weights=pesos, k=1)[0]
    idx = personas.index(ganador)

    perdida  = pesos[idx] * 0.3
    pesos[idx] -= perdida

    for i in range(len(pesos)):
        if i != idx:
            pesos[i] += perdida / (len(personas) - 1)
    
    print("Pesos actuales:",
          {personas[i]: round(pesos[i], 3) for i in range(len(personas))})
    
    print()



# Día 319 / 365
"""
Simulador simple de poblaciones (depredador–presa)
"""
import random

class Raton:
    def __init__(self):
        self.vivo = True

class Gato:
    def __init__(self):
        self.hambre = 0
        self.vivo = True

def simular(dias=20, ratones_iniciales=10, gatos_iniciales=2):
    ratones = [Raton() for _ in range(ratones_iniciales)]
    gatos = [Gato() for _ in range(gatos_iniciales)]

    for dia in range(1, dias + 1):
        print(f"\nDÍA {dia}")

        for gato in gatos:
            if not ratones:
                gato.hambre += 1
                continue
            if random.random() < 0.6:
                ratones.pop()
                gato.hambre = 0   
            else:
                gato.hambre += 1

        gatos = [g for g in gatos if g.hambre < 3]

        nuevos_ratones = []
        for _ in ratones:
            if random.random() < 0.3:
                nuevos_ratones.append(Raton())
        ratones.extend(nuevos_ratones)

        if random.random() < 0.1:
            gatos.append(Gato())

        print(f"Ratones: {len(ratones)} | Gatos: {len(gatos)}")

    return ratones, gatos

if __name__ == "__main__":
    simular()



# Día 320 / 365
# Generador de constelaciones ASCII
import random

def crear_cielo(ancho=40, alto=15, densidad=0.05):
    cielo = [[" " for _ in range(ancho)] for _ in range(alto)]

    estrellas = []
    for y in range(alto):
        for x in range(ancho):
            if random.random() < densidad:
                cielo[y][x] = "*"
                estrellas.append((x, y))
    return cielo, estrellas

def conectar_estrellas(cielo, estrellas, conexiones=3):
    if len(estrellas) < 2:
        return

    for _ in range(conexiones):
        a, b = random.sample(estrellas, 2)
        x1, y1 = a
        x2, y2 = b

        # línea horizontal
        for x in range(min(x1, x2), max(x1, x2) + 1):
            if cielo[y1][x] != "*":
                cielo[y1][x] = "-"

        # línea vertical
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if cielo[y][x2] != "*":
                cielo[y][x2] = "|"

def imprimir_cielo(cielo):
    for fila in cielo:
        print("".join(fila))

if __name__ == "__main__":
    cielo, estrellas = crear_cielo()
    conectar_estrellas(cielo, estrellas)
    imprimir_cielo(cielo)



# Día 321 / 365 
# Simulador de señal ruidosa + detección de picos
import random, math

def generar_senal(n=200, t=0.0, ruido=1.0, picos=5):
    s = [t*i + random.gauss(0, ruido) for i in range(n)]
    for _ in range(picos):
        s[random.randrange(n)] += random.uniform(5*ruido, 9*ruido)
    return s

def detectar_picos(s, k=1.5, win=1):
    avg = sum(s)/len(s)
    std = (sum((x-avg)**2 for x in s)/len(s))**0.5
    thr = avg + k*std
    out = []
    for i in range(win, len(s)-win):
        if s[i] >= thr and all(s[i] > s[i+d] for d in range(-win, win+1) if d):
            out.append(i)
    return out, thr

def ascii_plot(s, p=None, W=80, H=20):
    mn, mx = min(s), max(s)
    R = mx-mn if mx!=mn else 1
    step = max(1, len(s)//W)
    cols = [s[i] for i in range(0, len(s), step)]
    grid = [[" "]*len(cols) for _ in range(H)]
    for j,v in enumerate(cols):
        r = (H-1) - int((v-mn)/R*(H-1))
        grid[r][j] = "*"
    if p:
        pc = {i//step for i in p}
        for c in pc:
            for r in range(H):
                if grid[r][c] == "*":
                    grid[r][c] = "^"; break
    for row in grid: print("".join(row))
    print("-"*len(cols), f"\nmin={mn:.2f} max={mx:.2f}")

if __name__ == "__main__":
    N = 300
    sen = generar_senal(N, t=0.005, ruido=1.2, picos=8)
    p, thr = detectar_picos(sen, k=1.6, win=2)
    print(f"Picos detectados: {len(p)}  Umbral={thr:.2f}\n")
    ascii_plot(sen, p, W=100, H=20)



# Día 322 / 365 (alternativo)
"""
Simulador de predicción de tormentas 
con probabilidad dinámica
"""
import random
import time
from collections import deque
historial = deque(maxlen=10)

def generar_lectura():
    humedad = random.uniform(40, 100)    
    presion = random.uniform(950, 1020)   
    viento  = random.uniform(0, 40)         
    return humedad, presion, viento

def calcular_probabilidad(hum, pres, wind, tendencia):
    prob = 0
    
    if hum > 80: prob += 25
    if pres < 980: prob += 35
    if wind > 25: prob += 20
    
    prob += tendencia
    
    return min(100, prob)

tendencia = 0

print("🌪️ Simulador de predicción de tormentas\n")

for minuto in range(1, 31):
    hum, pres, wind = generar_lectura()
    historial.append((hum, pres, wind))
    
    if len(historial) == historial.maxlen:
        promedio_hum = sum(h[0] for h in historial) / len(historial)
        tendencia = (promedio_hum - 70) * 0.2  
    prob = calcular_probabilidad(hum, pres, wind, tendencia)
    
    estado = (
        "⚠️ Probable tormenta" if prob > 60 else
        "🌤️ Estable" if prob < 30 else
        "⛅ Cambios posibles"
    )
    
    print(f"[Min {minuto}] H:{hum:.1f}%  P:{pres:.1f}hPa  V:{wind:.1f}km/h")
    print(f" → Probabilidad de tormenta: {prob:.1f}% | Estado: {estado}\n")
    
    time.sleep(0.3)


