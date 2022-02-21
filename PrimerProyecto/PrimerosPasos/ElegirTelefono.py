opcion = int(input(("IOS o Android\n"
                    "\t1 - iOS\n"
                    "\t2 - Android\n")))
invalido = "Opcion invalida..."
if opcion == 1: # Ha contestado iOS

    opcion = input("Tienes dinero? (S/N): ")
    if opcion == "S": # El usuario tiene dinero
        print("# iPhone Ultra Pro Max Ultimate")

    elif opcion == "N": # El usuario no tiene plata
        print("# iPhone de segunda mano")

    else: # Por si ingresa una opcion no contemplada
        print(invalido)

elif opcion == 2:
    opcion = input("Tienes dinero? (S/N): ")
    if opcion == "S":
        opcion = input("Te importa la camara? (S/N): ")
        if opcion == "S":
            print("# Google Pixel Super camara")
        elif opcion == "N":
            print("# Android calidad-precio")
        else:
            print(invalido)
    elif opcion == "N":
        print("# Android Chino")
    else:
        print("Opcion invalida...")
else:
    print(invalido)
