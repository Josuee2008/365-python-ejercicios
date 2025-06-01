#Día 142 / 365
"""
 Simulador de un Sudoku
"""

import pygame
pygame.init()

tablero = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

screen = pygame.display.set_mode((450, 450))
font = pygame.font.SysFont(None, 40)
fixed = [[n != 0 for n in row] for row in tablero]
sel = [0, 0]

def dibujar():
    screen.fill((255, 255, 255))
    for i in range(9):
        for j in range(9):
            n = tablero[i][j]
            if n: screen.blit(font.render(str(n), True, (0,0,0)), (j*50+15, i*50+10))
    for i in range(10):
        pygame.draw.line(screen, (0,0,0), (0,i*50), (450, i*50), 2 if i%3==0 else 1)
        pygame.draw.line(screen, (0,0,0), (i*50,0), (i*50,450), 2 if i%3==0 else 1)
    pygame.draw.rect(screen,(255,0,0), (sel[0]*50, sel[1]*50,50,50),2)
    pygame.display.flip()

run = True
while run:
    dibujar()
    for e in pygame.event.get():
        if e.type == pygame.QUIT: run = False
        elif e.type == pygame.KEYDOWN:
            x, y = sel
            if e.key in[pygame.K_LEFT]: x = (x - 1) % 9
            if e.key in[pygame.K_RIGHT]: x = (x + 1) % 9
            if e.key in[pygame.K_UP]: y = (y - 1) % 9
            if e.key in[pygame.K_DOWN]: y = (y + 1) % 9
            sel = [x, y]
            if not fixed[y][x]:
                if pygame.K_1 <= e.key <= pygame.K_9:
                    tablero[y][x] = e.key - pygame.K_0
                elif e.key in [pygame.K_0, pygame.K_BACKSPACE, pygame.K_DELETE]:
                    tablero[y][x] = 0

pygame.quit()



#Día 143 / 365
"""
Generador de password aleatorio
"""
import random
import string

def generar_contraseña(longuitud=8):
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*"
    contraseña = ''.join(random.choice(caracteres) for _ in range(longuitud))
    return contraseña

print("¡Tu contraseña segura es!: " + generar_contraseña(10))


#Día 144 / 365
"""
 ¿Qué fecha es el día ? del año?
"""
from datetime import datetime, timedelta

def fecha_del_dia_del_año(dia_del_año, año=None):
    año = año or datetime.now().year
    fecha_inicio = datetime(año, 1,1)
    fecha_deseada = fecha_inicio + timedelta(days=dia_del_año -1)
    return fecha_deseada.strftime("%d de %B del %Y")

#Día del año
Día = 1
fecha = fecha_del_dia_del_año(Día)
print(f"📅 El día {Día} del año es: {fecha}")


#Día 145 / 365
"""
¿Cuántas horas has vivido?
"""
from datetime import datetime

def horas_vividad(fecha_naciemiento):
    nacimiento = datetime.strptime(fecha_naciemiento, "%d-%m-%Y")
    hoy = datetime.now()
    tiempo_vivido = hoy - nacimiento
    horas = int(tiempo_vivido.total_seconds() / 3600)
    return horas

Fecha_nacimiento = "15-07-2000"
horas = horas_vividad(Fecha_nacimiento)
print(f"Has vivido aproximadamente {horas:,} horas")
print(f"Equivale a:")
print(f"- {horas / 24:.0f} Días")
print(f"- {horas / 8760:.1f} años")
print(f"- {horas * 60:.0f} minutos")


#Día 146 / 365
"""
Simular 1000 lanzamientos de moneda 
y calcular la probabilidad de "cara".
"""

import random

def prob_moneda(n_lanzamientos):
    caras = sum(1 for _ in range(n_lanzamientos) if random.choice(["cara", "cruz"]) == "cara")
    return caras / n_lanzamientos

prob = prob_moneda(1000)
print(f"Probabilidad de 'cara' en 1000 lanzamientos: {prob:.2f}")


#Día 147 / 365
"""
 Calculadora de factorial
"""

#Opción 1
# 1️⃣ Método iterativo (con bucle)
def factorial_iterativo(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

#Opción 2
#2️⃣ Método recursivo
def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursivo(n - 1)

#Resultados:
num = int(input("Escribe un número: "))
print("Iterativo:", factorial_iterativo(num))
print("Recursivo:", factorial_recursivo(num))


#Día 148 / 365
"""
🧮 Cálculo de Potencias 
    con Exponenciación Rápida
"""
def potencial_rapida(base, exponente):
    resultado = 1
    while exponente > 0:
        if exponente % 2 == 1:
            resultado *= base
        base *= base
        exponente //= 2
    return resultado

print(potencial_rapida(2, 10)) #Salida 1024
