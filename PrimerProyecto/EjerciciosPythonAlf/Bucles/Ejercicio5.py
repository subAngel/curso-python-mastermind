amount = float(input("Ingrese la cantidad a invertir: "))
interest = float(input("Ingrese el interes anual: "))
years = int(input("ingrese el numero de años: "))
for i in range(years):
    amount += 1 + interest / 100
    print("Capital tras {} años: {}".format(i+1, round(amount, 2)))