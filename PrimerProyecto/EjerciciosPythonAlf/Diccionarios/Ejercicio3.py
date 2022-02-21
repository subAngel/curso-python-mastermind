# Diccionario de frutas
frutas = {'Platano': 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja': 0.70}

# Preguntar al usuario que fruta desea
fruta = input('Que fruta desea? ')

if fruta in frutas:
    kilos = int(input('Cuantos kilos quiere? '))
    precio = kilos*frutas[fruta]
    print('El precio por los {} kilos de {} serán {}'.format(kilos, fruta, round(precio, 2)))
else:
    print('Esa fruta no la tenemos, joven')