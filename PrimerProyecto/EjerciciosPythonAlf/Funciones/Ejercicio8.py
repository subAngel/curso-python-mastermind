lista_numeros = [1, 2, 3, 4, 5, 6]


def dict(lista):
    diccionario = {}
    diccionario['Media'] = sum(lista)/len(lista)
    diccionario['Varianza'] = sum(square(lista))/len(lista)-diccionario['Media']**2
    diccionario['Desviacion Estandar'] = diccionario['Varianza']**0.5
    return diccionario


def square(lista):
    list = []
    for i in lista:
        list.append(i**2)
    return list


print(dict(lista_numeros))
