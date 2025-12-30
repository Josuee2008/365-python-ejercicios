# Día 358 / 365
# Copo de nieve
import turtle

def curva_koch(t, longitud, orden):
    if orden == 0:
        t.forward(longitud)

    else:
        longitud /= 3.0
        curva_koch(t, longitud, orden - 1)
        t.left(60)
        curva_koch(t, longitud, orden - 1)
        t.right(120)
        curva_koch(t, longitud, orden - 1)
        t.left(60)
        curva_koch(t, longitud, orden - 1)

def dibujar_copo():
    pantalla = turtle.Screen()
    pantalla.bgcolor("skyblue")

    t = turtle.Turtle()
    t.speed(0)
    t.color("white")
    t.penup()
    t.goto(-150, 90)
    t.pendown()
    t.begin_fill()

    for _ in range(3):
        curva_koch(t, 300, 3)
        t.right(120)

    t.end_fill()
    t.hideturtle()
    print("¡Copo de nieve terminado!")
    pantalla.mainloop()

dibujar_copo()



# Día 359 / 365
# Simulador de Brindis Navideño
import random
import time
import sys

def brindis_navideno():
    deseos = [
        "Por la salud, el amor y los nuevos retos que vienen.",
        "Por los que están, los que se fueron y los que vendrán.",
        "Que la paz de esta noche nos acompañe todo el próximo año.",
        "Por los sueños cumplidos y los que estamos por cumplir.",
        "Brindemos por la familia, el pilar que nos mantiene unidos."
    ]

    print("🥂 PREPARANDO EL BRINDIS...")
    time.sleep(1)

    frase = random.choice(deseos)

    print("\n" + "✨" *20)

    for char in frase:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08)
    
    print("\n" + "✨" * 20)

    print("\n¡SALUD! 🥂")

if __name__ == "__main__":
    brindis_navideno()



# Día 360 / 365
# Planificación para el 2026

def planificador_metas_2026():
    print("🎯 ANALIZADOR DE METAS PARA EL AÑO 2026")
    print("Evalúa si tus objetivos son realistas y alcanzables.")

    metas = []

    while True:
        meta = input("Escsribie una meta para el próximo año (o 'fin' para ver resumen): ")
        if meta.lower() == 'fin': break

        print(f"Evaluando: '{meta}'...")
        especifica = int(input("1. ¿Qué tan específico es? (1-5): "))
        medible = int(input("2. ¿Es fácil de medir el progreso? (1-5): "))
        tiempo = int(input("3. ¿Tiene una fecha límite clara? (1-5):"))

        puntaje = (especifica + medible + tiempo) / 3
        metas.append((meta, puntaje))
        print("✅ Meta registrada.\n")
    
    print("\n" + "="*40)
    print("📊 REPORT DE VIABILIDAD")
    print("="*40)

    for m, p in metas:
        estado = "🔥 Muy viable" if p >= 4 else "⚠️ Necesta más detalle"
        print(f"- {m:<20} | Puntaje: {p:.1f}/5 | {estado}")

    print("\n Tip: Las metas con puntaje bajo necesitan una fecha o una cifra exacta.")

if __name__ == "__main__":
    planificador_metas_2026()


# Día 361 / 365
# Simulador de "Gastos de Fiesta"

def simulador_gastos_fiesta():
    print("💰 CALCULADORA DE GASTOS: FIESTA DE AÑO NUEVO")
    print("------------------------------------------")

    gastos = {}
    categoria = ["Comida", "Bebida (Jugos/Refrescos)", "Decaración",]

    for cat in categoria:
        try:
            monto = float(input(f"¿Cuanto gastaste en {cat}?: "))
            gastos[cat] = monto
        except ValueError:
            gastos[cat] = 0.0
    total = sum(gastos.values())

    if total == 0:
        print("\nNo hay gasots registrados.")
        return
    
    print("\n" + "=" * 45)
    print(f"📊 RESUMEN DE GASTOS (total: ${total:.2f})")
    print("="*45)

    for cat, monto in gastos.items():
        porcentaje = (monto / total) *100

        bloque = int(porcentaje / 5)
        barra = "█" * bloque + "░"*(20 - bloque)

        print(f"{cat:<15} | {barra} | {porcentaje:>5.1f}% (${monto:.2f})")

    print("=" * 45)
    print("💡 Tip: ¡Cigila el presupuesto de decoración para el próximo año!")

