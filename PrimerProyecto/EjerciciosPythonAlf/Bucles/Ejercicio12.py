frase = input("Escriba una frase: ")
letra = input("Ingrese una letra: ")
letra_repetida = 0

for i in frase:
    if i == letra:
        letra_repetida += 1
    else:
        pass

print("la letra '{}' se repite {} veces".format(letra, letra_repetida))
