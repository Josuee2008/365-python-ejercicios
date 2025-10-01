#Día 204 / 365
"""
Juego del Número Cambiante
"""
import tkinter as tk
import random

running = True

def cambiar_numero():
    if running:
        numero = random.randint(1, 9)
        etiqueta.config(text=str(numero))
        ventana.after(300, cambiar_numero)

def verificar():
    global running
    if etiqueta.cget('text') == '7':
        running = False
        resultado.config(text="🎉 ¡Ganaste!", fg="green")
    else:
        resultado.config(text="❌ Sigue intentando", fg="red")

ventana = tk.Tk()
ventana.title("Número Cambiante")

etiqueta = tk.Label(ventana, text="0", font=("Arial", 60))
etiqueta.pack()

tk.Button(ventana, text="¡Detener!", command=verificar).pack()
resultado = tk.Label(ventana, text="", font=("Arial", 14))
resultado.pack(pady=10)

cambiar_numero()
ventana.mainloop()


#Día 205 / 365
"""
Mini juego de reflejos en la terminal 
"""
import random
import time
import msvcrt

notas = ["A", "S","D", "F"]
print("Presiona la tecla que aparezca lo más rapido posiblo.")

puntuacion = 0

for _ in range(10):
    nota = random.choice(notas)
    print(f"\n¡Pulsar: {nota}!")
    start = time.time()

    while True:
        if msvcrt.kbhit():
            tecla = msvcrt.getch().decode("utf-8").upper()
            duracion = round(time.time() - start, 2)
            if tecla == nota:
                print(f"✔️ Bien hecho ({duracion}s)")
                puntuacion += 1

            else:
                print(f"❌ Fallaste. Era {nota}, no {tecla}")
            break
        if time.time() - start > 2:
            print("⏰ ¡Muy lento!")
            break

    
print(f"\n🎯 Puntuación final: {puntuacion}/10")



#Día 206 / 365
"""
Detecta si hay letras repetidas consecutivas
en una palabra ingresada por el usuario
"""

palabra = input("Escribe una palabra: ").lower()
repetidas = []

for i in range(len(palabra)-1):
    if palabra[i] == palabra[i + 1]:
        repetidas.append(palabra[i])

if repetidas:
    print("Letras repetidas consecutivas:", ", ".join(set(repetidas)))
else:
    print("No hay letras repetidas consecutivas")


#Día 207 / 365
"""
Generador de Paleta de Colores Aleatoria    
""" 
import tkinter as tk
import random

def generar_color():
    return f'#{random.randint(0, 0xFFFFFF):06x}'

def mostrar_colores():
    for i in range(5):
        color = generar_color()
        cuadro = tk.Label(frame, bg=color, width=20, height=5)
        cuadro.grid(row=0, column=i)
        etiquetas[i].config(text=color)

ventana = tk.Tk()
ventana.title("Paleta de Colores")

frame = tk.Frame(ventana)
frame.pack(pady=10)

etiquetas = [tk.Label(ventana,text="") for _ in range(5)]
for i, etiqueta in enumerate(etiquetas):
    etiqueta.pack(side="left", padx=10)

boton = tk.Button(ventana, text="Generar paleta", command=mostrar_colores)

boton.pack(pady=10)

ventana.mainloop()



# Día 208 / 365
"""
Calendario visual interactivo usando tkcalendar
"""
import tkinter as tk
from tkcalendar import Calendar

ventana = tk.Tk()
ventana.title("📅 Calendario Visual")
ventana.geometry("300x300")

cal = Calendar(ventana, selectmode='day', date_pattern='dd/mm/yyyy')
cal.pack(pady=20)

def mostrar_fecha():
    fecha = cal.get_date()
    resultado.config(text=f"Has seleccionado: {fecha}")

tk.Button(ventana, text="Mostrar Fecha", command=mostrar_fecha).pack()
resultado = tk.Label(ventana, text="")
resultado.pack(pady=10)

ventana.mainloop()


#Día 209 / 365
"""
Contador regresivo de 5 segundos
"""

import time

print("Contador regresivo:")
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

print("¡Tiempo terminado!")



#Día 210 / 365
"""
Contador de dígitos numéricos en una frase
"""

frase = input("Escribe una frase: ")
contador = 0

for caracter in frase:
    if caracter.isdigit():
        contador += 1

print(f"Digitos encontrados: {contador}")
