personas = {}

continuar = True
while(continuar):
    clave = input("Que dato quieres ingresar? ")
    valor = input(clave + ": ")
    personas[clave] = valor
    print(personas)
    continuar = input("Quieres añadir más información [S/N]? ") == "S"
