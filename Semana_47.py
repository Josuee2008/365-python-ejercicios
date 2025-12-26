# Día 323 / 365
# Simulador de Reservas de un Restaurante
import random
import time

capacidad = 8               
mesas_ocupadas = []         
cliente_id = 1

print("🍽️ Simulador de Reservas del Restaurante\n")

for minuto in range(1, 16):  
    print(f"⏰ Minuto {minuto}")

    mesas_ocupadas = [(c, t-1) for (c, t) in mesas_ocupadas if t-1 > 0]

    if random.random() < 0.75:
        print(f"🧍 Cliente {cliente_id} quiere una mesa.")

        if len(mesas_ocupadas) < capacidad:
            duracion = random.randint(2, 5)
            mesas_ocupadas.append((cliente_id, duracion))
            print(f"✔ Reserva aceptada. Se quedará {duracion} min.")
        else:
            print("❌ Reserva rechazada: No hay mesas disponibles.")

        cliente_id += 1
    else:
        print("… No llegó ningún cliente.")

    print(f"Mesas ocupadas: {len(mesas_ocupadas)}/{capacidad}")
    print("-" * 40)
    time.sleep(1)

print("\n🏁 Fin de la simulación")
print(f"Mesas ocupadas al final: {len(mesas_ocupadas)}")



# Día 324 / 365 
# Detector básico de patrones
import statistics
def tendencia(serie):
    n = len(serie)
    if n < 2: return "insuficiente"
    xs = range(n)
    xm, ym = statistics.mean(xs), statistics.mean(serie)
    num = sum((x - xm)*(y - ym) for x, y in zip(xs, serie))
    den = sum((x - xm)**2 for x in xs)
    pend = num / den if den else 0
    return "sube" if pend > 0 else "baja" if pend < 0 else "estable"

def picos(serie, k=2):
    m, s = statistics.mean(serie), statistics.pstdev(serie)
    umbral = m + k*s
    return [(i, v) for i, v in enumerate(serie) if v >= umbral]

def valles(serie, k=2):
    m, s = statistics.mean(serie), statistics.pstdev(serie)
    umbral = m - k*s
    return [(i, v) for i, v in enumerate(serie) if v <= umbral]

def cambios_bruscos(serie, rel=0.2):
    r = max(serie) - min(serie) or 1
    u = r * rel
    out = []
    for i in range(1, len(serie)):
        if abs(serie[i] - serie[i-1]) >= u:
            out.append((i-1, serie[i-1], serie[i]))
    return out

def analizar(serie):
    print("Serie:", serie)
    print("Tendencia:", tendencia(serie))
    print("Picos:", picos(serie))
    print("Valles:", valles(serie))
    print("Cambios bruscos:", cambios_bruscos(serie))

if __name__ == "__main__":
    demo = [10, 12, 15, 30, 28, 26, 40, 39, 38, 10]
    analizar(demo)



# Día 325 / 365
# Monitor simple de cambios en un archivo

import time
from pathlib import Path

def monitorear(ruta, intervalo=1.0):
    ruta = Path(ruta)

    if not ruta.exists():
        print("El archivo no existe.")
        return

    ultima_mod = ruta.stat().st_mtime
    print(f"Monitoreando cambios en: {ruta}")

    while True:
        time.sleep(intervalo)
        nueva_mod = ruta.stat().st_mtime

        if nueva_mod != ultima_mod:
            print(f"[CAMBIO DETECTADO] {time.ctime(nueva_mod)}")
            ultima_mod = nueva_mod

            try:
                contenido = ruta.read_text(encoding="utf-8", errors="ignore")
                print("Contenido actualizado:")
                print("-------------------------")
                print(contenido)
                print("-------------------------\n")
            except:
                print("No se pudo leer el archivo actualizado.\n")

if __name__ == "__main__":
    archivo = input("Ruta del archivo a monitorear: ")
    monitorear(archivo)



# Día 326 / 365
# Organizador automático de archivos por tipo


import os
from pathlib import Path
import shutil


CATEGORIAS = {
    "imagenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "docs": [".pdf", ".txt", ".docx", ".md"],
    "videos": [".mp4", ".mov", ".avi"],
    "audio": [".mp3", ".wav", ".ogg"]
}

def categoria_para(ext):
    ext = ext.lower()
    for nombre, lista_ext in CATEGORIAS.items():
        if ext in lista_ext:
            return nombre
    return "otros"

