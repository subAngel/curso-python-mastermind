dict_traductor = {"hola": "hi", "mi": "my", "nombre": "name", "es": "is", 'cual': 'what'}

frase_esp = input("Ingrese una frase: ")
frase_ing = ""

for i in frase_esp.split():
    if i.lower() in dict_traductor:
        print(dict_traductor[i], end=' ')
    else:
        print(i, end=' ')
