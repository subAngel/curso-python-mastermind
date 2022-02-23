def area_circulo(radio):
    pi = 3.14
    return pi * radio**2


def volumen_cilindro(radio, altura):
    return round(area_circulo(radio) * altura, 3)


print(volumen_cilindro(14, 20))