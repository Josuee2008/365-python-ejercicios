#Día 183 / 365
"""
🌦️ "Consulta el clima actual 
de una ciudad con Streamlit y OpenWeather"
"""

import streamlit as st
import requests

st.title("🌤️ Consultar el clima actual")

API_KEY = "b0c944316e2afa3b8b3edb01288867ff" #Tu API key 
ciudad = st.text_input("Escribe el nombre de la ciudad")

if ciudad:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        st.subheader(f"Clima en {ciudad.title()}")
        st.write(f"🌡️ Temperatura: {datos['main']['temp']}°C")
        st.write(f"💧 Humedad: {datos['main']['humidity']}%")
        st.write(f"🌥️ Estado: {datos['weather'][0]['description'].capitalize()}")
    else:
        st.error("Ciudad no encontrada o error con la API.")


Día 184 / 365
"""
Círculo rebotador con Pygame
"""

import pygame

pygame.init()
ANCHO, ALTO = 600, 400
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("🟢 Círculo rebotador")

#Propiedades del círculo
x, y = 300, 200
radio = 20
vel_x, vel_y = 3, 2
color = (0, 200, 0)

reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    
    #Mover el círculo 
    x += vel_x
    y += vel_y

    #Rebote de los bordes
    if x - radio <= 0 or x + radio >= ANCHO:
        vel_x *= -1
    if y - radio <= 0 or y + radio >= ALTO:
        vel_y *= -1

    ventana.fill((255, 255, 255))
    pygame.draw.circle(ventana, color, (x, y), radio)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()



#Día 185 / 365
"""
Visualizador de porcentajes con Matplotlib
"""
import matplotlib.pyplot as plt

#Activadades y sus porcentajes (Puedes cambiar los valores)
actividades = ["Dormir", "Estudiar", "Ejercicio", "Redes Sociales", "Ocio"]
porcentajes = [30, 25, 10, 15, 20]

colores = ['#66b3ff', '#99ff99', '#ffcc99', '#ff9999', '#c2c2f0']

plt.pie(porcentajes, labels=actividades, colors=colores, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('¿Cómo distribuyes tu día?')
plt.show()


#Día 186 / 365
"""
Mapa interactivo con 
marcadores usando Folium
"""
import folium

# Coordenadas para centrar el mapa en Tokio, Japón
latitud = 35.6895
longitud = 139.6917

# Crear el mapa centrado en Tokio
mapa = folium.Map(location=[latitud, longitud], zoom_start=13)

# Agregar un marcador en Tokio
folium.Marker(
    location=[latitud, longitud],
    popup="Tokyo, Japan",
    tooltip="Haz clic para ver",
    icon=folium.Icon(color='blue')
).add_to(mapa)

# Guardar el mapa como archivo HTML
mapa.save("mapa_tokyo.html")
print("Mapa guardado como 'mapa_tokyo.html'")



#Día 187 / 365
"""
larma básica en Python
"""
import datetime
import time
import winsound #Solo funciona en Windows

alarma = input("Escribe la hora de la alarma (HH:MM:SS): ")

print("⏰ Esperando la hora...")

while True:
    ahora = datetime.datetime.now().strftime("%H:%M:%S")
    if ahora == alarma:
        print("¡Despierta! 🔔")
        winsound.Beep(1000, 1000) #Frecuencia, duración en ms
        break
    time.sleep(1)



#Dia 188 / 365
"""
Creador de gráficos de barras con Plotly
"""
import plotly.express as px

#DAtos de ejemplo
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"]
ingresos = [1200, 1500, 1000, 1600, 2000]

#Crear el gráfico
fig = px.bar(x=meses, y=ingresos, labels={'x': "Meses", 'y': "Ingresos ($)"}, title="Ingresos Mensuales")

#Mostrar el grafico en el navegador
fig.show()



#Día 189 / 365
"""
Juego básico: Atrapa el cuadrado (Pygame)
"""
import pygame
import random

pygame.init()
ANCHO, ALTO = 600, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("🎯 Atrapa el Cuadrado")

#Colores
NEGRO = (0, 0, 0)
AZUL = (0, 0, 225)
ROJO = (255, 0, 0)

#Jugador
jugador = pygame.Rect(300, 200, 40, 40)
velocidad = 5

#Objetico
objetivo = pygame.Rect(random.randint(0, ANCHO -30), random.randint(0, ALTO -30), 30, 30)

#Puntos
puntos = 0
fuente = pygame.font.SysFont(None, 36)

reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]: jugador.x -= velocidad
    if teclas[pygame.K_RIGHT]: jugador.x += velocidad
    if teclas[pygame.K_UP]: jugador.y -= velocidad
    if teclas[pygame.K_DOWN]: jugador.y += velocidad

    if jugador.colliderect(objetivo):
        puntos += 1
        objetivo.x = random.randint(0, ANCHO -30)
        objetivo.y = random.randint(0, ALTO -30)

    pantalla.fill(NEGRO)
    pygame.draw.rect(pantalla, AZUL, jugador)
    pygame.draw.rect(pantalla, ROJO, objetivo)

    texto = fuente.render(f"Puntos: {puntos}", True, (255, 255, 255))
    pantalla.blit(texto, (10, 10))

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
