#Día 162 / 365
"""
Suma solo los números positivos
en una lista dada por el usuario
"""
numeros = input("Ingresa números separados por comas: ")
lista = [int(n) for n in numeros.split(',')]
suma_positivo = sum(n for n in lista if n > 0)
print(f"Suma de positivos: {suma_positivo}")


# Día 163 / 365
"""
Elimina los espacios duplicados
de una frase escrita por el usuario
"""
frase = input ("Ingresa una frase con espacios duplicados: ")
resultado =" ".join(frase.split())
print ("Frase corregida: ", resultado)


# Día 164 / 365
"""
Detecta si una palabra tiene letras
repetidas 
"""

palabra = input("Escribe una palabra: ").lower()
letras_vistas = set()
repetida = False

for letra in palabra:
    if letra in letras_vistas:
        repetida = True
        break
    letras_vistas.add(letra)

if repetida:
    print("La palabra tiene letras repetidas")
else:
    print("Todas las letras son únicas")


#Día 165 / 365
"""
página web que diga “Hola Mundo” 
usando solo Python con el microframework Flask.
"""

from flask  import Flask

app = Flask(__name__)

@app.route('/')
def hola():
    return '<h1>Hola Mundo desde Python 🐍</h1>'

if __name__ == '__main__':
    app.run(debug=True)


#Día 166 / 365
"""
"Crea una app visual que 
cuente palabras con Streamlit"
"""

import streamlit as st

st.title("Contador de Palabras 📝")

texto = st.text_area("Escribe algo aquí:")

if texto:
    palabras = texto.split()
    total = len(palabras)
    st.write(f"Has escrito **{total}** palabras")

#Día 167 / 365
"""
Conversor de texto a voz con Python
"""

import streamlit as st
import pyttsx3

st.title("🗣️ Conversor de Texto a Voz")
st.write("Escribe algo y haz clic en el botón para escucharlo en voz alta.")

texto = st.text_area("Ingresar el texto aquí:")

if st.button("🔊 Reproducir"):
    if texto.strip() != "":
        engine = pyttsx3.init()
        engine.say(texto)
        engine.runAndWait()
        st.success("✅ Texto leído en voz alta.")
    else:
        st.warning("⚠️ Por favor escribe algo.")


#Día 168 / 365
"""
Calculadora Web Simple con Streamlit
"""
import streamlit as st

st.title("Calculadora Simple")

num1 = st.number_input("Número 1")
num2 = st.number_input("Número 2")
operacion = st.selectbox("Operacion", ["Sumar", "Restar", "Multiplicar", "Dividir"])

if st.button("Calcular"):
    if operacion == "Sumar":
        st.write("Resultado:", num1 + num2)
    elif operacion == "Restar":
        st.write("Resultado:", num1 - num2)
    elif operacion == "Multiplicar":
        st.write("Resultado:", num1 * num2)
    elif operacion == "Dividir":
        if num2 != 0:
            st.write("Resultado:", num1/num2)
        else:
            st.write("No se puede dividir por cero")
