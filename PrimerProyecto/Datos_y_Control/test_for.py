frase = "hola mi nombre es angel"

vocales = 0

lista_vocales = ["a", "e", "i", "o", "u"]

for letra in frase:
    if letra in lista_vocales:
        print("He encontrado una '{}'".format(letra))
        vocales += 1

print("Vocales encontradas: {}".format(vocales))