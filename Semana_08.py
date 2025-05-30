#Día 50/365
"""
Palabra Más Larga en un Texto 📚
"""

#Pedir al usuario un texto 
texto = input("Ingresar un texto: ")

#Dividir el texto en palabras
palabras = texto.split()

#Inicializar la palabra más larga
palabra_mas_larga = " "
longuitud_maxima = 0

#Recorer las palabras y encontrar la más larga
for palabra in palabras:
    if len(palabra) > longuitud_maxima:
        palabra_mas_larga = palabra
        longuitud_maxima = len(palabra)

#Mostrar el resultado 
print(f"La palabra más larga es: {palabra_mas_larga} con {longuitud_maxima} caracteres.")


#Dia 51/365
"""
Generador de Correos Electrónicos Reales 📧
"""
import random

#Pedimos al usuario su nombre y apellido 
nombre = input("Ingresa tu nombre: ").strip().lower()
apellido =  input("Ingresar tu apellido: ").strip().lower()

#Lista de dominios
dominios = ["gmail.com", "outlook.com", "yahoo.com", "icloud.com", "protonmail.com"]

#Elegir un dominio aleatorio 
dominio = random.choice(dominios)

#Generar diferentes formas de correos
opciones = [
    f"{nombre}, {apellido}@{dominio}",
    f"{nombre[0]}, {apellido}@{dominio}",
    f"{nombre}, {apellido[0]}@{dominio}",
    f"{nombre}, {random.randint(10, 99)}@{dominio}"

]



#Seleccionar una opción aleatoria
correo_generado = random.choice(opciones)

print(f"Tu correo sugerido es: {correo_generado}") #Mostrar el resultado 



#Día 52/365
"""
Generador de Código QR con Python 📱🔲
"""
#En terminal instalamos
"pip install pillow"
"pip install qrcode"

import qrcode

# Función para probar un código qr
def generar_qr(texto, nombre_archivo = "codigo_qr.png"):
    qr = qrcode.QRCode(
        version= 1, #Tamaño del código QR
        error_correction= qrcode.constants.ERROR_CORRECT_L, #Nivel de corrección de errores
        box_size=10, #Tamaño de cada píxel
        border=4 #Borde del QR
    )
    qr.add_data(texto) #Agregar información al QR
    qr.make(fit=True) #Ajustar tamño automáticamente

    
    #Crear imagen del código qr
    imagen_qr = qr.make_image(fill = "black", back_color = "white")
    imagen_qr.save(nombre_archivo) #Guardar la imagen

    print(f"Codigo QR generado y guardado como '{nombre_archivo}'")


#Solicitar información al usuario 
texto_qr = input("Ingresar el texto o enlace para generar el código QR: ")
generar_qr(texto_qr)


#Día 54/365
"""
uego de "Piedra, Papel o Tijera" 
contra la computadora
"""
import random

def juego():
    opciones = ["piedra", "papel", "tijera"]
    print("Bienvenido al jugo de Piedra, Papel o Tijera.")
    print("Escribe 'salir' para terminar el juego.")

    while True:
        jugador = input("\nElegir piedra, papel, tijera: ").lower()

        if jugador == "salir":
            print("¡Gracias por jugar!")
            break

        if jugador not in opciones:
            print("Opción no valida. Intenta de nuevo.")
            continue
        computadora = random.choice(opciones)
        print(f"La computadora eligió: {computadora}")

        if jugador == computadora:
            print("¡Es un empate!")
        elif (jugador == "piedra" and computadora == "Tijera" ) or \
            (jugador == "papel" and computadora == "piedra") or \
            (jugador == "tijera" and computadora == "papel"):
            print("¡Ganaste!")
        else:
            print("Perdiste ...:(")
#Iniciar el jugo 
juego()


#Día 54/365
"""
Convertir Dólares a Pesos MXN 💵
"""
def convertir_dolares_a_pesosmx():
    #Tasa de conversión(1 USD = 17.05 MXN)
    tasa_peso_mx = 17.05

    #Pedir la cantidad en dólares
    dolares = float(input("Ingresar la cantidad en dólares (USD): "))

    #Convertir a pesos mexicanos
    pesos = dolares * tasa_peso_mx

    #Mostrar resultado 
    print(f"\n${dolares:.2f} USD equivale a {pesos:.2f} MXN.")

#Ejecutar el convertidor
convertir_dolares_a_pesosmx()


#Día 56/365
"""
Encontrar el número que falta 
en una secuencia del 1 al 5
"""

def numero_faltante(lista):
    n = len(lista) + 1 #El tamaño correcto de la secuencia
    conjunto_completo = set(range(1, n + 1)) #Conjunto esperado (1,2,3,....,5)
    conjunto_lista = set(lista) #Conjunto de los números en lista
    return(conjunto_completo - conjunto_lista).pop() #Diferencia de conjuntos
#Ejemplo de uso 
numeros = [1,2,3,5]
print("El número faltante es:", numero_faltante(numeros))

