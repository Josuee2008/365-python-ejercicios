#Día 99 /365
"""
Simulador de Lista 
de Compras con Presupuesto
"""

def lista_de_compras():
    presupúesto = float(input("Ingresa tu presupuesto total ($): "))
    total = 0
    compras = []

    while True:
        producto = input("Nombre del producto (o escribe 'fin' para terminar): ")

        if producto.lower() == 'fin':
            break

        precio = float(input(f"Precio de {producto}: $"))
        if total + precio > presupúesto:
            print("¡Te pasaste del presupuesto! No puedes agregar este producto")
        else:
            compras.append((producto, precio))
            total += precio
            print(f"Producto agregado. Total acutal: ${total:.2f}")
    print("\n🛒 Lista de compras final:")
    for p, precio in compras:
        print(f"-{p}: ${precio:.2f}")
    print(f"\n💰 Total gastado: ${total:.2f}")
    print(f"\n🤑 Dinero restante: ${presupúesto - total:.2f}")

#Ejecutar
lista_de_compras()


#Día 100/365
"""
 Simulador de Pantalla de Carga
"""
import time
import sys

def loading_screen(message = "Cargando", duration = 5, steps = 30):
    print(f"\n{message}...\n")
    for i in range(steps):
        percent = int((i + 1) * 100/ steps)
        bar = '█' * (i + 1) + '-' * (steps - i -1)
        sys.stdout.write(f"\r[{bar}] {percent}%")
        sys.stdout.flush()
        time.sleep(duration/steps)
    print("\n\n¡Carga completada!\n")

#Ejecutar simulador
loading_screen()


#Día 101/365
"""
Simulador de Reembolso de Compras 💸
"""

def calcular_rembolso():
    total = 0
    productos = int(input("¿Cuántos productos vas a devolver? "))

    precios = []
    for i in range(productos):
        precio = float(input(f"Ingresa el precio del producto #{i + 1}: "))
        precios.append(precio)

    usado = input("¿Los productos están usados? (si/no): ").strip().lower()

    total = sum(precios)

    if usado == 'si' or usado == 'sí':
        total *= 0.9 #Agregar descuento del 100%

    print(f"Total a reembolsar: ${total:.2f}")

#Ejecutar la función
calcular_rembolso()


#Día 102 /365
"""
Calculadora de Costos 
de Envío Internacional 🌍📦
"""
def calcular_envios(peso, destino, urgente):
    tarifas_base = {
        "EEUU" : 10,
        "Europa" : 15,
        "Asia" : 20,
        "Latinoamérica" : 22
    }

    tarifas_por_kg = 5
    extra_urgente = 10 if urgente.lower() == "si" else 0

    if destino in tarifas_base:
        base = tarifas_base[destino]
        total = base + (peso * tarifas_por_kg) + extra_urgente
        return total
    
    else:
        return "Destino no disponible"
    
#Entradas
peso = float(input("¿Cuanto peso tu paquete en kg?: "))
destino = input("¿A qué región lo enviarás? (EEUU, Asia, Europa, Latinoamerica): ")
urgente = input("¿Deseas envío urguente (si/no): ")

#Calcular
costo = calcular_envios(peso, destino, urgente)

#Salida
print(f"El costo total del envío es: ${costo}" if isinstance(costo, float) else costo)



#Día 103/365
"""
Calculadora de Consumo
 de Agua Diario 💧
"""
peso = float(input("¿Cuál es tu peso en kilogramos?: "))

agua_litros = peso * 0.033

print(f"Deberías tomar aproximadamente {agua_litros:.2f} litros de agua al día ")



#Día 104/365
"""
Calculadora de Interés Compuesto 📈
"""
# Preguntamos los datos
capital = float(input("¿Cuánto vas a invertir?: $ "))
interes = float(input("¿Cuál es la tasa de interés anual? (en %) "))
años = int(input("¿Durante cuántos años? "))

# Covertimos el interés a decimal
tasa = interes/100

#Fórmula del interés compuesto 
monto_final = capital *(1 + tasa) **años
#Mostramos el resultado 
print(f"Téndras ${monto_final:.2f} después de {años} años.")


#Día 105 / 365
"""
Calculadora de descuento por temporada 👇
"""
precio = float(input("Ingresa el precio del producto: "))

temporada = input("¿En qué temporada estamos? (verano/invierno/otoño/primavera): ")

if temporada == "verano":
    descuento = 0.20
elif temporada == "invierno":
    descuento = 0.15
elif temporada == "otoño":
    descuento = 0.10
elif temporada == "primavera":
    descuento = 0.05
else:
    descuento = 0

precio_final = precio*(1 - descuento)

print(f"Precio final con descuento: ${precio_final:.2f}")
