"""
1.Crear lista con asignaturas (strings)
2.Crear lista para calificaciones (float)
3.Llenar las lista calificaciones
4.Imprimir elementos
"""
asignarutas = ["Mate","Fisica","Quimica","Historia","Lengua"]
calificaciones = []

for asignatura in asignarutas:
    cal = input(f"Cuanto sacaste en {asignatura}:")
    calificaciones.append(cal)

for asignatura,calificacion in zip(asignarutas,calificaciones):
    print(f"En la asignatura {asignatura} has sacado {calificacion}")
