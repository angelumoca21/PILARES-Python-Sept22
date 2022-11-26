"""
1.Crear lista con asignaturas (strings)
2.Crear lista para calificaciones (float)
3.Llenar las lista calificaciones
4.Imprimir elementos
"""
asignaturas = ["Mate","Fisica","Quimica","Historia","Lengua"]
calificaciones = []

for asignatura in asignaturas:
    cal = input(f"Cuanto sacaste en {asignatura}:")
    calificaciones.append(cal)

"""for asignatura,calificacion in zip(asignarutas,calificaciones):
    print(f"En la asignatura {asignatura} has sacado {calificacion}")"""

tam = len(calificaciones)
for i in range(0,tam):
    print("En la asignatura " + asignaturas[i] + " has sacado " + calificaciones[i])
