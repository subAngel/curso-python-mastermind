asignaturas = {'Matematicas': 6, 'Fisica': 4, 'Quimica': 5}
total_creditos = 0

for asignatura, creditos in asignaturas.items():
    print("{} tiene {} creditos".format(asignatura, creditos))
    total_creditos += creditos

print("Creditos totales: {}".format(total_creditos))