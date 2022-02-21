lista_compra = input("Ingrese productos a comprar separados por una ',': ")
lista_compra = lista_compra.split(", ")
for i in range(len(lista_compra)):
    print(lista_compra[i])

# SOLUCION 2
cesta = input('Introduce los productos de la cesta de la compra separados por comas: ')
print(cesta.replace(',', '\n'))

# SOULCION 3
cesta = input('Introduce los productos de la cesta de la compra separados por comas: ')
print('\n'.join(cesta.split(',')))