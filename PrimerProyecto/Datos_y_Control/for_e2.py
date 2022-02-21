import string

texto_usuario = input("Escriba una frase: ")

cont_mayusculas = 0

for M in texto_usuario:
    if M in string.ascii_uppercase:
        cont_mayusculas += 1

print("Mayusculas encontradas: {}".format(cont_mayusculas))