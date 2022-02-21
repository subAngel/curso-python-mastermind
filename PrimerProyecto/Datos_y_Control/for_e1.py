texto_usuario = input("Escriba una frase: ")

espacios = 0
puntos = 0
comas = 0

for char in texto_usuario:
    if char == " ":
        espacios += 1
    elif char == ".":
        puntos += 1
    elif char == ",":
        comas += 1

print("Se han encontrado: \n"
      "espacios: {}\n"
      "puntos: {}\n"
      "comas: {}".format(espacios, puntos, comas))
