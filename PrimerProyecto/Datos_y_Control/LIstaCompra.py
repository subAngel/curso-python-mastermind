
titulo = "LISTA DE LA COMPRA"
print(titulo + "\n"+len(titulo)*"-")

pregunta = "Que desea comprar? ([Q] para salir): "

producto = None
lista_compra = []

while True:
    producto = input(pregunta)
    if producto == "Q":
        break
    elif producto in lista_compra:
        print("{} ya está en la lista!".format(producto))
    else:
        if input("Seguro que quieres agregar '{}' [S/N]: ".format(producto)) == "S":
            lista_compra.append(producto)
            print("{} añadido!".format(producto))

salida = "La Lista de la compra es: {}".format(lista_compra)
print(len(salida)*"-" + "\n" + salida)
