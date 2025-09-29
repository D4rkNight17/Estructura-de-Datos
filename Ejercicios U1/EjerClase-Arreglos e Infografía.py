import random
import time

# Parámetros
num_alumnos = int(input("Ingrese número de alumnos: "))
num_materias = int(input("Ingrese número de materias: "))

inicio = time.time()

# Crear matriz con calificaciones aleatorias
matriz = [[random.randint(0, 100) for _ in range(num_materias)] for _ in range(num_alumnos)]

# Encabezado
print(f"{'Alumno':<10}", end="")
for j in range(num_materias):
    print(f"Materia{j+1:<10}", end="")
print()

# Separador
print("-" * (10 + num_materias * 10))

# Imprimir todos los alumnos con sus calificaciones
for i in range(num_alumnos):
    print(f"{'Alumno' +str(i+1):<10}", end="")

    for j in range(num_materias):
        print(f"{matriz[i][j]:<10}", end="")
    print()

fin = time.time()
print("\n⏱️ Tiempo de ejecución:", round(fin - inicio, 6), "segundos")

# ============================
# BÚSQUEDA DE ALUMNO Y MATERIA
# ============================
alumno_buscar = 321
materia_buscar = 5

if alumno_buscar <= num_alumnos and materia_buscar <= num_materias:
    calificacion = matriz[alumno_buscar-1][materia_buscar-1]
    print(f"\n🔍 Calificación del Alumno {alumno_buscar} en Materia {materia_buscar}: {calificacion}")
else:
    print("\n❌ Ese alumno o materia no existe en la tabla.")
