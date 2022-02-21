num = int(input("numero de la tabla? "))

resultado = 0

print("Tabla del {}".format(num))

for i in range(1, 10+1):
    print("{} x {} = {}".format(num, i, num*i))