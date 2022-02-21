
numeros_introducidos = input("introduzca los numeros separados por comas: ")
lista_numeros = [int(numero) for numero in numeros_introducidos.split(",")]

numero_pequenio = lista_numeros[0]
numero_grande = lista_numeros[0]

for numero in lista_numeros[1:]:
    if numero_pequenio > numero:
        numero_pequenio = numero

    if numero_grande < numero:
        numero_grande = numero


print("Numero Grande: {}, Numero pequenio: {}".format(numero_grande,numero_pequenio))
