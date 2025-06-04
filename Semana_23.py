#Día  155 / 365
"""
Mostrar los días festivos de 
un país en un año específico
"""

import holidays

año = int(input("Ingresa un año (por ejemplo, 2025): "))

feriados = holidays.country_holidays('EC', years=año)

print(f"Días festivos en Ecuador para el año {año}: \n")
for fecha, nombre in sorted(feriados.items()):
    print(f"{fecha}: {nombre}")
