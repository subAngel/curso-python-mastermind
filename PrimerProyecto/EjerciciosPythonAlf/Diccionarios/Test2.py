def lista_usuario():
    # Pregunto por nombre, edad, direccion y telefono
    nombre = input("Escribe tu nombre: ")
    edad = int(input("Escribe tu edad: "))
    direccion = input("Escribe tu direccion: ");
    telefono = (input("Escribe tu telefono: "))
    print()
    usuario = (nombre, edad, direccion, telefono)

    return usuario


def agregar_al_diccionario(diccionario, usuario, lista):
    if usuario not in diccionario:
        diccionario[usuario] = list()

    diccionario[usuario].extend(lista)
    return diccionario


def main():
    aux = 0

    # diccionario = {'nombre': None, 'edad': None, 'direccion': None, 'telefono': None}
    while (aux < 3):
        usuario = lista_usuario()
        diccionario = {}
        agregar_al_diccionario(diccionario, usuario[0], usuario)
        aux += 1

    print(diccionario)


if __name__ == '__main__':
    main()
