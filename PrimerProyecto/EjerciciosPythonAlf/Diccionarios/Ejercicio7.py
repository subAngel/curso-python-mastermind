cesta = {}

continuar = True

while(continuar):
    articulo = input("Que articulo quiere agregar? ")
    precio = int(input("Cual es su precio? "))
    cesta[articulo] = precio
    continuar = input("Quieres seguir agregando articulos a tu cesta [S/N]? ") == "S"

precio_total = 0
lista_de_compra = "Lista De Compra"

print("-"*len(lista_de_compra))
print(lista_de_compra)
print("-"*len(lista_de_compra))

for articulo, precio in cesta.items():
    print("{:<9} {:<4}".format(articulo, precio))
    precio_total+=precio

print("{:<9} {:<4}".format("...", "..."))
print("{:<9} {:<4}".format("Total", round(precio_total, 2)))
print("-"*len(lista_de_compra))

