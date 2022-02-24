def lista_cuadrados(lista_numeros):
    lista = []
    for i in lista_numeros:
        lista.append(i ** 2)
    return lista


lista_numeros = [1, 2, 3, 4, 5, 6]
print(lista_cuadrados(lista_numeros))
