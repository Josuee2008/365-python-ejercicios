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



