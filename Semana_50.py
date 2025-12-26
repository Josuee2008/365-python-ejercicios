# Día 344 / 365
# Simulador de fallos de sensores
import random

def generar_valor(normal, ruido=2, prob_fallo=0.05):
    if random.random() < prob_fallo:
        return random.uniform(normal*5, normal*10)
    return normal + random.uniform(-ruido, ruido)

def evaluar_sensor(nombre, valores, limite):
    fallos = [v for v in valores if abs(v) > limite]
    print(f"\nSensor: {nombre}")
    print("Valores:", [round(v, 2) for v in valores])
    if fallos:
        print("⚠ FALLA detectada en valores:", [round(f,2) for f in fallos])
    else:
        print("✔ Sensor funcionando normalmente.")

def main():
    sensores = {
        "temperatura": (25, 2, 40),
        "humedad": (60, 5, 90),
        "vibración": (5, 1, 12),
    }

    for nombre, (normal, ruido, limite) in sensores.items():
        valores = [generar_valor(normal, ruido) for _ in range(8)]
        evaluar_sensor(nombre, valores, limite)

if __name__ == "__main__":
    main()



# Dia 345 / 365
# Simulador de Estación Meteorológica DIY
import random

def generar_datos():
    return {
        "temperatura": round(random.uniform(10, 40), 1),
        "humedad": random.randint(20, 100),
        "viento": random.randint(0, 80),
        "presion": random.randint(970, 1030)
    }

def clasificar_clima(datos):
    t = datos["temperatura"]
    h = datos["humedad"]
    v = datos["viento"]
    p = datos["presion"]

    if v > 55 and p < 990:
        return "🌩️ Tormenta fuerte"
    elif t > 36:
        return "🔥 Calor extremo"
    elif h > 80 and p < 1005:
        return "🌧️ Lluvia probable"
    else:
        return "🌤️ Condiciones normales"

def reporte(datos):
    print("\n=== Estación Meteorológica ===")
    for k, v in datos.items():
        print(f"{k.capitalize()}: {v}")
    print("Estado:", clasificar_clima(datos))

if __name__ == "__main__":
    datos = generar_datos()
    reporte(datos)


# Día 346 / 365
# Clasificador simple de plantas con ML (KNN)

from sklearn.neighbors import KNeighborsClassifier
import numpy as np

X = np.array([
    [15, 1], [18, 2], [12, 1],     
    [30, 6], [25, 5], [28, 7],      
    [60, 10], [55, 11], [58, 12]   
])

y = np.array([
    "Cactus", "Cactus", "Cactus",
    "Helecho", "Helecho", "Helecho",
    "Girasol", "Girasol", "Girasol"
])

modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X, y)

nueva_planta = np.array([[40, 8]])  
prediccion = modelo.predict(nueva_planta)

print("La planta predicha es:", prediccion[0])



# Día 347 / 365
# Predicción de consumo eléctrico doméstico
import random
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

def generar_datos(n=300):
    data = []

    for _ in range(n):
        temp = random.uniform(10, 38)
        personas = random.randint(1, 6)
        dia = random.randint(0, 6)
        electro = random.randint(0, 1)
        horas_ac = random.uniform(0, 10)

        consumo = (
            3 +
            personas * 0.8 +
            horas_ac * 1.2 +
            electro * 2.5 +
            temp * 0.05 +
            random.gauss(0, 1)
        )

        data.append([temp, personas, dia, electro, horas_ac, consumo])

    return pd.DataFrame(
        data,
        columns=[
            "temperatura",
            "personas",
            "dia_semana",
            "electrodomesticos",
            "horas_ac",
            "consumo_kwh"
        ]
    )

# Crear dataset
df = generar_datos()

# Preparación de datos

X = df.drop("consumo_kwh", axis=1)
y = df["consumo_kwh"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Entrenamiento del modelo

modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Evaluación

pred = modelo.predict(X_test)
mae = mean_absolute_error(y_test, pred)
r2 = r2_score(y_test, pred)

print(f"MAE: {mae:.2f} kWh")
print(f"R²: {r2:.2f}")

# Predicción práctica

nueva_casa = pd.DataFrame([{
    "temperatura": 32,
    "personas": 4,
    "dia_semana": 5,
    "electrodomesticos": 1,
    "horas_ac": 7
}])

estimacion = modelo.predict(nueva_casa)[0]
print(f"\nConsumo estimado para hoy: {estimacion:.2f} kWh")



# Día 348 / 365
# Clasificador simple: aprobar o no

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = {
    "horas_estudio": [2, 4, 6, 8, 1, 7],
    "asistencia": [60, 70, 80, 90, 50, 85],
    "aprueba": [0, 0, 1, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df[["horas_estudio", "asistencia"]]
y = df["aprueba"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

modelo = LogisticRegression()
modelo.fit(X_train, y_train)

nuevo_estudiante = [[5, 75]]  
resultado = modelo.predict(nuevo_estudiante)

print("¿Aprueba?" , "Sí" if resultado[0] == 1 else "No")


# Día 349 / 365
# Clasificador simple de crédito
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = {
    "ingreso": [800, 1200, 3000, 1500, 4000, 600, 2500, 1000],
    "edad": [22, 25, 40, 30, 50, 21, 35, 28],
    "historial": [1, 2, 10, 4, 15, 0, 7, 3],
    "deuda": [300, 500, 400, 600, 200, 700, 300, 500],
    "aprobado": [0, 0, 1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

X = df.drop("aprobado", axis=1)
y = df["aprobado"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

nuevo_cliente = [[2000, 29, 5, 400]]
resultado = model.predict(nuevo_cliente)

print("Crédito aprobado" if resultado[0] == 1 else "Crédito rechazado")



# Día 350 / 365
# Simulador de Clima con Predicción de Temperatura

import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def generar_temperaturas(n_dias=100, temp_inicial=20.0, max_variacion=2.0):
    temperaturas = [temp_inicial]
    for i in range(1, n_dias):
        variacion = random.uniform(-max_variacion, max_variacion)  
        temp_dia = temperaturas[-1] + variacion
        temperaturas.append(temp_dia)
    return temperaturas


n_dias = 100
temperaturas = generar_temperaturas(n_dias)

X = np.array([temperaturas[i] for i in range(n_dias-1)]).reshape(-1, 1)  
y = np.array([temperaturas[i+1] for i in range(n_dias-1)])  

modelo = LinearRegression()
modelo.fit(X, y)


predicciones = modelo.predict(X)
plt.figure(figsize=(10, 6))
plt.plot(range(1, n_dias), temperaturas[1:], label="Temperaturas reales")
plt.plot(range(1, n_dias), predicciones, label="Predicción del modelo", linestyle='dashed')
plt.xlabel("Día")
plt.ylabel("Temperatura (°C)")
plt.title("Simulador de Clima: Predicción de Temperatura")
plt.legend()
plt.show()

ultimo_dia = temperaturas[-1]
prediccion_dia_101 = modelo.predict([[ultimo_dia]]) 
print(f"Predicción de temperatura para el día 101: {prediccion_dia_101[0]:.2f} °C")
