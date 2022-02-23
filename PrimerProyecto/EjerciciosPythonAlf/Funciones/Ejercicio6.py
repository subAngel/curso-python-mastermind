def calc_media(lista_numeros):
    lista_numeros = lista_numeros.split(',')
    sum, prom = 0, 0
    for i in lista_numeros:
        sum += int(i)
    return sum / len(lista_numeros)


lista_num = input("Ingrese una lista de numeros (x,x,x,...x): ")
print((calc_media(lista_num)))
