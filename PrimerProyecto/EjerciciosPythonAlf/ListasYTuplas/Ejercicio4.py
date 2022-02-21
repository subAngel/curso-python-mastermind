lista_ganadores = []

for n in range(5):
    lista_ganadores.append(int(input("Introduce los numeros ganadores: ")))

lista_ganadores.sort()
print("Los numeros ganadores son: {}".format(lista_ganadores))