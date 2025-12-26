# Día 330 
# Simulador simple de robot limpiador inteligente


import random

class Habitación:
    def __init__(self, ancho=10, alto=10, basura_prob=0.12):
        self.ancho = ancho
        self.alto = alto
        self.grid = [[random.random() < basura_prob for _ in range(ancho)] for _ in range(alto)]

    def hay_basura(self, x, y):
        return self.grid[y][x]

    def limpiar(self, x, y):
        self.grid[y][x] = False

class Robot:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.mapa_calor = {}   # lugares donde suele haber basura

    def mover(self, ancho, alto):
        # Movimiento con ligera preferencia hacia zonas "sucias"
        if self.mapa_calor and random.random() < 0.3:
            self.x, self.y = random.choice(list(self.mapa_calor.keys()))
        else:
            self.x = max(0, min(ancho-1, self.x + random.choice([-1, 0, 1])))
            self.y = max(0, min(alto-1, self.y + random.choice([-1, 0, 1])))

    def recordar(self, pos):
        self.mapa_calor[pos] = self.mapa_calor.get(pos, 0) + 1

def simular(pasos=30):
    room = Habitación()
    robot = Robot()

    for p in range(1, pasos+1):
        robot.mover(room.ancho, room.alto)
        pos = (robot.x, robot.y)

        if room.hay_basura(*pos):
            print(f"Paso {p}: Basura encontrada en {pos} → limpiando")
            room.limpiar(*pos)
            robot.recordar(pos)
        else:
            print(f"Paso {p}: Sin basura en {pos}")

    print("\nZonas visitadas frecuentemente sucias (mapa de calor):")
    for zona, veces in sorted(robot.mapa_calor.items(), key=lambda x: -x[1]):
        print(f"{zona}: {veces} veces")

if __name__ == "__main__":
    simular()



# Día 331 
# Simulador de cola de atención con prioridades

import random
import heapq

class Cliente:
    def __init__(self, id):
        self.id = id
        self.prioridad = random.randint(1, 5)          # 1 = alta urgencia, 5 = baja
        self.tiempo_atencion = random.randint(2, 8)
        self.limite_espera = random.randint(5, 20)
        self.espera = 0

    def __lt__(self, other):
        return self.prioridad < other.prioridad

def simular(minutos=40):
    cola = []   # heap de prioridades
    atendiendo = None
    tiempo_restante = 0
    id_cliente = 1

    for minuto in range(1, minutos + 1):
        # llegan clientes al azar
        if random.random() < 0.3:
            c = Cliente(id_cliente)
            id_cliente += 1
            heapq.heappush(cola, c)
            print(f"[{minuto}] Llega cliente {c.id} (prio {c.prioridad})")

        # si no hay nadie siendo atendido, tomar el siguiente por prioridad
        if atendiendo is None and cola:
            atendiendo = heapq.heappop(cola)
            tiempo_restante = atendiendo.tiempo_atencion
            print(f"[{minuto}] → Atendiendo cliente {atendiendo.id}")

        # procesar atención
        if atendiendo:
            tiempo_restante -= 1
            if tiempo_restante == 0:
                print(f"[{minuto}] ✓ Cliente {atendiendo.id} atendido")
                atendiendo = None

        # incrementar espera de los que están en cola
        restantes = []
        while cola:
            c = heapq.heappop(cola)
            c.espera += 1
            if c.espera > c.limite_espera:
                print(f"[{minuto}] ✗ Cliente {c.id} se va por demora")
            else:
                restantes.append(c)
        for c in restantes:
            heapq.heappush(cola, c)

    print("\nSimulación terminada.")

if __name__ == "__main__":
    simular()



# Dia 332 / 365
# Simulador de flujo de agua en red de tuberías
tuberias = {
    "T1": {"cap": 10, "abierta": False},
    "T2": {"cap": 15, "abierta": False},
    "T3": {"cap": 7,  "abierta": False},
    "T4": {"cap": 20, "abierta": False},
    "T5": {"cap": 12, "abierta": False},
}

def mostrar_tuberias():
    print("\nEstado de tuberías:")
    for t, info in tuberias.items():
        estado = "ABIERTA" if info["abierta"] else "cerrada"
        print(f"{t} - Capacidad: {info['cap']} L/s - {estado}")

def abrir_tuberia(nombre):
    if nombre not in tuberias:
        print("Tubería inexistente.")
    elif tuberias[nombre]["abierta"]:
        print("Ya estaba abierta.")
    else:
        tuberias[nombre]["abierta"] = True
        print(f"{nombre} abierta.")

def cerrar_tuberia(nombre):
    if nombre not in tuberias:
        print("Tubería inexistente.")
    elif not tuberias[nombre]["abierta"]:
        print("Ya estaba cerrada.")
    else:
        tuberias[nombre]["abierta"] = False
        print(f"{nombre} cerrada.")

