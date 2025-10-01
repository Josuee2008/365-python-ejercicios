#Día 218 / 365
"""
 Contador de letras mayúsculas y minúsculas
"""

texto = input("Ingresa un texto: ")

mayuscula = 0
minuscula = 0

for caracter in texto:
    if caracter.isupper():
        mayuscula += 1
    elif caracter.islower():
        minuscula += 1

print("mayusculas:", mayuscula)
print("Minusculas:", minuscula)


#Día 219 / 365
"""
Contador de números positivos, 
negativos y ceros en una lista
"""
def contar_numeros(lista):
    postivos = 0
    negativos = 0
    ceros = 0

    for num in lista:
        if num > 0:
            postivos += 1

        elif num < 0:
            negativos += 1
        else:
            ceros +=1

    return postivos, negativos, ceros

#Ejemplo de uso
numeros = [3, -1, 0, 7, -5, 0, 2, -8]
pos, neg, cer = contar_numeros(numeros)

print(f"Positivos: {pos}")
print(f"Negativos: {neg}")
print(f"Ceros: {cer}")


#Día 220 / 365
"""
 Detector de sílabas repetidas en una palabra
"""

def detector_silabas(palabra):
    palabra = palabra.lower()
    repeticiones = {}

    for i in range(len(palabra) -1):
        silabas = palabra[i:i+2]
        repeticiones[silabas] = repeticiones.get(silabas, 0) + 1

    repetidas = {s: c for s,c in repeticiones.items() if c > 1}

    if repetidas:
        for silaba, veces in repetidas.items():
           print(f'Sílabas repetidas: "{silaba}" → {veces} veces')

    else:
        print("No hay sílabas repetidas")

palabra = input("Ingresa una palabra: ")
detector_silabas(palabra)


#Día 221 / 365
"""
 Detector de letras consecutivas repetidas
"""
def detectar_letras_conseccutivas(texto):
    texto = texto.lower()
    contador = 1

    for i in range(1, len(texto)):
        if texto[i] == texto[i - 1]:
            contador += 1

        else:
            if contador > 1:
                print(f'letra "{texto[i - 1]}" repetida {contador} veces seguidas')
            contador = 1
    if contador > 1:
        print(f'Letra "{texto[-1]}" repetida {contador} veces seguidas')

texto_usuario = input("Ingresa una palabra o frase: ")
detectar_letras_conseccutivas(texto_usuario)



#Día 222 / 365
"""
Juego de reacción visual con letras
"""
import random
import time
import msvcrt

puntos = 0
vidas = 3
velocidad = 1.5

print("Bienvenido al juego...")
print("Presiona la letra que aparezca en pantalla antes de que se termine el timpo")
print("¡Listo!, Pulsa cualquier tecla para comenzar...")
msvcrt.getch()

while vidas > 0:
    Letras = random.choice("abcdefghijklmnopqrstuvwxyz")
    print(f"\nLetra: {Letras.upper()} | Tiempo: {velocidad:.2f}s")
    inicio = time.time()
    teclado_presionado = None

    while time.time() - inicio < velocidad:
        if msvcrt.kbhit():
            teclado_presionado = msvcrt.getch().decode().lower()
            break
    if teclado_presionado == Letras:
        puntos += 1
        velocidad = max(0.4, velocidad - 0.05)
        print(f"¡Bien! Putnos: {puntos}")
    else:
        vidas -= 1
        print(f"Fallaste. vidas restantes: {vidas}")

print("\nJuego terminado")
print(f"total de puntos: {puntos}")



#Día 223 / 365
"""
    Juego de Memoria
"""
import random
import time
import os

ronda = 1

while True:
    secuencia = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(ronda))

    print(f"\nRonda {ronda} - Memoriza esto:")
    print(secuencia)

    time.sleep(max(1, 3 - ronda * 0.2))

    os.system('cls' if os.name == 'nt' else 'clear')

    respuesta = input("Escribe la secuencia: ").strip().upper()

    if respuesta == secuencia:
        print("✅ ¡Correcto!")
        ronda += 1

    else:
        print(f"❌ Fallaste. La secuencia era: {secuencia}")
        break



#Día 224 / 365
"""
Juego de Ordenar las Palabras
"""
import random
import time
import os

#Lista de palabras
palabras = ["python", "teclado", "pantalla", "juego", "programa", "ventana", "internet", "codigo"]

puntaje = 0
tiempo_limite = 5

while True:
    palabra = random.choice(palabras)
    desorden = ''.join(random.sample(palabra, len(palabra)))

    print(f"\nAdivina la palabra: {desorden}")
    inicio = time.time()
    respuesta = input("Tu respuesta: ")
    fin = time.time()

    if fin - inicio > tiempo_limite:
        print("Timepo agotado")
        break
    if respuesta.lower() == palabra:
        puntaje += 1
        print("¡Correcto!")
        tiempo_limite = max(2, tiempo_limite - 0.5)
    else:
        print(f"Incorrecto. Era: {palabra}")
        break

print(f"\nJuego terminado. Puntuación final: {puntaje}")
