#Día 106 / 365
"""
Calcular los gastos mensuales
"""
ingresos = float(input("¿Cuánto ganas al mes?: $"))

gasots = []
categorias = ["alquiler", "comida", "transporte", "otros"]

for categoria in categorias:
    gasto = float(input(f"Ingresa cuánto gastas en {categoria}: $"))
    gasots.append(gasto)

total_gastos = sum(gasots)
saldo_final = ingresos - total_gastos

print(f"\nGastas un total de ${total_gastos:.2f}")
print(f"Te queda ${saldo_final:.2f} este mes")


#Día 107 / 365
"""
Sueldo por hora trabajada
"""
sueldo_mensual = float(input("¿Cuál es tu sueldo mensul en dólares? "))
horas_mensuales = float(input("¿Cuántas horas trabajas al mes? "))

if horas_mensuales > 0:
    sueldo_por_hora = sueldo_mensual / horas_mensuales
    print(f"Ganas aproximadamente ${sueldo_por_hora:.2f} por hora.")
else:
    print("Las horas trabajados deben ser mayores a cero.")




#Día 108 / 365
"""
Calculadora de Precio por Unidad
"""
precio_a = float(input("Ingresa el precio del Producto A: "))
unidades_a = float(input("Ingresa cuántas unidades trae el Producto A: "))

precio_b = float(input("Ingresa el precio del Producto B: "))
unidades_b = float(input("Ingresa cuántas unidades trae el Producto B: "))

unidad_a = precio_a / unidades_a
unidad_b = precio_b / unidades_b

print(f"El Producto A cuesta${unidad_a:.2f} por unidad.")
print(f"El Producto B cuesta${unidad_b:.2f} por unidad.")

if unidad_a < unidad_b:
    print("El Preducto A es más conveniente.")
elif unidad_b < unidad_a:
    print("El Preducto B es más conveniente.")
else:
    print("Ambos porductos tienen el mismo precio por unidad.")



#Día 109 / 365
"""
Calculadora de ganancias netas
"""

ingresos = float(input("¿Cuánto ganaste cada mes (ingresos brutos)? "))

impuestos = float(input("¿Qué porcentaje pagas de impuestos? (Ejemplo: 15) "))

monto_impuesto = ingresos * (impuestos / 100)

ganancias_netas = ingresos - monto_impuesto

print(f"Después de impustos, ganaste ${ganancias_netas:.2f}")


#Día 110/ 365
"""
Calculadora de Intereses Simples
"""
capital = float(input("¿Cuánto dinero vas a invertir?: "))
tasa_interes = float(input("¿Cuál es la tasa de interés anual (%): "))
tiempo = float(input("¿Cuántos años durará la inversion? "))

interes = capital * (tasa_interes / 100) * tiempo

total = capital + interes

print(f"Interés generado: ${interes:.2f}")
print(f"Total después de {tiempo} años: ${total:.2f}")


# Día 111 / 356
"""
¿Cuántos productos caben en una caja?
"""
caja = float(input("Tamaño de la caja en cm³: "))
producto = float(input("Tamaño de un producto en cm³: "))

cantidad = int(caja // producto)

print("Puede caber", cantidad, "productos en la caja")


#Día 112 / 365
"""
Costo de limpieza por metro cuadrado
"""
metros = float(input("¿Cuántos metros cuadrados hay que limpiar?: "))
precio = float(input("¿Cuánto cuesta limpiar por metro cuadrado?: "))

total = metros * precio

print(f"El costo total de la limpieza es: ${total:.2f}")
