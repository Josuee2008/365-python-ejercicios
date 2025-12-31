# Día 365 - EL GRAN FINAL
import random
import time
import os

def animar_fuegos():
    COLORES = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]
    RESET = "\033[0m"
    BOLD = "\033[1m"

    ancho, alto = os.get_terminal_size()

    EXPLOSIONES = [
        ["  * ", "***", "  * "],
        [" \ | / ", "-- * --", " / | \ "],
        ["  o O o  ", "O  * O", "  o O o  "]
    ]

    try:
        for _ in range(5):
            col_cohete = random.randint(10, ancho - 10)
            color = random.choice(COLORES)

            for fila in range(alto - 2, alto // 4, -1):
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\n" * fila + " " * col_cohete + color + "▲" + RESET)
                time.sleep(0.03)

            diseno = random.choice(EXPLOSIONES)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n" * (alto // 4))
            for linea in diseno:
                print(" " * (col_cohete - 3) + color + BOLD + linea + RESET)
            print(f"\n" + " " * (col_cohete - 2) + color + "✨ ¡BOOM! ✨" + RESET)
            time.sleep(0.6)

# 2. MENSAJE FINAL
        os.system('cls' if os.name == 'nt' else 'clear')
        agradecimiento = f"""
{BOLD}{COLORES[2]}=================================================
          🏆 RETO 365 DÍAS COMPLETADO 🏆
================================================={RESET}

{BOLD} ¡GRACIAS A TODOS POR HABERME APOYADO EN ESTE VIAJE! {RESET}

 A quienes me siguieron, comentaron y aprendieron
 conmigo: este logro es tanto mío como de ustedes.

 Hoy cerramos un ciclo que duró todo un año.
            "¡GRACIAS POR TODO!"
            
 {COLORES[5]}¡FELIZ AÑO NUEVO 2026 Y GRACIAS POR ESTAR HASTA EL FINAL! {RESET}
================================================="""

        print(agradecimiento)
        input("\nPresiona Enter para cerrar el ciclo...")

    except KeyboardInterrupt:
        print(f"\n{RESET}¡Gracias por seguirme!")

if __name__ == "__main__":
    animar_fuegos()
