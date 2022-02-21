n = int(input("Ingrese un numero entero positivo mayor a 2: "))
i = 2
while n % i != 0:
    i+=1
if i == n:
    print("{} es primo".format(n))
else:
    print("{} no es primo".format(n))