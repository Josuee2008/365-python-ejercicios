# Día 281 / 365
# Mini juego del dinosaruio 
import pygame, sys, random
pygame.init()
p = pygame.display.set_mode((800, 300)); r = pygame.time.Clock()
d = pygame.Rect(50, 250, 40, 40); o = pygame.Rect(800, 250, 20, 40)
vy, salto, puntos = 0, False, 0; f = pygame.font.SysFont(None, 30)
while True:
    r.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:sys.exit()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE and not salto:
            salto, vy = True, -15
    if salto:
            d.y += vy; vy += 1
            if d.y >= 250: salto, d.y = False, 250
    o.x -= 8
    if o.x <-20: o.x = random.randint(800, 1000); puntos += 1
    if d.colliderect(o):
            texto = f.render("💀 Game Over!", True, (0,0,0))
            p.blit(texto, (320, 130)); pygame.display.flip(); pygame.time.wait(800)
            o.x, puntos = 800, 0
    p.fill((255, 255, 255))
    pygame.draw.rect(p,(0,0,0), d); pygame.draw.rect(p,(0,0,0), o)
    p.blit(f.render(f"Puntos: {puntos}", True, (0,0,0)), (10,10))
    pygame.display.flip()


# Día 282 / 365
# ¿Cómo Crear una base de datos con Python?
import sqlite3

conn = sqlite3.connect("original.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS empleados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    puesto TEXT,
    salario REAL
)
""")

empleados = [
    ("Ana", "Piloto", 3500),
    ("Carlos", "Ingeniero", 4300),
    ("Lucía", "Mecánica", 3100)
]

cursor.executemany("INSERT INTO empleados(nombre, puesto, salario) VALUES (?, ?, ?)", empleados)

conn.commit()
conn.close()

print("✅ Base de datos 'original.db' creada con éxito.")


# Día 283 / 365
# Mini gestor de tareas con base de datos

import sqlite3

# Crear o conectar base
conn = sqlite3.connect("tareas.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS tareas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT,
    completada INTEGER
)
""")

tareas = [("Aprender Python", 0), ("Editar video de TikTok", 0), ("Subir código", 0)]
cur.executemany("INSERT INTO tareas(descripcion, completada) VALUES (?, ?)", tareas)

print("📋 Tareas pendientes:")
for t in cur.execute("SELECT id, descripcion FROM tareas WHERE completada=0"):
    print(f"- {t[1]}")

cur.execute("UPDATE tareas SET completada=1 WHERE id=1")
conn.commit()
print("\n✅ Primera tarea completada.")

conn.close()


# Día 284 / 365
# Mini sistema de login con base de datos
import sqlite3

conn = sqlite3.connect("usuarios2.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    password TEXT
)
""")

cur.execute("SELECT COUNT(*) FROM usuarios")
if cur.fetchone()[0] == 0:
    cur.execute("INSERT INTO usuarios(nombre, password) VALUES ('admin', '1234')")
    cur.execute("INSERT INTO usuarios(nombre, password) VALUES ('andres', 'python')")
    conn.commit()

nombre = input("Usuario: ")
clave = input("Contraseña: ")


cur.execute("SELECT * FROM usuarios WHERE nombre=? AND password=?", (nombre, clave))
if cur.fetchone(): 
    print("✅ Acceso concedido. Bienvenido,", nombre)
else:
    print("❌ Usuario o contraseña incorrecta.")

conn.close()



# Día 285 / 365
# Contador de visitas con base de datos (SQLite)

import sqlite3

conn = sqlite3.connect("contador.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS visitas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cantidad INTEGER
)
""")

cur.execute("SELECT cantidad FROM visitas WHERE id=1")
dato = cur.fetchone()

if dato is None:
    visitas = 1
    cur.execute("INSERT INTO visitas(cantidad) VALUES (?)", (visitas,))
else:
    visitas = dato[0] + 1
    cur.execute("UPDATE visitas SET cantidad=? WHERE id=1", (visitas,))

conn.commit()
conn.close()

print(f"👋 Bienvenido, esta es tu visita número {visitas}")




# Día 286 / 365
# 📊 Registro de temperatura con base de datos (SQLite)

import sqlite3, datetime, random

conn = sqlite3.connect("clima.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS temperatura(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT,
    valor REAL
)
""")

hoy = datetime.date.today()
temp = round(random.uniform(15, 35), 2)
cur.execute("INSERT INTO temperatura(fecha, valor) VALUES (?, ?)", (hoy, temp))
conn.commit()

cur.execute("SELECT AVG(valor) FROM temperatura")
prom = cur.fetchone()[0]

print(f"🌡️ Temperatura registrada hoy: {temp}°C")
print(f"📈 Promedio histórico: {prom:.2f}°C")

conn.close()



# Día 287 / 365
# ❤️ Registro de frecuencia cardíaca (SQLite + Matplotlib)
import sqlite3, datetime, random
import matplotlib.pyplot as plt

conn = sqlite3.connect("pulso.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS frecuencias(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT,
    bpm INTEGER
)
""")

hoy = datetime.date.today()
bpm = random.randint(60, 110)
cur.execute("INSERT INTO frecuencias(fecha, bpm) VALUES (?, ?)", (hoy, bpm))
conn.commit()

cur.execute("SELECT fecha, bpm FROM frecuencias ORDER BY id")
datos = cur.fetchall()
conn.close()

fechas = [d[0] for d in datos]
valores = [d[1] for d in datos]

plt.plot(fechas, valores, marker="o", color="red")
plt.title("❤️ Frecuencia cardíaca diaria")
plt.xlabel("Fecha")
plt.ylabel("Pulsaciones por minuto")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

prom = sum(valores) / len(valores)
print(f"🩺 Pulso de hoy: {bpm} bpm")
print(f"📊 Promedio histórico: {prom:.1f} bpm")
