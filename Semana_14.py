#Día 92/365
"""
Eliminar espacios duplicados
 en un texto ✨🔤
"""
def Limpiar_espacios(texto):
    return " ".join(texto.split()) #Eliminacion de espacios duplicados

#Pedimos al usuario una frase
frase = input("Ingresa una frase con espacios extra: ")
resultado = Limpiar_espacios(frase)

print("Texto limpio:", resultado)


#Día 93/365
"""
Cálculo del Total con IVA
"""

def caclular_total_con_iva(precio, iva = 0.15):
    total = precio * (1 + iva)
    return round(total, 2)

#Ejemplo de uso
precio = float(input("Ingresa el preio del producto: "))
total = caclular_total_con_iva(precio)

print(f"El precio final con IVA: ${total}")


#Día 94/365
"""
Calculadora de edad 
en meses, días y semanas
"""

def calcular_tiempo():
    edad = int(input("¿Cuantos años tienes? "))

    meses = edad * 12
    dias = edad * 365
    semanas = edad * 52

    print(f"Has vivido aproximadamente: ")
    print(f"-{meses} Meses")
    print(f"-{dias} Días")
    print(f"-{semanas} Semanas")
calcular_tiempo()


#Día 95/365
"""
Calculadora de 
Propina Inteligente 🧾💸
"""
import tkinter as tk
from tkinter import ttk, messagebox

def calcular_propina():
    try:
        cuenta = float(entry_cuenta.get())
        servicio = combo_servicio.get()

        if servicio == "Malo":
            porcentaje = 0.05
        elif servicio == "Regular":
            porcentaje = 0.10
        elif servicio == "Bueno":
            porcentaje = 0.15
        else:
            messagebox.showerror("Error", "Selecciona un nivel de servicio válido.")
            return

        propina = cuenta * porcentaje
        total = cuenta + propina

        resultado.config(text=f"💸 Propina: ${propina:.2f} | 💳 Total: ${total:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Ingresa un número válido en la cuenta.")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora de Propina")
ventana.geometry("300x200")
ventana.resizable(False, False)

# Widgets
tk.Label(ventana, text="Total de la cuenta ($):").pack(pady=5)
entry_cuenta = tk.Entry(ventana)
entry_cuenta.pack(pady=5)

tk.Label(ventana, text="Nivel de servicio:").pack(pady=5)
combo_servicio = ttk.Combobox(ventana, values=["Malo", "Regular", "Bueno"], state="readonly")
combo_servicio.pack(pady=5)

tk.Button(ventana, text="Calcular", command=calcular_propina).pack(pady=10)
resultado = tk.Label(ventana, text="")
resultado.pack(pady=5)

ventana.mainloop()



#Día 96/365
"""
Calculadora de Ahorro 
Semanal para una Meta 🎯💰
"""
def calcular_ahorro(meta, semanas):
    if semanas <= 0:
        print("Las semanas deben ser mayores a cero.")
        return
    ahorro_semanal = meta / semanas
    print(f"Debes ahorrar ${ahorro_semanal:.2f} cada semana para alcanzar tu meta.")

#Ejemplo de uso
meta = float(input("¿Cuál es tu meta de ahorro?: $"))
semanas = int(input("¿En cuántas semanas quieres lograrlo? "))
calcular_ahorro(meta, semanas)


#Día 97/365
"""
Simulador de pagos 
de tarjeta de crédito
"""
#Entrada de datos
deuda = float(input("Ingresa tu deuda total en dólares: "))
interees_mensual = float(input("Interés mensual (en %): ")) / 100
pago_mensual = float(input("¿Cuámto pagáras cada mes?: "))

#Incializacion de variables
meses = 0
total_pagos = 0

#simulación del pago mes a mes
while deuda > 0:
    deuda += deuda * interees_mensual 
    pago = min(pago_mensual, deuda)
    deuda -= pago
    total_pagos += pago
    meses += 1

#Resultados
print(f"Deuda saldad en {meses} mensuales")
print(f"Total pagado incluyendo intereses: ${round(total_pagos, 2)}")


#Día 98 / 365
"""
 Simulador de conversión de divisa
"""

tasas = {
    'EUR': 0.91,
    'MXN': 16.7,
    'JPY': 151.3,
}

#Lista para guardar historial 
historial = []

while True:
    print("\n---Conversor de Divisas ---")
    print("Monedas disponibles:", ', '.join(tasas.keys()))
    moneda = input("A que moneda quieres convertir (o escribe 'salir'): ").upper()

    if moneda == "SALIR":
        break

    if moneda not in tasas:
        print("Moneda no encontrada")
        continue
    try:
        usd = float(input("Ingresa el monto en USD: "))
    except ValueError:
        print("Monto inválido")
        continue

    tasa = tasas[moneda]
    resultado = usd * tasa
    print(f"{usd} USD = {round(resultado, 2)} {moneda} (Tasa: {tasa})")

    historial.append((usd, moneda, tasa, round(resultado, 2)))

#Mostrar historial al final
print("\n Historial de conversiones:")
for item in historial:
    print(f"{item[0]} USD → {item[3]} {item[1]} (tasa: {item[2]})")
