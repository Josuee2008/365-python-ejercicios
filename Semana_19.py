#Día 128 / 365
"""
Simulador de stock para una pequeña tienda
"""
stock = {}

num_productos = int(input("¿Cuántos preductos quieres registrar? "))

for _ in range(num_productos):
    nombre = input("Nombre del prodcuto: ")
    cantidad = int(input(f"Cantidad de {nombre} en stock: "))
    stock[nombre] = cantidad

print("\nStock inicial:")
for producto, cantidad in stock.items():
    print(f"{producto}: {cantidad} unidades")

print("\nRegistrar ventas:")
for producto in stock:
    vendidos = int(input(f"¿Cuántas {producto} se vendieron? "))
    stock[producto] -= vendidos

print("\nStock actualizado:")
for producto, cantidad in stock.items():
    print(f"{producto}: {cantidad} unidades restantes")


#Día 129 / 365
"""
 Registro de asistencia semanal en Python
"""

estudiantes = input("Ingresa los nombres de los estudiantes (separados por coma): ").split(",")

estudiantes = [e.strip() for e in estudiantes]

asistencias = {e: 0 for e in estudiantes}

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

for dia in dias:
    presentes = input(f"¿Quiénes asistieron el {dia}? (separa los nombres con coma): ").split(",")
    presentes = [p.strip() for p in presentes]

    for estudiante in presentes:
        if estudiante in asistencias:
            asistencias[estudiante] += 1

print("\nPorcentaje de asistencia semanala:")
for estudiante, cantidad, in asistencias.items():
    porcentaje = (cantidad / len(dias)) * 100
    print(f"{estudiante}: {porcentaje:.2f}%")

#Día 130 / 365
"""
El Reloj de Sol Digital con Emojis
"""
import time

def reloj():
    while True:
        hora_actual = time.localtime()
        horas = hora_actual.tm_hour % 12
        minutos = hora_actual.tm_min

        posicion = (horas + minutos/60) * 2

        cielo = ["🌑"] * 24
        cielo[int(posicion)] = "🌞"

        print(f"{''.join(cielo)} {horas}:{minutos:02d} {'AM' if hora_actual.tm_hour < 12 else 'PM'}")
        time.sleep(60)

reloj()


#Día 131 / 365
"""
 calculadora completa con interfaz gráfica
"""
import tkinter as tk
from tkinter import font

def agregar_caracter(caracter):
    entrada.insert(tk.END, caracter)

def calcular():
    try:
        expresion = entrada.get()
        resultado = str(eval(expresion))
        entrada.delete(0, tk.END)
        entrada.insert(0, resultado)
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

def limpiar():
    entrada.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.resizable(0, 0)

fuente = font.Font(size=14)

entrada = tk.Entry(ventana, width=20, font=fuente, borderwidth=5, justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]
for (texto, fila, columna) in botones:
    if texto == '=':
        boton = tk.Button(ventana, text=texto, padx=30, pady=20,command=calcular, bg='#4CAF50', fg="white")
    elif texto in 'C':
        boton = tk.Button(ventana, text=texto, padx=30, pady=20, command=limpiar, bg='#f44336', fg="white")
    else:
        boton = tk.Button(ventana, text=texto, padx=30, pady=20,
                          command=lambda t=texto: agregar_caracter(t))
    boton.grid(row=fila, column=columna)

boton_limpiar = tk.Button(ventana, text='C', padx=30, pady=20, command=limpiar, bg="#f44336", fg="white" )
boton_limpiar.grid(row=5, column=0, columnspan=4, sticky="nsew")

ventana.mainloop()



#Día 132 / 365
"""
 Validación de Paréntesis (Estructuras de datos)
"""
def validar_parentesis(cadena):
    pila = []
    parejas = {')': '(', ']':'[', '}':'{'}
    for char in cadena:
        if char in parejas.values():
            pila.append(char)
        elif char in parejas.keys():
            if not pila or pila.pop() != parejas[char]:
                return False
    return not pila

print(validar_parentesis("({[]})")) #True quiere decir que todo esta bien cerrado
print(validar_parentesis("({[}")) #False quiere decir que el orden o cierre esta mal


#Día 133 / 365
"""
Validador de Etiquetas HTML con Stack
"""
def validad_etiqueta_html(codigo):
    pila = []
    i = 0
    while i < len(codigo):
        if codigo[i] == '<':
            if i + 1 >= len(codigo):
                return False
            
            if codigo[i + 1] == '/':
                fin = codigo.find('>', i)
                if fin == -1:
                    return False
                etiquta = codigo[i+2:fin]
                if not pila or pila.pop() != etiquta:
                    return False
                i = fin + 1
            else:
                fin = codigo.find('>', i)
                if fin == -1:
                    return False
                etiquta = codigo[i + 1:fin].split()[0]
                pila.append(etiquta)
                i = fin + 1
        else:
            i += 1
    return not pila

print(validad_etiqueta_html("<div><p>Hola</p></div>"))
print(validad_etiqueta_html("<div><span>Mundo</div></span>"))
print(validad_etiqueta_html("<a href='#'>Link</a>"))



#Día 134 / 365
"""
Mini-Buscador de Archivos (Sistema de Archivos)
"""
import os
def buscador_archivos(extensión, directorio = "."):
    for raíz, _, archivos in os.walk(directorio):
        for archivos in archivos:
            if archivos.endswith(extensión):
                print(os.path.join(raíz, archivos))

buscador_archivos(".py")



