#Día 211
"""
Contador de Sílabas 
"""

def contar_silabas(palabra):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    cuenta = 0
    anteriror_vocal = False

    for letra in palabra:
        if letra in vocales:
            if not anteriror_vocal:
                cuenta += 1
                anteriror_vocal = True
        else:
            anteriror_vocal = False

    return cuenta

texto = input("Escribe una palabra o frase. ")
palabras = texto.split()

for palabra in palabras:
    silabas = contar_silabas(palabra)
    print(f"{palabra}: {silabas} sílabas (aproximadas)")



#Día 212 / 365
"""
Detector de idioma básico con Python 
(usando langdetect)
"""
from langdetect import detect

frase = input("Escribe una frase en cualquier idioma: ")

idioma = detect(frase)

print(f"Idioma detectado: {idioma}")



#Día 213 / 365
"""
Juego de sinónimos
"""
import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')

palabra = input("Escribe una palabra en inglés: ")

sinonimos = set()

for syn in wordnet.synsets(palabra):
    for lem in syn.lemmas():
        sinonimos.add(lem.name())

if sinonimos:
    print("Sinónimos encontrados: ")
    for s in sinonimos:
        print("-", s)

else:
    print("No se encontraron sinónimos")


#Día 214 / 365
"""
Detector de anagramas
"""

def es_anagrama(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

p1 = input("Ingresa la primera palabra: ")
p2 = input("Ingresa la segunda palabra: ")

if es_anagrama(p1, p2):
    print("¡Son Anagramas!")

else:
    print("No son anagramas")


#Día 215 / 365
"""
Simulador de Mezcla de Colores
"""
import tkinter as tk
from tkinter import colorchooser

def seleccionar_color1():
    color = colorchooser.askcolor()[1]
    if color:
        color1.set(color)
        actualizar_resultado()

def seleccionar_color2():
    color = colorchooser.askcolor()[1]
    if color:
        color2.set(color)
        actualizar_resultado()

def actualizar_resultado():
    try:
        r1, g1, b1 = ventana.winfo_rgb(color1.get())
        r2, g2, b2 = ventana.winfo_rgb(color2.get())

        r = (r1 + r2) // 2 // 256
        g = (g1 + g2) // 2 // 256
        b = (b1 + b2) // 2 // 256

        color_mezcla = f'#{r:02x}{g:02x}{b:02x}'
        resultado.config(bg=color_mezcla, text=f"Color mezclado: {color_mezcla}")

    except:
        resultado.config(text="Selecciona dos colores válidos")

ventana = tk.Tk()
ventana.title("Mezcla de Colores")
ventana.geometry("300x200")

color1 = tk.StringVar()
color2 = tk.StringVar()

tk.Button(ventana, text="Seleccionar Color 1", command=seleccionar_color1).pack(pady=5)
tk.Button(ventana, text="Seleccionar Color 2", command=seleccionar_color2).pack(pady=5)

resultado = tk.Label(ventana, text="Color mezclado", font=("Arial", 12), bg="white", width=25, height=4)
resultado.pack(pady=20)

ventana.mainloop()


#Día 216 / 365
"""
Simulador Decisiones Aleatorias
"""
import random, time

opciones = input("Escribe opciones separadas por comas: ").split(",")
print("🎡 Girando la ruleta...", end="", flush=True)
for _ in range(5):
    print(".", end="", flush=True); time.sleep(0.5)
print(f"\n✅ La decisión es: {random.choice(opciones).strip()} 🎉")



#Día 217 / 365
"""
Adivina el Emoji
"""
import random
emojis = ["😊", "😎", "🤖", "👻", "🐱", "🔥"]
elegido = random.choice(emojis)

print("Adivina qué emoji estoy pensando 🤔")
print("Opciones:", " ".join(emojis))

intento = input("Tu elección: ")

if intento.strip() == elegido:
    print("🎉 ¡Correcto! Adivinaste el emoji.")
else:
    print(f"❌ No era ese. Era {elegido}")


