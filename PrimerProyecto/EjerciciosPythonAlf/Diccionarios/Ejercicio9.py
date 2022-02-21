"""
facturas = {}

continuar = True

while(continuar):
    entrada = input("Quiere añadir una nueva factura, pagar una existente o terminar [A/P/T]? ")
    if entrada == "A":
        clave = input("Ingrese la nueva factura: ")
        valor = input("Ingrese el valor de la factura '{}': ".format(clave))
        facturas[clave] = valor

    elif entrada == "P":
        clave = input("Ingrese la factura a pagar: ")
        del facturas[clave]
        print("Factura pagada")

    elif entrada == "T":
        continuar = False

    else:
        print("Opcion no valida...")

print(facturas)
"""
facturas = {}
cobrado = 0
pendiente = 0
opcion = ''
while opcion != "T":
    if opcion == "A":
        clave = input("Introduce el numero de la factura: ")
        coste = float(input("introduce el coste de la factura: "))
        facturas[clave] = coste
        pendiente += coste
    if opcion == "P":
        clave = input("Introduce el numero de la factura a pagar: ")
        coste = facturas.pop(clave, 0)
        cobrado += coste
        pendiente -= coste
    print("{:<20} {:<5}".format("Recaudado", cobrado))
    print("{:<20} {:<5}".format("Pendiente de cobro", pendiente))
    opcion = input("Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? ")