input_user = input("Ingrese numeros separados por coma (Ejemplo: x,x,x): ")
lista_numeros = list(input_user.split(","))
n = len(lista_numeros)
for i in range(n):
    lista_numeros[i] = int(lista_numeros[i])
lista_numeros = tuple(lista_numeros)
sum = 0
sumsq = 0
for i in lista_numeros:
    sum += i
    sumsq += i**2
mean = sum/n
stdev = (sumsq/n-mean**2)**(1/2)
print("La media es {}".format(round(mean, 2)))
print("La desviacion tipica es {}".format(round(stdev, 2)))