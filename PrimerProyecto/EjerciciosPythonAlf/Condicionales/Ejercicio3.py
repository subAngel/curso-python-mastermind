divisor = int(input("Ingrese el divisor: "))
dividendo = int(input("Ingrese el dividendo: "))

division = divisor/dividendo

if divisor == 0:
    print("ERROR")
else:
    print("{} entre {} es igual a {}".format(divisor, dividendo, round(division, 2)))