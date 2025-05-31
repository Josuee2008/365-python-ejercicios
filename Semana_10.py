#Día 64/365
"""
 Primeros 10 números de Fibonacci
"""

class fibonacci_generador:
    def __init__(self):
        self.a = 1
        self.b = 1
    def __iter__(seft):
        return seft
    
    def __next__(self):
        resultado = self.a
        self.a, self.b = self.b, self.a + self.b
        return resultado 
#Ejemplo de uso 
print("Primeros 10 números de Fibonacci: ")
fib_gen = fibonacci_generador()
for i in range(10):
    print(next(fib_gen))


#Día 65/365
"""
Autocompletado de palabras. 
"""

def autocompletar(prefijo, lista_palabras):
    #Filtrar las palabras que empiezan con el prefijo(ignorando mayusculas y minisculas)
    sugerencia = [palabra for palabra in lista_palabras if palabra.lower().startswith(prefijo.lower())]
    return sugerencia if sugerencia else["No hay coincidencias"]
#Lista de palabras predefinidas
palabras = ["Python", "Pygame", "Programación", "Panda", "Parámetro"]

#solicitar prefijo al usuario
entrada = input("Ingresa un prefijo para autocompletar: ")
sugerencia = autocompletar(entrada, palabras)

#Mostrar resultados
print("Sugerenciad:", ",".join(sugerencia))

#Día  66/365
"""
Generador de patrones geométricos
 usando matplotlib
"""

import matplotlib.pyplot as plt
import numpy as np

def crear_patron_geometrico(n=36):
    """
    Creamos un patrón geométrico con n puntos
    """
    angulos = np.linspace(0, 2*np.pi, n, endpoint=False)
    radio = 1
    x = radio * np.cos(angulos)
    y = radio * np.sin(angulos)

    #Crear la figura
    plt.figure(figsize=(10, 10))

    #Dibujar las líneas conectando puntos alternos
    for i in range(n):
        for j in range(i+1, n):
            if(j - i) % 3 == 0: #cONECTAMOS CADA PUNTO
                plt.plot([x[i], x [j]], [y[i], y[j]],
                         color=plt.cm.viridis(i/n), alpha=0.5)
    plt.title("Patron Geométrico")
    plt.axis("equal")
    plt.savefig("patron_gemetrico.png")
    plt.close()
#Generamos el patrón
crear_patron_geometrico(36)


#Día 67/365
"""
Simulación de un 
Cajero Automático 💳
"""
class cajeroautomatico:
    def __init__(self, saldo_inicial = 500):
        self.saldo = saldo_inicial

    def consultar_saldo(self):
        print(f"💰 Saldo actual: ${self.saldo}")
    
    def retirar_dinero(self, monto):
        if monto > self.saldo:
            print("❌ fondos insuficientes.")
        elif monto <= 0:
            print("❌ Ingresa un monto válido.")
        else:
            self.saldo -= monto
            print(f"✅ Retiro exitoso. Nuevo saldo: ${self.saldo}")

    def depositar_dinero(self, monto):
        if monto <0:
            print("❌ Ingresa un monto válido.")
        else:
            self.saldo += monto
            print(f"✅ Depósito exitoso. Nuevo saldo: ${self.saldo}")
#Función principal
def iniciar_cajero():
    cajero = cajeroautomatico()

    while True:
        print("\n🏦 Bienvenido al Cajero Automático")
        print("📌 Opciones:\n1. Consultar saldo\n2. Retirar dinero\n3. Depositar dinero\n4. Salir")
        opcion = input("Elegir una opción: ")

        if opcion == "1":
            cajero.consultar_saldo()
        elif opcion == "2":
            monto = float(input("Ingresa el monto a retirar: "))
            cajero.retirar_dinero(monto)
        elif opcion == "3":
            monto  = float(input("Ingresar el monto a depositar: "))
            cajero.depositar_dinero(monto)
        elif opcion == "4":
            print("👋 Gracias por usar el cajero. ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

#Ejecutar el cajero 
iniciar_cajero()


#Día 68/365
"""
 Hoy creamos un Organizador 
 de Tareas con Prioridades ✅🔥
"""

def agregar_tareas():
    tareas = []
    while True:
        tarea = input("📝 Ingresa una tarea (o 'salir' para terminar): ")
        if tarea.lower() == "salir":
            break

        prioridad = input("📌 Prioridad (1 = Alta, 2 = Media, 3 = Baja): ")
        if prioridad not in ["1", "2", "3"]:
            print("⚠️ Prioridad no válida. Usa 1, 2 o 3.")
            continue
        tareas.append((tarea, int(prioridad)))

    #Ordenar por prioridad (1 = más importante)
    tareas.sort(key=lambda x: x[1])


    print("\n✅ **Lista de tareas organizadas por prioridad:**")
    for tarea, prioridad in tareas:
        prioridad_texto = {1: "🔴 Alta", 2: "🟡 Media", 3: "🟢 Baja"}[prioridad]
        print(f"{prioridad_texto} → {tarea}")
#Ejecutar el programa
agregar_tareas()


#Día 69/365
"""
Comprimir cadenas de texto
"""

def comprimir_cadena(cadena):
    if not cadena:
        return ""
    
    resultado = []
    contador = 1

    for i in range(1, len(cadena)):
        if cadena[i] == cadena[i -1]:
            contador += 1

        else:
            resultado.append(cadena[i -1] + str(contador))
            contador = 1

    resultado.append(cadena[-1] + str(contador)) #Agregamos el ultimo grupó
    return "".join(resultado)

#Ejemplo de uso 
texto = "aaaabbcddd"
comprimido = comprimir_cadena(texto)
print("Texto comprimido:", comprimido)


#Día 70/365
"""
Detectar si una lista
 está ordenada en Python
"""
def verificar_orden(lista):
    if lista  == sorted(lista):
        return "La lista esta ordenado de forma ascendente."
    elif lista == sorted(lista, reverse=True):
        return "La lista esta ordenada de forma descendente"
    else:
        return "La lista no está ordenada."
    
#Ejemplo de uso 
numeros = [3, 2, 1]
print(verificar_orden(numeros))

