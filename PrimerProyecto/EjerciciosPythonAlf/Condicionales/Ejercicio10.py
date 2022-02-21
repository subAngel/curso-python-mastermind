titulo = "| Pizzeria Bella Napoli |"
carta = "CARTA" \
        "\n1. Pizza vegetariana" \
        "\n2. Pizza no vegetariana"
ingredientes = "Mozarella, tomate, "
print(len(titulo)*"-" + "\n" +titulo+ "\n" + len(titulo)*"-")
print(carta+'\n')

eleccion = input("Que pizza desea llevar? ")
if eleccion == "1":
    pizza = "vegetariana"
    print("Pizza Vegetariana"
          "\nSolo puede elegir un ingrediente"
          "\n\t1. Pimiento"
          "\n\t2. Tofu")
    eleccion = input()
    if eleccion == "1":
        ingredientes += "Pimiento"
    elif eleccion == "2":
        ingredientes += "Tofu"
elif eleccion == "2":
    pizza == "no vegetariana"
    print("Pizza no vegetariana"
          "\nSolo puede elegir un ingrediente"
          "\n\t1. Peperoni"
          "\n\t2. Jamon"
          "\n\t3. Salmon")
    eleccion = input()
    if eleccion == "1":
        ingredientes += "Peperoni"
    elif eleccion == "2":
        ingredientes += "Jamon"
    elif eleccion == "3":
        ingredientes += "Salmon"
    else:
        pass
else:
    pass
print("Tu pizza es {} con los ingredientes: {}".format(pizza, ingredientes))