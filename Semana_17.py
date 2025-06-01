#Día 113 / 365
"""
Crea tu primera interfaz gráfica con Tkinter
"""
import tkinter as tk

def saludar():
    nombre = entrada.get()
    etiqueta_saludar.config(text=f"¡Hola, {nombre}!")

ventana = tk.Tk()
ventana.title("Saludador")

etiqueta = tk.Label(ventana, text="Escribe tu nombre: ")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()

etiqueta_saludar = tk.Label(ventana, text="")
etiqueta_saludar.pack()

ventana.mainloop()


#Día 114 / 365
"""
Crea una calculadora de suma con interfaz gráfica
"""
import tkinter as tk

def sumar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado = num1 + num2
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        etiqueta_resultado.config(text="Ingresa solo números")
ventana = tk.Tk()
ventana.title("Calculadora de Suma")

tk.Label(ventana, text="Numero 1:").pack()
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Numero 2:").pack()
entrada2 = tk.Entry(ventana)
entrada2.pack()

tk.Button(ventana, text="Sumar", command=sumar).pack()

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

ventana.mainloop()


#Día 115 / 365
"""
Calculadora de propinas con interfaz gráfica
"""
import tkinter as tk

def calcular_propina(porcentaje):
    try:
        monto = float(entrada.get())
        propina = monto * porcentaje
        total = monto + propina
        resultado.config(text=f"Propina: ${propina:.2f}\nTotal: ${total:.2f}")
    except ValueError:
        resultado.config(text="Ingresa un monto válido.")
    
ventana = tk.Tk()
ventana.title("Calculadora de propinas")

tk.Label(ventana, text="Monto de la cuenta ($):").pack()
entrada = tk.Entry(ventana)
entrada.pack()

tk.Button(ventana, text="10%",command=lambda: calcular_propina(0.10)).pack()
tk.Button(ventana, text="15%",command=lambda: calcular_propina(0.15)).pack()
tk.Button(ventana, text="20%",command=lambda: calcular_propina(0.20)).pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

ventana.mainloop()


#Día 116 / 365
"""
Simulador de préstamo bancario
"""
#Entrada
monto = float(input("Ingresa el monto del préstamo (en dólares): "))
interes_anual = float(input("ingresa el intéres anual (%): "))
anios = int(input("ingresa el número de años para pagar: "))

#Calcular
interes_mensual = interes_anual / 12 / 100
num_pagos = anios * 12
pago_mensual = (monto * interes_mensual) / (1 - (1 + interes_mensual) ** -num_pagos)

#Salida
print(f"Tu pago mensual será de: ${pago_mensual:.2f}")


#Día 117 / 365
"""
Calculadora de Costos de Envío por Peso
"""
peso = float(input("¿Cuál es el peso del paquete en kilogramos?: "))

distancia = float(input("¿cuál es la distancia del envío en kilometros?:  "))

if peso <= 1:
    costo_base = 5
elif peso <= 5:
    costo_base = 10
else:
    costo_base = 20

if distancia <= 50:
    cargo_distancia = 0
elif distancia <= 200:
    cargo_distancia = 5
else:
    cargo_distancia = 10

costo_total = costo_base + cargo_distancia

print(f"El costo total de envío es de ${costo_total:.2f} dólares")


#Día 118 / 365
"""
Calculadora de Ganancias por Ventas
"""
precio_venta = float(input("¿Cuál es el precio de venta del producto en dólares?: "))

costo_producto = float(input("¿Cuánto fue el costo del producto en dólares? "))

cantidad_vendida = int(input("¿Cuántos productos vendiste? "))

ganancia_bruta = (precio_venta - costo_producto) * cantidad_vendida

impuestos = ganancia_bruta * 0.15

ganancia_neta = ganancia_bruta - impuestos

print(f"Tu ganancia neta despues de impuestos es de ${ganancia_neta:.2f} dólares.")


#Día 119 / 365
"""
Calculadora de impuestos progresivos para empresas
"""
ganacias = float(input("Ingresa las ganancias anuales de la empresa: "))

impuestos = 0

if ganacias <= 50000:
    impuestos = ganacias * 0.10
elif ganacias <= 100000:
    impuestos = (50000 * 0.10) + ((ganacias - 50000) * 0.20) 
else:
    impuestos = (50000 * 0.10) + (50000 * 0.20) + ((ganacias - 100000) * 0.30)

print(f"Impuestos a pagar: ${impuestos:.2f}")
