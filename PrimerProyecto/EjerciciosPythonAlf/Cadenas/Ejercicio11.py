nom_prod = input("Ingrese el nombre del producto: ")
precio_prod = float(input("Ingrese su precio: "))
cant_prod = int(input("Ingrese la cantidad de ese producto: "))

salida = "{}: {} x {}$  = {}$".format(nom_prod, cant_prod, format(precio_prod, '.2f'), format(precio_prod*cant_prod, '.2f'))

print(salida)

# OTRA SOLUCION
producto = input('Introduce el nombre del producto: ')
precio = float(input('Introducde el precio unitario: '))
unidades = int(input('Introduce el número de unidades: '))
print('{producto}: {unidades:3d} unidades x {precio:9.2f}€ = {total:11.2f}€'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))