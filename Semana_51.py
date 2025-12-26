# Día 351 / 365
# Detector simple de hábitos diarios

import random
import statistics

HORAS = 24
DIAS = 14

def simular_actividad():
    """Minutos activos por hora"""
    dias = []
    for _ in range(DIAS):
        dia = []
        for h in range(HORAS):
            if 6 <= h <= 8 or 17 <= h <= 19:  # horas activas
                dia.append(random.randint(30, 60))
            else:
                dia.append(random.randint(0, 30))
        dias.append(dia)
    return dias

def analizar_habitos(datos):
    actividad_por_hora = list(zip(*datos))
    promedio = [statistics.mean(h) for h in actividad_por_hora]

    horas_activas = [i for i, v in enumerate(promedio) if v >= 35]
    horas_pasivas = [i for i, v in enumerate(promedio) if v <= 10]

    return promedio, horas_activas, horas_pasivas

datos = simular_actividad()
promedios, activas, pasivas = analizar_habitos(datos)

print("Promedio de actividad por hora:")
for h, v in enumerate(promedios):
    print(f"{h:02d}:00 → {v:.1f} min")

print("\nHoras con hábito ACTIVO:", activas)
print("Horas con hábito PASIVO:", pasivas)



# Día 352 / 365
# La Cápsula del Tiempo Encriptada"
import time
from datetime import datetime

class CapsulaDelTiempo:
    def __init__(self, usuario, mensaje, fecha_apertura):
        self.usuario = usuario
        self.mensaje = mensaje
        self.fecha_apertura = datetime.strptime(fecha_apertura, "%Y-%m-%d")

    def intentar_abrir(self):
        ahora = datetime.now()
        
        if ahora >= self.fecha_apertura:
            print(f"\n🔓 ¡Hola {self.usuario}! El tiempo ha pasado. Aquí está tu mensaje:\n")
            for char in self.mensaje:
                print(char, end='', flush=True)
                time.sleep(0.05)
            print("\n")
        else:
            faltan = self.fecha_apertura - ahora
            print(f"🔒 Acceso denegado. Esta cápsula está sellada.")
            print(f"Vuelve en: {faltan.days} días y {faltan.seconds // 3600} horas.")

# --- Simulación del ejercicio ---
mi_mensaje = "¡Feliz Año Nuevo 2026!"
mi_capsula = CapsulaDelTiempo("TuNombre", mi_mensaje, "2026-01-01")
mi_capsula.intentar_abrir()


# Día 353 / 365
# Simulador de Caída de Copos de Nieve

import random
import time
import os 

def simulador_nieve(ancho=40, alto=20, densidad=15):
    copos = [[random.randint(0, alto -1), random.randint(0, ancho -1)] for _ in range(densidad)]

    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            pantalla = [[" " for _ in range(ancho)] for _ in range(alto)]

            for copo in copos:
                f, c = copo

                if 0 <= f < alto and 0 <= c < ancho:
                    pantalla[f][c] = "*"

                copo[0] += 1
                copo[1] = (copo[1] + random.choice([-1, 0, 1])) % ancho

                if copo[0] >= alto:
                    copo[0] = 0
                    copo[1] = random.randint(0, ancho -1)

            for fila in pantalla:
                print("".join(fila))

            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nSimulación terminada.")

if __name__ == "__main__":
    simulador_nieve()



# Día 354 / 365
# Generador Fractal de Árboles de Navidad

import random

def dibujar_arbol(n, nivel_actual=1):
    if nivel_actual > n:
        esapacio_tronco = " " * (n-1)
        print(f"{esapacio_tronco}[###]")
        print(f"{esapacio_tronco}[###]")
        return
    
    espacio = " " * (n - nivel_actual)
    hojas = ""

    for _ in range(2 * nivel_actual -1):
        if random.random() < 0.2:
            hojas += random.choice(["o", "@", "&", "★"])
        else:
            hojas += "*"

    
    print(f"{espacio}\033[32m{hojas}\033[0m")

    dibujar_arbol(n, nivel_actual + 1)

print("🎄 CONFIGURADOR DE ÁRBOL NAVIDEÑO 🎄")

try: 
    tamanio = int(input("¿De qué tamaño quieres tu árbol? (Recomendado 10-20): "))
    print("\n")
    dibujar_arbol(tamanio)
    print("\n¡Felices Fiestas!")
except ValueError:
    print("Por favor, introduce un número entero.")



# Día 355 / 365
# ¡Contador de Año Nuevo!
import time
from datetime import datetime

def cuenta_regresiva_anual():
    proximo_ano = datetime.now().year + 1
    objetivo = datetime(proximo_ano, 1, 1, 0, 0, 0)

    try: 
        while True:
            ahora = datetime.now()
            diferencia = objetivo - ahora

            if diferencia.total_seconds() <= 0:
                print("\n" + "★"  * 30)
                print(" ¡¡¡FELIZ AÑO NUEVO 2026!!! ")
                print("★" * 30)
                break

            dias = diferencia.days
            horas, residuo = divmod(diferencia.seconds, 3600)
            minutos, segundos = divmod(residuo, 60)

            print(f"Faltan: {dias}d {horas:02d}h {minutos:02d}m {segundos:02d}s", end="\r")

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nContador detenido.")

if __name__ == "__main__":
    cuenta_regresiva_anual()
# Día 356 / 365
# Algoritmo del Amigo Secreto

import random
import time

def realizar_sorteo(participantes):
    receptores = participantes[:]

    while True:
        random.shuffle(receptores)
        valido = True

        for i in range(len(participantes)):
            if participantes[i] == receptores[i]:
                valido = False
                break

        if valido:
            return list(zip(participantes, receptores))
        
def ejecutar_amigo_secreto():
    nombres = ["Ana", "Juan", "Carlos", "Lucía", "Manuel", "Elean", "Josué"]

    print("🎄 INICIANDO SORTEO DE AMIGO SECRETO 🎄")
    print("Mezclando nombre...")
    time.sleep(2)

    resultado = realizar_sorteo(nombres)

    print("\n🎁 RESULTADOS DEL SORTEO:")
    print("-" * 25)
    for dador, receptor in resultado:
        print(f"{dador:.<12} le regalata a {receptor:.>10}")
        time.sleep(0.5)

if __name__ == "__main__":
    ejecutar_amigo_secreto()



# Día 357 / 365
# Luces Navideñas
import time
import random
import os

def simulador_lueces():
    ROJO = "\033[31m"
    VERDE = "\033[32m"
    AMARILLO = "\033[33m"
    AZUL = "\033[34m"
    RESET = "\033[0m"

    colores = [ROJO, VERDE, AMARILLO, AZUL]
    iconos = ["●", "○", "★", "✴"]

    print("🎄 Iniciando serie de luces... (Presiona Ctrl+C para detener)")
    time.sleep(1)

    try:
        while True:
            linea_luces = ""
            for _ in range(20):
                color = random.choice(colores)
                icon = random.choice(iconos)

                if random.random() > 0.5:
                    linea_luces += f"{color}{icon}  "
                else:
                    linea_luces += f"{RESET}.  "
            print(f"\r{linea_luces}", end="", flush=True)

            time.sleep(0.3)

    except KeyboardInterrupt:
        print(f"{RESET}\n\n✨ Luces apagadas. ¡Felices fiestas!")

if __name__ == "__main__":
    simulador_lueces()
