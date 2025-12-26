# Día 274 / 365
"""
Simulador de trayectoria de un proyectil
"""
import math
import time

g = 9.8

#Pedir datos al usuario
v = float(input("Velocidad inicial (m/s): "))
angulo = float(input("Angulo de lanzamiento (grados): "))

# Convertir ángulo a radianes
theta = math.radians(angulo)

t = 0
dt = 0.5 #Intervalo de tiempo (medio segundo)

print("\nSimulación de la trayectoria:\n")

while True:
    #Fórmula del movimiento
    x = v * math.cos(theta) * t
    y = v * math.sin(theta) * t - 0.5 * g * t**2

    if y < 0:
        break

    print(f"t={t:.1f}s -> x={x:.2f}m, y={y:.2f}m")

    time.sleep(0.3) #pausa para simular "tiempo real"
    t += dt

print("\nEl proyectil ha caído al suelo.")



# Día 275 / 365
#Detector de similitud de textos con embeddings en Python.

import spacy

# Cargar modelo en español
# (Antes de correr: instala el modelo con -->  python -m spacy download es_core_news_md)
nlp = spacy.load("es_core_news_md")

# Pedir frases al usuario
texto1 = input("Escribe la primera frase: ")
texto2 = input("Escribe la segunda frase: ")

# Procesar textos con spaCy
doc1 = nlp(texto1)
doc2 = nlp(texto2)

# Calcular similitud semántica
similitud = doc1.similarity(doc2) * 100

print(f"Similitud entre los textos: {similitud:.2f}%")



# Día 276 / 365
# Simulador de estación de servicio

import random
import time

# Párametros iniciales
precio_litro = 2.25
ganancias = 0
autos_totales = 0

print("⛽ Simulador de Estación de Servicio\n")

for minuto in range(1, 16):
    print(f"🕒 Minuto: {minuto}")

    # Probabilidad de llegada de autos
    if random.random() < 0.8:
        autos_totales += 1
        litros = random.randint(5, 50) #litro cargado
        paga = litros * precio_litro
        ganancias += paga
        print(f"🚗 Auto: {autos_totales} cargó {litros}L -> Pagó ${paga:.2f}")
    else:
        print("X No llegó ningún auto este minuto.")
    
    # Mostrar resumen parcial
    print(f"💰 Ganancias acumuladas: ${ganancias:.2f}")
    print("-" * 40)
    time.sleep(1)

#Resumen final
print("\n🏁 Final de la simulación")
print(f"Autos atendidos: {autos_totales}")
print(f"Ganancia total: ${ganancias:.2f}")



# Día 277 / 365
# Detector de anomalías en datos de sensores


import random
import time

# Parámetros del sensor
rango_min = 20
rango_max = 30
lecturas_totales = 0
anomalías = []

print("📡 Simulador de Sensor con Detección de Anomalías\n")

# Simulamos 20 lecturas en "tiempo real"
for i in range(20):
    valor = random.uniform(15, 35)  # genera un valor aleatorio
    lecturas_totales += 1
    print(f"Lectura {i+1}: {valor:.2f} °C")

    # Detectar si está fuera del rango
    if valor < rango_min or valor > rango_max:
        print("⚠️ Anomalía detectada")
        anomalías.append(valor)

    time.sleep(0.5)

# Resumen final
print("\n📊 Resumen del Monitoreo:")
print(f"Total de lecturas: {lecturas_totales}")
print(f"Anomalías detectadas: {len(anomalías)}")
if anomalías:
    print("Valores anómalos:", [f"{v:.2f}" for v in anomalías])
else:
    print("✅ No se detectaron anomalías")




# Día 278 / 365
# Simulador de votación en tiempo real 

import random
import time
from collections import Counter

candidatos = ["Alice", "Robert", "Carlos"]
votos = Counter()
total_votos = 0

print("🔴 Simulador de votación en tiempo real")
print("Candidatos:", ", ".join(candidatos))
print("Presiona Ctrl+C para detener la simulación.\n")

try:
    # Parámetros de la simulación
    num_votos = 100            # número máximo de votos simulados
    espera_min, espera_max = 0.05, 0.5

    for i in range(1, num_votos + 1):
        # Simular llegada de un voto
        elegido = random.choices(candidatos, weights=[0.4, 0.35, 0.25])[0]
        votos[elegido] += 1
        total_votos += 1

        # Calcular líder y porcentajes
        lider_count = max(votos.values())
        lideres = [c for c, n in votos.items() if n == lider_count]
        lider_text = ", ".join(lideres)

        porcentajes = {c: (votos[c] / total_votos) * 100 for c in candidatos}

        # Mostrar estado en tiempo real
        print(f"Voto #{i}: {elegido}  |  Total: {total_votos}")
        for c in candidatos:
            print(f"  - {c}: {votos[c]} votos ({porcentajes[c]:5.1f}%)")
        print(f"→ Líder(es): {lider_text}\n{'-'*40}")

        # Espera aleatoria para simular tiempo real
        time.sleep(random.uniform(espera_min, espera_max))

except KeyboardInterrupt:
    print("\nSimulación interrumpida por el usuario.\n")

# Resultado final
print("\n🏁 Resultado final")
print(f"Total de votos: {total_votos}")
for c in candidatos:
    pct = (votos[c] / total_votos * 100) if total_votos else 0
    print(f" - {c}: {votos[c]} votos ({pct:.1f}%)")

# Determinar ganador (o empate)
if total_votos:
    max_votos = max(votos.values())
    ganadores = [c for c, n in votos.items() if n == max_votos]
    if len(ganadores) == 1:
        print(f"\n🎉 Ganador: {ganadores[0]} con {max_votos} votos")
    else:
        print(f"\n🤝 Empate entre: {', '.join(ganadores)} (cada uno con {max_votos} votos)")
else:
    print("\nNo se registraron votos.")



# Día 279 / 365
# Simulador de crecimiento bacteriano 🧫

import random
import time
import os

filas, columnas = 10, 20
poblacion = [["." for _ in range(columnas)] for _ in range(filas)]

for _ in range(10):
    x, y = random.randint(0, filas - 1), random.randint(0, columnas - 1)
    poblacion[x][y] = "🦠"

def mostrar(poblacion):
    os.system("cls" if os.name == "nt" else "clear")
    for fila in poblacion:
        print(" ".join(fila))
    print()

def siguiente_generacion(poblacion):
    nueva = [fila[:] for fila in poblacion]
    for i in range(filas):
        for j in range(columnas):
            vecinos = 0
    
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    x, y = i + dx, j + dy
                    if 0 <= x < filas and 0 <= y < columnas:
                        if poblacion[x][y] == "🦠":
                            vecinos += 1

            if poblacion[i][j] == "🦠":
                if vecinos < 2 or vecinos > 3:
                    nueva[i][j] = "."
            else:
                if vecinos == 3:
                    nueva[i][j] = "🦠"
            
    return nueva

for _ in range(30):
    mostrar(poblacion)
    poblacion = siguiente_generacion(poblacion)
    time.sleep(0.3)



# Día 280 / 365
# Generador de constelaciones estelares ✨

import random
import os
import time

ancho, alto = 40, 15

def generar_cielo():
    return[["." if random.random() > 0.1 else "✦" for _ in range(ancho)] for _ in range(alto)]

def mostrar_cielo(cielo):
    os.system("cls" if os.name == "nt" else "clear")
    for fila in cielo:
        print("".join(fila))
    print("\n🌌 Cielo generado al azar\n")

for _ in range(10):
    cielo = generar_cielo()
    mostrar_cielo(cielo)
    time.sleep(0.4)
    