def organizar(carpeta):
    carpeta = Path(carpeta)

    if not carpeta.exists():
        print("Carpeta no encontrada.")
        return

    for archivo in carpeta.iterdir():
        if archivo.is_file():
            cat = categoria_para(archivo.suffix)
            destino = carpeta / cat
            destino.mkdir(exist_ok=True)

            nuevo = destino / archivo.name
            shutil.move(str(archivo), str(nuevo))
            print(f"Movido: {archivo.name} -> {cat}/")

def main():
    ruta = input("Carpeta a organizar: ")
    organizar(ruta)

if __name__ == "__main__":
    main()


# Día 327 / 365
# Simulador de memoria volátil

import random

recuerdos = []

def agregar(texto):
    recuerdos.append({"texto": texto, "fuerza": random.uniform(0.6, 1.0)})

def decaimiento():
    olvidados = []
    for r in recuerdos[:]:
        r["fuerza"] -= random.uniform(0.05, 0.25)
        if r["fuerza"] <= 0.2:
            olvidados.append(r["texto"])
            recuerdos.remove(r)
    return olvidados

def mostrar():
    print("\n--- RECUERDOS ACTUALES ---")
    if not recuerdos:
        print("(vacío)")
    for r in recuerdos:
        print(f"- {r['texto']}  | fuerza={r['fuerza']:.2f}")

def main():
    while True:
        print("\n1) Agregar recuerdo")
        print("2) Ejecutar ciclo de decaimiento")
        print("3) Ver recuerdos")
        print("4) Salir")
        op = input("> ")

        if op == "1":
            agregar(input("Recuerdo: "))
        elif op == "2":
            olv = decaimiento()
            print("Olvidados:", olv if olv else "ninguno")
        elif op == "3":
            mostrar()
        elif op == "4":
            break

if __name__ == "__main__":
    main()



# Día 328 
# Puertas lógicas emocionales

import random

class Gate:
    def __init__(self, tipo):
        self.tipo = tipo
        self.animo = random.choice(["feliz", "neutral", "triste"])

    def procesar(self, a, b):
        if self.tipo == "AND": r = a & b
        elif self.tipo == "OR": r = a | b
        else: r = a ^ b

        # modificar según estado emocional
        if self.animo == "feliz" and random.random() < 0.3:
            r = 1
        if self.animo == "triste" and random.random() < 0.3:
            r = 0

        return r

def generar_circuito(n=5):
    tipos = ["AND","OR","XOR"]
    return [Gate(random.choice(tipos)) for _ in range(n)]

def ejecutar(circuito, a, b):
    val = (a, b)
    for g in circuito:
        val = (g.procesar(*val), random.randint(0,1))
    return val[0]

# Demostración
c = generar_circuito()
a, b = random.randint(0,1), random.randint(0,1)
print("Entrada:", a, b)
print("Ánimos:", [g.animo for g in c])
print("Salida:", ejecutar(c, a, b))



# Día 329
# Simulador básico de inversiones bursátiles
import random
class Mercado:
    def __init__(self, precio_inicial=100):
        self.precio = precio_inicial

    def mover_precio(self):
        cambio = random.uniform(-0.05, 0.05)   # ±5%
        self.precicio_anterior = self.precio
        self.precio = round(self.precio * (1 + cambio), 2)
        return self.precio

class Inversionista:
    def __init__(self, capital=1000):
        self.capital = capital
        self.acciones = 0

    def comprar(self, precio):
        if self.capital >= precio:
            self.acciones += 1
            self.capital -= precio

    def vender(self, precio):
        if self.acciones > 0:
            self.acciones -= 1
            self.capital += precio

def estrategia(precio_actual, precio_anterior):
    if precio_actual < precio_anterior * 0.97:
        return "comprar"
    elif precio_actual > precio_anterior * 1.05:
        return "vender"
    return "mantener"

def simular(dias=20):
    mercado = Mercado()
    trader = Inversionista()

    for d in range(1, dias+1):
        precio_anterior = mercado.precio
        precio = mercado.mover_precio()
        accion = estrategia(precio, precio_anterior)

        print(f"\nDía {d}: Precio = {precio} USD")

        if accion == "comprar":
            trader.comprar(precio)
            print(" → Compraste 1 acción")
        elif accion == "vender":
            trader.vender(precio)
            print(" → Vendiste 1 acción")
        else:
            print(" → Mantener")

        print(f"Acciones: {trader.acciones} | Capital: {round(trader.capital, 2)} USD")

    valor_total = trader.capital + trader.acciones * mercado.precio
    print(f"\nValor final del portafolio: {round(valor_total, 2)} USD")

if __name__ == "__main__":
    simular()

