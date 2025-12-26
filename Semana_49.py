# Día 337 / 365
""" 
Simulador de Confianza entre Robots 
(experimental e inusual)
"""
import random

robots = {
    "R1": 70,
    "R2": 60,
    "R3": 50,
    "R4": 65
}

for ronda in range(1, 15):
    print(f"\nRonda {ronda}")
    for r in robots:
        prob_exito = robots[r] / 100
        if random.random() < prob_exito:
            robots[r] = min(100, robots[r] + random.randint(1, 5))
            print(f"{r} completó su misión. Confianza: {robots[r]}")
        else:
            robots[r] = max(1, robots[r] - random.randint(3, 8))
            print(f"{r} falló la misión. Confianza: {robots[r]}")

print("\nEstado final:")
for r, c in robots.items():
    print(f"{r}: {c}")

ganador = max(robots, key=lambda x: robots[x])
print(f"\nRobot más confiable: {ganador}")



# Día 338 / 365
# Mini-Juego: "Curación de Datos Ruidosos"

import random
import statistics
def generar_serie(n=20):
    serie = [random.randint(10, 20) for _ in range(n)]
    for _ in range(3):
        idx =random.randint(0, n-1)
        serie[idx] = random.randint(30, 60)
    
    for _ in range(2):
        idx = random.randint(0, n-1)
        serie[idx] = None
    return serie

def curar_serie(serie):
    limpia = []

    for i, v in enumerate(serie):
        if v is None:
            vecinos = []
            if i > 0: vecinos.append(serie[i-1])
            if i < len(serie)-1: vecinos.append(serie[i+1])
            v = statistics.mean([x for x in vecinos if x is not None])
        limpia.append(v)

    media = statistics.mean(limpia)
    std = statistics.pstdev(limpia)
    limpia = [media if abs(x - media) > 2*std else x for x in limpia]

    for i in range(1, len(limpia)):
        if abs(limpia[i] - limpia[i - 1]) > 7:
            limpia[i] = (limpia[i] + limpia[i-1]) / 2

    return limpia

def calificacion(serie):
    std = statistics.pstdev(serie)
    if std < 2: return "🟢 EXCELENTE"
    if std < 4: return "🟡 Aceptable"
    return "🔴 Inestable"

if __name__ == "__main__":
    original = generar_serie()
    print("Serie original ruidosa:")
    print(original)

    curada = curar_serie(original)
    print("\nSerie 'curada':")
    print([round(x,2) for x in curada])

    print("\nCalificación:", calificacion(curada))


# Día 339 / 365
# Simulador de micro-criaturas inteligentes (versión simple)

import random

def crear_criaturas(n=5):
    return [
        {"x": random.randint(0, 10),
         "y": random.randint(0, 10),
         "energia": random.randint(5, 12)}
        for _ in range(n)
    ]

def crear_comida(m=6):
    return {(random.randint(0, 10), random.randint(0, 10)) for _ in range(m)}

def mover(criatura):
    criatura["x"] += random.choice([-1, 0, 1])
    criatura["y"] += random.choice([-1, 0, 1])

def simular(ciclos=15):
    criaturas = crear_criaturas()
    comida = crear_comida()

    for c in range(ciclos):
        print(f"\n--- Ciclo {c+1} ---")
        for cr in criaturas:
            mover(cr)
            cr["energia"] -= 1

            pos = (cr["x"], cr["y"])
            if pos in comida:
                cr["energia"] += 4
                comida.remove(pos)
                print("Una criatura encontró comida!")

        criaturas = [c for c in criaturas if c["energia"] > 0]

        print("Criaturas vivas:", len(criaturas))
        if not criaturas:
            print("Todas las criaturas murieron 😢")
            break

    print("\nSimulación terminada.")

if __name__ == "__main__":
    simular()


# Día 340 / 365
# Simulador de Robots Reparadores en un Mapa Dinámico
import random

TAM = 10
TURNS = 12

def crear_mapa():
    mapa = [["." for _ in range(TAM)] for _ in range(TAM)]
    robots = [(0,0), (9,9)]
    daños = [(5,5)]

    for r in robots:
        mapa[r[1]][r[0]] = "R"
    for d in daños:
        mapa[d[1]][d[0]] = "X"

    return mapa, robots, daños

