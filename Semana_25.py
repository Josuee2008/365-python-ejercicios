#Día 169 / 365
"""
 "Cambia color de fondo 
 según el clima - con Flask + API"
"""
from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def clima():
    clima = random.choice(['soleado', 'lluvioso', 'nublado'])
    colores = {'soleado': '#FFD700', 'lluvioso': '#87CEFA', 'nublado': '#B0C4DE'}
    color = colores[clima]
    return f"""
    <body style="background-color:{color};">
    <h1>Clima: {clima.capitalize()}</h1>
    </body>
    """

if __name__ == '__main__':
    app.run(debug=True)


#Día 170 / 365
"""
Visualiza la frecuencia de letras en un texto 
con Streamlit + Matplotlib
"""
import streamlit as st
import matplotlib.pyplot as plt
from collections import Counter
import string

st.title("Frecuencia de Lectura 🔤:")

texto = st.text_area("Escribir un texto:")
if texto:
    letras = [c.lower() for c in texto if c.lower() in string.ascii_lowercase]
    conteo = Counter(letras)

    fig, ax = plt.subplots()
    ax.bar(conteo.keys(), conteo.values())
    ax.set_title("Frecuencias de letras")
    st.pyplot(fig)


#Día 171 / 365
"""
Contador de clicks con 
interfaz en Streamlit
"""
import streamlit as st
st.title("Contador de Clicks")

if "contador" not in st.session_state:
    st.session_state.contador = 0
if st.button("Haz click"):
    st.session_state.contador += 1

st.write(f"Has hecho click {st.session_state.contador} veces.")


#Día 172 / 365
"""
Creador de contraseñas fuertes con Flask
"""
from flask import Flask
import random, string

app = Flask(__name__)

@app.route('/')
def generar():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choices(caracteres, k=12))
    return f"<h1>Tu contraseña segura es:</h1><p>{contraseña}</p>"

if __name__ == '__main__':
    app.run(debug=True)


#Día 173 de 365
"""
Detector de números primos 
(con interfaz gráfica usando Tkinter)
"""
import tkinter as tk

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def verificar():
    num = int(entrada.get())
    resultado.set("Es primo" if es_primo(num) else "No es primo")

ventana = tk.Tk()
ventana.title("¿Es primo?")

entrada = tk.Entry(ventana)
entrada.pack()

tk.Button(ventana, text="Verificar", command=verificar).pack()
resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado).pack()

ventana.mainloop()


#Día 174 / 365
"""
“Detector de Palabras Palíndromas 
con interfaz usando Tkinter
"""
import tkinter as tk

def verificar():
    palabra = entrada.get().lower().replace(" "," ")
    if palabra == palabra[::-1]:
        resultado.set("Es un palíndromo")
    else:
        resultado.set("No es un palíndromo")

ventana = tk.Tk()
ventana.title("¿Es palíndromo?")

entrada = tk.Entry(ventana)
entrada.pack()

tk.Button(ventana, text="Verificar", command=verificar).pack()
resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado).pack()

ventana.mainloop()


#Día 175 / 365
"""
App visual para convertir 
temperaturas con Streamlit
"""
import streamlit as st

st.title("Conversor de temperatuta🌡️ ")

grados = st.number_input("Ingresa la temperatura:")
opcion = st.radio("Convertir a:", ["Celsius", "Fahrenheit"])

if opcion == "Celsius":
    convertidor = (grados -32) * 5/9
    st.write(f"{grados}°F son{convertidor:.2f}°C")
else:
    convertidor = (grados * 9/5) + 32
    st.write(f"{grados}°C son {convertidor:.2f}°F")

