peso_dolar = 0.046
dolar_peso = 21.20
peso_euro = 0.041
euro_peso = 24.16

opcion = input("Que moneda quiere convertir? \n"
               "\t1 - Convertir de peso a dolar\n"
               "\t2 - Convertir de dolar a peso\n"
               "\t3 - Convertir de peso a euro\n"
               "\t4 - Convertir de euro a peso\n")
texto_usuario = "Introduzca la cantidad de {} a convertir: "

if opcion == "1":
    cantidad_de_dinero = float(input(texto_usuario.format("pesos")))
    print("La cantidad en dolares es {}".format(cantidad_de_dinero*peso_dolar))
elif opcion == "2":
    cantidad_dinero = float(input(texto_usuario.format("dolares")))
    print("La cantidad en pesos es {}".format(cantidad_dinero*dolar_peso))
elif opcion == "3":
    cantidad_dinero = float(input(texto_usuario.format("pesos")))
    print("La cantidad en euros es {}".format(cantidad_dinero*peso_euro))
elif opcion == "4":
    cantidad_dinero = float(input(texto_usuario.format("euros")))
    print("La cantidad en pesos es {}".format(cantidad_dinero*euro_peso))
else:
    print("Opcion Incorrecta")