def mostrar(mapa):
    for fila in mapa:
        print(" ".join(fila))
    print()

def distancia(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def mover_robot(robot, objetivo):
    x,y = robot
    ox, oy = objetivo
    if ox > x: x += 1
    elif ox < x: x -= 1
    elif oy > y: y += 1
    elif oy < y: y -= 1
    return (x,y)

mapa, robots, daños = crear_mapa()

for turno in range(1, TURNS+1):
    mapa = [["." for _ in range(TAM)] for _ in range(TAM)]

    for i, r in enumerate(robots):
        if daños:
            objetivo = min(daños, key=lambda d: distancia(r,d))
            nuevo = mover_robot(r, objetivo)

            if nuevo == objetivo:
                daños.remove(objetivo)
            robots[i] = nuevo

    if turno % 3 == 0:
        nx, ny = random.randint(0,9), random.randint(0,9)
        daños.append((nx,ny))

    for r in robots:
        mapa[r[1]][r[0]] = "R"
    for d in daños:
        mapa[d[1]][d[0]] = "X"

    print(f"--- Turno {turno} ---")
    mostrar(mapa)



# Día 341 / 365
# Simulador de Cadena de Suministro Inteligente
import random

def simular_cadena_suministro(dias=20):
    inventario = 50
    costo_unitario = 3
    costo_total = 0

    ajuste = 0    
    dias_escasez = 0
    dias_sobra = 0
    historial_inv = []

    for d in range(1, dias+1):
        demanda = random.randint(10, 40)

    
        produccion = max(0, int((demanda + 25)/2 + ajuste))
        
        inventario += produccion
        inventario -= demanda

        costo_total += produccion * costo_unitario

        historial_inv.append(inventario)

        if inventario < 0:         
            ajuste += 2
            dias_escasez += 1
            inventario = 0
        elif inventario > 70:       
            ajuste -= 1
            dias_sobra += 1

        print(f"Día {d}: Demanda={demanda}, Prod={produccion}, Inv={inventario}, Ajuste={ajuste}")

    return costo_total, dias_escasez, dias_sobra, historial_inv


def grafico_ascii(hist):
    print("\nINVENTARIO (gráfico ASCII):")
    for v in hist:
        print(f"{v:3d} | " + "#" * (v // 2))


if __name__ == "__main__":
    costo, faltas, sobras, hist = simular_cadena_suministro()
    print("\n--- RESUMEN ---")
    print("Costo total:", costo)
    print("Días con escasez:", faltas)
    print("Días con sobreproducción:", sobras)
    grafico_ascii(hist)



# Día 342 / 365
# Simulador de crecimiento bacteriano

import random


poblacion = 1000
nutrientes = 500

for dia in range(1, 11):
    print(f"\nDía {dia}")
    temp = random.randint(30, 42) 
    crecimiento = 0.10  

    if 36 <= temp <= 38:
        crecimiento += 0.05
        print("  Temperatura óptima (+5%)")
    else:
        crecimiento -= 0.10
        print("  Temperatura desfavorable (-10%)")

    if random.random() < 0.20:
        if random.random() < 0.5:
            crecimiento += 0.05
            print("  Mutación positiva (+5%)")
        else:
            crecimiento -= 0.05
            print("  Mutación negativa (-5%)")

    poblacion = int(poblacion * (1 + crecimiento))

    consumo = poblacion // 20
    nutrientes -= consumo

    print(f"  Población: {poblacion}")
    print(f"  Nutrientes restantes: {nutrientes}")

    if poblacion < 100 or nutrientes <= 0:
        print("\n💀 La colonia colapsó.")
        break

else:
    print("\n🧬 La colonia sobrevivió los 10 días.")



# Día 343 / 365
# Mini-simulador de termostato inteligente
import random
import time

temp = float(input("Temperatura inicial: "))

for i in range(10):
    temp += random.choice(([-0.5, 0.5]))

    if temp < 20:
        accion = "Calefacción ON"
        temp += 1
    elif temp > 25:
        accion = "Aire acondicionado ON"
        temp -= 1
    else:
        accion = "Sistema en reposo"

    print(f"Ciclo {i-1}: {temp:.1f}°C - {accion}")
    time.sleep(0.4)



