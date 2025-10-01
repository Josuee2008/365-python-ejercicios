#Día 176 / 365
"""
Lanzador de dados animado con Turtle
"""

import turtle
import random

def dibujar_circulo(x,y):
    t.penup()
    t.goto(x, y)
    t.dot(20, "Black")
def lanzar_dado():
    t.clear()
    n = random.randint(1, 6)
    posicones = {
            1: [(0, 0)],
        2: [(-40, 40), (40, -40)],
        3: [(-40, 40), (0, 0), (40, -40)],
        4: [(-40, 40), (-40, -40), (40, 40), (40, -40)],
        5: [(-40, 40), (-40, -40), (0, 0), (40, 40), (40, -40)],
        6: [(-40, 40), (-40, 0), (-40, -40), (40, 40), (40, 0), (40, -40)],
    }
    for pos in posicones[n]:
        dibujar_circulo(*pos)

#Configuración inicial
t = turtle.Turtle()
t.hideturtle()
turtle.Screen().onclick(lambda x, y: lanzar_dado())
turtle.done()



#Día 177 / 365
"""
 “Simulador de semáforo con Tkinter
"""
import tkinter as tk
ventana = tk.Tk()
ventana.title("Simulador de Semáforo")
canvas = tk.Canvas(ventana, width=200, height=300, bg='black')
canvas.pack()

luces = {
    'red': canvas.create_oval(50,20, 150, 100, fill='gray'),
    'yellow': canvas.create_oval(50, 110, 150, 190, fill='gray'),
    'green' : canvas.create_oval(50, 200, 150, 280, fill='gray')
}

def cambiar_color():
    colores = ['red', 'yellow', 'green']
    for color in colores:
        canvas.itemconfig(luces[color], fill='gray')
    color_actual = colores[cambiar_color.estado % 3]
    canvas.itemconfig(luces[color_actual], fill=color_actual)
    cambiar_color.estado += 1
    ventana.after(1000, cambiar_color)

cambiar_color.estado = 0
cambiar_color()
ventana.mainloop()


#Día 178 / 365
"""
Controlador de pelota 
con el teclado (usando pygame)
"""
import pygame

pygame.init()
ventana = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Mover la Pelota")

x, y = 200, 200
radio = 20
velocidad = 5

reloj = pygame.time.Clock()
ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidad
    if teclas[pygame.K_RIGHT]:
        x += velocidad
    if teclas[pygame.K_UP]:
        y -= velocidad
    if teclas[pygame.K_DOWN]:
        y += velocidad
    ventana.fill((255, 255, 255))
    pygame.draw.circle(ventana,(255, 0, 0), (x, y), radio)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()



#Día 179 / 365
"""
Reproductor de Sonidos con Pygame
"""
import pygame

pygame.init()
pygame.mixer.init()

sonido = pygame.mixer.Sound("crack_glass-7177.wav")

print("Presiona ENTER para reproducir el sonido...")
input()
sonido.play()

input("Presiona ENTER para cerrar.")
pygame.quit()



#Día 180 / 365
"""
Reloj digital en vivo con Tkinter
"""

import tkinter as tk
import time

ventana = tk.Tk()
ventana.title("🕒 Reloj Digital")

etiqueta = tk.Label(ventana, font=("Arial", 48), fg="white", bg="black")
etiqueta.pack(padx=20, pady=20)

def actucalizar_reloj():
    hora_actal = time.strftime("%H:%M:%S")
    etiqueta.config(text=hora_actal)
    ventana.after(1000, actucalizar_reloj)
actucalizar_reloj()
ventana.mainloop()



#Día 181 / 360
"""
Dibuja una estrella con Turtl
"""
import turtle

pantalla = turtle.Screen()
pantalla.bgcolor("black")

estrella = turtle.Turtle()
estrella.color("yellow")
estrella.pensize(2)
estrella.speed(3)

for _ in range(5):
    estrella.forward(150)
    estrella.right(144)

turtle.done()


#Día 182 / 365
"""
🔒 Verificador de fuerza de 
contraseña con Streamlit
"""
import streamlit as st
import re

st.title("🔐 Verificador de Contraseñas")

password = st.text_input("Escribe tu contraseña", type="password")

def verificar_fuerza(pw):
    if len(pw) < 6:
        return "Debil"
    elif not re.search(r"\d", pw):
        return "Media"
    elif not re.search(r"[A-Z]", pw):
        return "Media"
    elif not re.search(r"[@$!%*?&]", pw):
        return "Media"
    else:
        return "Fuerte"
    
if password:
    fuerza = verificar_fuerza(password)
    st.success(f"Fuerza de la contraseña: {fuerza}")


    

