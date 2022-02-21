asignaturas = ['matematicas', 'fisica', 'quimica', 'historia', 'ingles']
notas = []
for asignatura in asignaturas:
    notas.append(int(input("Cuanto sacaste en {}: ".format(asignatura))))

for i in range(len(notas)):
    if notas[i] < 7:
        pass
    else:
        asignaturas.remove(asignaturas[i])

print("Tienes que repetir {}".format(asignaturas))