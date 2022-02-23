clientes = {}
opcion = ''
opciones = "\n(1) Añadir cliente\n" \
           "(2) Eliminar cliente\n" \
           "(3) Mostrar cliente\n" \
           "(4) Listar todos los clientes\n" \
           "(5) Listar clientes preferentes\n" \
           "(6) Terminar"
# Datos del cliente


while opcion != "6":
    print(opciones)
    opcion = input("Ingrese la opcion que desee: ")
    if opcion == "1":
        nif = input("\tIngrese el NIF del nuevo usuario: ")
        nombre = input("\tIngrese el nombre del usuario: ")
        direccion = input("\tIngrese la direccion: ")
        telefono = input("\tIngrese el numero telefonico: ")
        correo = input("\tIngrese el correo electronico: ")
        vip = input("\tEl usuario es preferente [S/N]: ")
        cliente = {'Nombre': nombre, 'Direccion': direccion, 'Telefono': telefono, 'Correo': correo, 'VIP': str(vip=='S')}
        clientes[nif] = cliente
    elif opcion == "2":
        NIF = input("\tCual es el NIF del usaurio a eliminar? ")
        if NIF in clientes:
            del clientes[NIF]
            print('\tUsuario Eliminado')
        else:
            print('\tEl usuario no se encuentra en la base de datos')
    elif opcion == "3":
        NIF = input('\tIntroduce el NIF del usuario: ')
        if NIF in clientes:
            print('\tNIF: {}'.format(NIF))
            for clave, valor in clientes[NIF].items():
                print("\t" + clave.title() + ': ' + valor)
        else:
            print('\tEl usuario no se encuentra en la base de datos')
    elif opcion == "4":
        print("\tLISTA DE CLIENTES")
        print("\t{:<5} {:<10}".format("NIF", "Nombre"))
        for nif, nombre in clientes.items():
            print("\t{:<5} {:<10}".format(nif, nombre['Nombre']))
    elif opcion == "5":
        print("\tLISTA DE CLIENTES VIP")
        print("\t{:<5} {:<10}".format("NIF", "Nombre"))
        for clave, valor in clientes.items():
            if valor['VIP'] == "True":
                print('\t{:<5} {:<10}'.format(clave, valor['Nombre']))




print(clientes)

