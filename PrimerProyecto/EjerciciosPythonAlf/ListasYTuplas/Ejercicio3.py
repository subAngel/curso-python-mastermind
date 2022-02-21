asignaturas = ['matematicas', 'fisica', 'quimica', 'historia', 'ingles']
notas = []

for asignatura in asignaturas:
    nota = input("Cuanto sacaste en {}: ".format(asignatura))
    notas.append(nota)

print()

for i in range(len(asignaturas)):
    print("En {} sacaste {}".format(asignaturas[i].title(), notas[i]))

