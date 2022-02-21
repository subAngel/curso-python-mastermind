# Una juguetería tien mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa
# de logística lers cobra por peso de cada paquete así que deben calcular el peso de los payasos ymuñecas que saldrán
# en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos
# y muñecas vendidos en el último pedido y calcule el peso total del paquete que será elevado.

peso_clowns = 112   # Cada payaso pesa 112 g
peso_dolls = 75     # Cada muñeca pesa 75 g
clowns = int(input("Cuantos payasos va a enviar? "))
dolls = int(input("Cuantas muñecas va a enviar? "))
peso_total = clowns*peso_clowns + dolls*peso_dolls
print("El peso total del paquete es de {} kg".format(peso_total/1000))