def calcular_flujo():
    flujo = sum(info["cap"] for info in tuberias.values() if info["abierta"])
    cap_total = sum(info["cap"] for info in tuberias.values())
    por = (flujo / cap_total) * 100
    
    
    print(f"\nFlujo total: {flujo} L/s {por:.1f}%")


    if por < 30:
        print("Estado: Flujo bajo.")
    elif por < 70:
        print("Estado: Flujo estable.")
    else:
        print("Estado: ¡Flujo al máximo! Precaución.")

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Mostrar tuberías")
        print("2. Abrir tubería")
        print("3. Cerrar tubería")
        print("4. Calcular flujo")
        print("5. Salir")

        op = input("Opción: ")

        if op == "1":
            mostrar_tuberias()
        elif op == "2":
            abrir_tuberia(input("Nombre: ").upper())
        elif op == "3":
            cerrar_tuberia(input("Nombre: ").upper())
        elif op == "4":
            calcular_flujo()
        elif op == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

menu()


# Día 333 / 365
# Mini-Sistema de Inventario con alerta de consumo rápido

import random

inventario = {
    "manzanas": 30,
    "bananas": 25,
    "naranjas": 40
}

def consumir():
    fruta = random.choice(list(inventario.keys()))
    cantidad = random.randint(1, 6)
    inventario[fruta] -= cantidad
    print(f"Consumo registrado: {cantidad} {fruta}")

def verificar_alertas():
    for fruta, cant in inventario.items():
        if cant <= 0:
            print(f"⚠ {fruta} agotadas. Reabesteciendo a 20.")
            inventario[fruta] = 20
        elif cant < 10:
            print(f"⚠ {fruta} por agotarse (quedan {cant}).")

for _ in range(10):
    consumir()
    verificar_alertas()

print("\nInventario final:", inventario)


# Día 334 / 365
# Simulador de reacciones en cadena entre nodos conectados

import random
def crear_red(n = 10, prob = 0.3):
    red = {}
    for i in range(n):
        conexiones = [j for j in range(n) if j != i and random.random() < prob]
        red[i] = conexiones
    return red

def propagar(red, inicio):
    activados = set([inicio])
    cola = [inicio]

    while cola:
        actual = cola.pop(0)
        for vecino in red[actual]:
            activados.add(vecino)
            cola.append(vecino)
        return activados
    
if __name__ == "__main__":
    red = crear_red(n=12, prob=0.25)
    inico = random.randint(0, 11)
    resultado = propagar(red, inico)

    print("Red generada:")
    for k, v in red.items():
        print(f"{k} -> {v}")
    
    print("\nNodo inicial:", inico)
    print("Nodos activados en cadena:", sorted(resultado))




# Día 335 / 365
# Simulador de Sensores Inteligentes (Mini-IoT)
import random
class Sensor:
    def __init__(self, nombre, valor_inicial):
        self.nombre = nombre
        self.valor = valor_inicial
    
    def leer(self):
        # Ruido aleatorio
        self.valor += random.uniform(-1, 1)
        return self.valor

def detectar_y_corregir(sensores, umbral=3):
    lecturas = [s.valor for s in sensores]
    prom = sum(lecturas) / len(lecturas)
    
    for s in sensores:
        if abs(s.valor - prom) > umbral:
            print(f"⚠ Sensor '{s.nombre}' desviado → Corrigiendo…")
            s.valor = prom  # autocorrección por consenso

def mostrar(sensores):
    for s in sensores:
        print(f"{s.nombre}: {s.valor:.2f}")
    print("—"*30)

if __name__ == "__main__":
    sensores = [
        Sensor("Temp", 25),
        Sensor("Humedad", 50),
        Sensor("Presión", 1000)
    ]

    for _ in range(10):
        print("Lecturas:")
        for s in sensores:
            s.leer()
        detectar_y_corregir(sensores)
        mostrar(sensores)



# Día 336 / 365
""" 
Smula pequeñas "páginas web" que compiten 
por atención de usuarios
"""
import random

sitios  = {
    "TechNews": {"atractivo": 50, "visitas": 0},
    "Game.com": {"atractivo": 40, "visitas": 0},
    "EcoLife": {"atractivo": 35, "visitas": 0},
    "Youtube": {"atractivo": 40, "visitas": 0},  
}

for dia in range(1, 11):
    print(f"\nDía {dia}")
    for sitio in sitios:
        cambio = random.randint(-10, 10)
        sitios[sitio]["atractivo"] = max(1, sitios[sitio]["atractivo"] + cambio)

    for _ in range(200):
        total = sum(s["atractivo"] for s in sitios.values())
        r = random.uniform(0, total)
        acc = 0
        for nombre, datos in sitios.items():
            acc += datos["atractivo"]
            if r <= acc:
                datos["visitas"] += 1
                break

print("\nResultados finales:")
for s, d in sitios.items():
    print(f"{s}: {d['visitas']} visitas")



