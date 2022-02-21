age = int(input("Ingrese su edad: "))
if age < 4:
    precio_entrada = 0
elif age < 18:
    precio_entrada = 5
elif age >= 18:
    precio_entrada = 10
else:
    precio_entrada = None
    # Imprimiendo costo del boleto
if precio_entrada == None:
    print("ERROR")
else:
    print("Su boleto cuesta %.1f$" % precio_entrada)