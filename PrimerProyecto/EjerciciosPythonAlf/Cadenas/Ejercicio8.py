# MI SOLUCION
precio_producto = input("Cual es el precio del pan? ")
print(precio_producto[:precio_producto.find(".")] + " Euros con " + precio_producto[precio_producto.find(".")+1:] + " centavos")

# SOLUCION PAGINA WEB
precio = input("Introduce el precio del producto con dos decimales: ")
print(precio[:precio.find(".")], ' euros con ', precio[precio.find(".")+1:], ' centavos')