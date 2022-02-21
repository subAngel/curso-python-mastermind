divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

divisa = input("Escriba una divisa: ").title()

if divisa in divisas:
    print("La divisa {} se encuentra en el diccionario, y su simbolo es {}".format(divisa, divisas[divisa]))
else:
    print("La divisa no se encuentra almacenada")