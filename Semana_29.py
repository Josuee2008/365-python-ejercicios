#Día 197 / 365
"""
Generador de notas musicales con winsound (Windows)
"""

import winsound
import time


#Diccionario de notas musicales y su fracuencia en HZ
notas = {
    "C": 261,
    "D": 294,
    "E": 329,
    "F": 349,
    "G": 392,
    "A": 440,
    "B": 493

}

#Lista con una pequeña melodía
melodia = ["C", "E", "G", "E", "C"]

print("🎵 Reproduciendo melodía...")
for nota in melodia:
    winsound.Beep(notas [nota], 400) #400 milisegundos
    time.sleep(0.1)


#Día 198 / 365 
"""
Lienzo interactivo para 
dibujar con el mouse (Tkinter)
"""
import tkinter as tk

ventana = tk.Tk()
ventana.title("Lienzo de dibujo 🎨")

lienzo = tk.Canvas(ventana, width=400, height=400, bg="white")
lienzo.pack()

def dibujo(event):
    x, y = event.x, event.y
    lienzo.create_oval(x-2, y-2, x+2, y+2, fill="black")

lienzo.bind("<B1-Motion>", dibujo)

ventana.mainloop()


#Día 199 / 365
"""
Círculo que sigue al mouse con Pygame
"""

import pygame

ventana = pygame.display.set_mode((400, 300))
pygame.display.set_caption("🟢Sigue al mause")


color_fondo = (30, 30, 30)
color_circulo = (0, 255, 0)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        x, y = pygame.mouse.get_pos()

    
    ventana.fill(color_fondo)
    pygame.draw.circle(ventana, color_circulo, (x, y), 20)
    pygame.display.flip()


#Día 200 / 365
"""
Calculadora de Probabilidad Básica
"""

def calculadora_probabilidad(favorables, posibles):
    if posibles == 0:
        return "❌ No se puede dividir entre cero"
    probabilidad = (favorables/posibles) *100
    return f"La probabilidad de que ocurra el evento es: {probabilidad:.2f} %"

#Entrada del ususario
f = int(input("Ingresa los casos favorables: "))
p = int(input("Ingresa los casos posibles: "))

print(calculadora_probabilidad(f, p))


#Día 201/365
"""
Programa que le pregunte al usuario 
por sus actividades diarias
Y genera un grafico con matplotlib
"""
import matplotlib.pyplot as plt

print("📅 ¿Qué actividades realizas en tu día y cuánto tiempo dedicas a cada una (en horas)?")
actividades = []
tiempos = []

while True:
    actividad = input("✏️ Actividad (o escribe 'fin' para terminar): ")
    if actividad.lower() == "fin":
        break

    try:
        tiempo = float(input(f"⏱️ Horas dedicadas a {actividad}: "))
        actividades.append(actividad)
        tiempos.append(tiempo)

    except ValueError:
        print("❌ Ingresa un número válido")

#Colores personalizados para cada barra
colores = plt.cm.viridis(range(len(actividades)))

plt.figure(figsize=(10, 6))
plt.bar(actividades, tiempos, color=colores)
plt.xlabel("Actividades")
plt.ylabel("Horas")
plt.title("Distribución del tiempo diario ⏰")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


#Día 202 / 365
"""
Cronómetro básico
"""
import time

input("Presiona Enter para iniciar el cronómetro...")
inicio = time.time()

input("Presiona Enter para detener el cronómetro...")
fin = time.time()

tiempo_transcurido = fin - inicio
print(f"Timpo transcurrido: {tiempo_transcurido:.2f} segundos")


#Día  203 / 365
"""
 Simulador de recibo de compra 
"""

productos = []
precios = []

while True:
    nombre = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    try:
        precio = float(input(f"Ingrese el precio de {nombre}: "))
        productos.append(nombre)
        precios.append(precio)
    except ValueError:
        print("Precio inválido. Intente nuevamente.")

subtotal = sum(precios)
iva = subtotal * 0.15
total = subtotal + iva

print("\n🧾 Recibo de compra:")
for i in range(len(productos)):
    print(f"- {productos[i]}: ${precios[i]:.2f}")

print(f"\nSubtotal: ${subtotal:.2f}")
print(f"IVA (15%): ${iva:.2f}")
print(f"Total: ${total:.2f}")

pago = float(input("\nIngrese el monto pagado: "))
cambio = pago - total

if cambio < 0:
    print("⚠️ Pago insuficiente.")
else:
    print(f"Cambio: ${cambio:.2f}")
    print("✅ Gracias por su compra.")
