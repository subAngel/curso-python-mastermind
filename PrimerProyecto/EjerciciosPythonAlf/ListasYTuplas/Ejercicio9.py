vocales = ['a', 'e', 'i', 'o', 'u']
frase = input("Escribe una frase: ")
for vocal in vocales:
    count = 0
    for letra in frase:
        if letra.lower() == vocal:
            count += 1
    print("La vocal '{}' se repite {} veces en la frase".format(vocal, count))