if __name__ == "__main__":
    simulador_gastos_fiesta()



# Día 362 / 365
# Cómputo Global de Medianoche
import datetime
import time
import os

def simulador_medianoche_global():
    ciudades = {
        "Tokio (Japón)": 9,
        "Madrid (España)": 1,
        "Buenos Aires (Arg)": -3,
        "Nueva York (EE.UU.)": -5,
        "Ciudad de México": -6
    }

    ano_nuevo_utc = datetime.datetime(2026, 1, 1, 0, 0, 0)

    print("🌍 MONITOR DE AÑO NUEVO GLOBAL - DÍA 362")
    print("----------------------------------------")

    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            ahora = datetime.datetime.utcnow()

            print(f"Hora Actual (UTC): {ahora.strftime('%H:%M:%S')}")
            print("=" * 45)
            print(f"{'CIUDAD':<25} | {'TIEMPO RESTANTE'}")
            print("=" * 45)

            for ciudad, offset in ciudades.items():
                ano_nuevo_local = ano_nuevo_utc - datetime.timedelta(hours=offset)

                if ahora >= ano_nuevo_local:
                    restante = "✨ ¡FELIZ AÑO NUEVO! ✨"
                else:
                    diferencia = ano_nuevo_local - ahora
                    horas, rem = divmod(diferencia.seconds, 3600)
                    minutos, segundos = divmod(rem, 60)
                    restante = f"{diferencia.days}d {horas:02d}h {minutos:02d}m {segundos:02d}s"

                print(f"{ciudad:<25} | {restante}")

            print("=" * 45)
            print("Presiona Ctrl+C para detener el monitor...")
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nMonitor finalizado. ¡Buen viaje hacia el 2026!")

if __name__ == "__main__":
    simulador_medianoche_global()



# Día 363 / 365
# Generador de Firma Digital para Regalos
import hashlib
import time

def generar_firma_regalo():
    print("🔐 SISTEMA DE REGALOS AUTÉNTICOS - DÍA 363")
    print("----------------------------------------")

    regalo = input("¿Qué regalo o deseo quiere enviar?: ")
    remitente = input("¿Quién lo envía?: ")

    datos_crudos = f"{regalo}{remitente}{time.time()}"

    firma = hashlib.sha256(datos_crudos.encode()).hexdigest()

    print("\n📦 REGALO EMAQUETADO DIGITALMENTE")
    print(f"Contenido: {regalo}")
    print(f"Enviado por: {remitente}")
    print(f"Firma de seguridad (Hash):\n👉 {firma}")

    print("\n Si cambias una solo letra del regalo, la firma cambiará por completo.")

if __name__ == "__main__":
    generar_firma_regalo()



# Día 364 / 365
# Cofre de Deseos 2026 (Manejo de JSON)
import json
import os

def cofre_de_deseos():
    archivo = "Deseos_2026.json"
    
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            deseos = json.load(f)
    else:
        deseos = []

    os.system('cls' if os.name == 'nt' else 'clear')
    print("✨ COFRE DE DESEOS - DÍA 364")
    print("-----------------------------")
    print(f"Actualmente tienes {len(deseos)} deseos guardados.\n")
    
    nuevo_deseo = input("Escribe un deseo o meta para el 2026: ")
    categoria = input("Categoría (Salud, Viajes, Código, etc.): ")

    entrada = {
        "id": len(deseos) + 1,
        "meta": nuevo_deseo,
        "categoria": categoria,
        "completado": False
    }
    
    deseos.append(entrada)

    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(deseos, f, indent=4, ensure_ascii=False)

    print("\n✅ Deseo sellado en el cofre (archivo JSON actualizado).")
    
    print("\n📋 TUS METAS ACTUALES:")
    for d in deseos:
        print(f"[{d['id']}] {d['meta']} ({d['categoria']})")

if __name__ == "__main__":
    cofre_de_deseos()
