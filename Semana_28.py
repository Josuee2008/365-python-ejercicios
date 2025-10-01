#Día 190 / 365
"""
Esquiva los meteoritos
"""
import pygame
import random

pygame.init()
ANCHO, ALTO = 500, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("🚀 Esquiva los meteoritos")

#Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

#Jugador
nave = pygame.Rect(200, 500, 50, 50)
velocidad = 6

#Meteoritos
meteoritos = [pygame.Rect(random.randint(0, ANCHO -30), -50, 30, 30 ) for _ in range(5)]
vel_meteorito = 5

reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            corriendo = False
        
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and nave.x > 0: nave.x -= velocidad
    if teclas[pygame.K_RIGHT] and nave.x < ANCHO - nave.width: nave.x += velocidad

    pantalla.fill(NEGRO)
    pygame.draw.rect(pantalla, BLANCO, nave)

    for m in meteoritos:
        m.y += vel_meteorito
        pygame.draw.rect(pantalla, ROJO, m)

        if m.y > ALTO:
            m.y = random.randint(-100, -40)
            m.x = random.randint(0, ANCHO -m.width)
        
        if nave.colliderect(m):
            pygame.quit()
            print("💥¡Perdiste! ")
            exit()

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()


#Día 191 / 365
"""
Lector de texto en voz alta con pyttsx3
"""
import pyttsx3
import logging
logging.basicConfig(level=logging.CRITICAL)


texto = input("Escribe algo para leer en voz alta: ")
voz = pyttsx3.init()
voz.say(texto)
voz.runAndWait()


# Día 193 / 365
"""
Dibuja una figura tipo mandala usando turtle
"""

import turtle
import colorsys

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("Black")
t.pensize(2)

h = 0

for i in range(36):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(c)
    t.circle(100)
    t.left(10)
    h += 0.028

turtle.done()


#Día 193 / 365
"""
🟩 Mini Pong para un jugador 
(rebotar la pelota con una barra)
"""
import pygame
import random

pygame.init()
ANCHO, ALTO = 600, 400
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mini Pong 🏓")

blanco = (255, 255, 255)
negro = (0, 0, 0)
verde = (0, 255, 0)

#Pelota
x, y = 300, 200
radio = 15
vel_x, vel_y = 3, 3

#Barra
barra_x = 250
barra_y = 350
barra_w = 100
barra_h = 10
vel_barra = 6

reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and barra_x > 0:
        barra_x -= vel_barra
    if teclas[pygame.K_RIGHT] and barra_x < ANCHO - barra_w:
        barra_x += vel_barra
    
    x += vel_x
    y += vel_y

    if x <= 0 or x >= ANCHO:
        vel_x *= -1
    if y <= 0:
        vel_y *= -1
    if y + radio >= barra_y and barra_x <= x <= barra_x + barra_w:
        vel_y *= -1
    if y > ALTO:
        x, y = 300, 200

    ventana.fill(negro)
    pygame.draw.rect(ventana, verde, (barra_x, barra_y, barra_w, barra_h))
    pygame.draw.circle(ventana, blanco, (x, y), radio)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()


#Día 194 / 365
"""
Juego de clic rápido: 
atrapa el círculo antes de que desaparezca
"""
import pygame
import random
import time

pygame.init()
ventan = pygame.display.set_mode((699, 400))
pygame.display.set_caption("¡Haz clic en el círculo! ")
reloj = pygame.time.Clock()

puntos = 0
tiempo = 10
inicio = time.time()

def nuevo_circulo():
    return random.randint(50, 550), random.randint(50, 350)

x, y = nuevo_circulo()

corriendo = True
while corriendo:
    ventan.fill((30, 30, 30))
    pygame.draw.circle(ventan, (200, 0, 0), (x, y), 30)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = evento.pos
            if (x - mouse_x) ** 2 + (y -mouse_y) ** 2 < 30 ** 2:
                puntos += 1
                x, y = nuevo_circulo()

        
    tiempo_restante = tiempo - int(time.time() - inicio)
    if tiempo_restante <= 0:
        corriendo = False

    fuente = pygame.font.SysFont(None, 36)
    texto = fuente.render(f"Puntos: {puntos} | Tiempo: {tiempo}", True, (255, 255, 255))
    ventan.blit(texto, (20, 20))

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()



#Día  195 / 365
"""
🧠 Conversor de números romanos a enteros
"""
def romano_a_entero(romano):
    valor = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    anterior = 0

    for letras in romano[::-1]:
        actual = valor[letras]
        if actual < anterior:
            total -= actual
        else:
            total += actual
        anterior = actual

    return total
    
romano = input("Ingresa un número: ").upper()
print(f"El número es: {romano_a_entero(romano)}")



#Día 196 / 365
"""
🎨 Creador de degradados con Pillow
"""
from PIL import Image

ancho, alto = 300, 300
imagen = Image.new("RGB", (ancho, alto))

for y in range(ancho):
    for x in range(ancho):
        rojo = int((x / ancho) * 225)
        azul = int((y / alto) * 225)
        imagen.putpixel((x, y), (rojo, 0, azul))

    
imagen.save("degradado.png")
print("Imagen guradada como degradado.png")

