# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla
# la <n> entre <m> de un cociente <c> y un resto <r> donde <n> y <m> son los numeros introducidos por el usuario,
# y <c> y <r> son el cociente y el resto de la división entera respectivamente.

n = int(input("Ingrese el primer numero entero: "))
m = int(input("Ingrese el segundo numero entero: "))
c = n//m
r = n%m
print("{} entre {} da un cociente de {} y un resto de {}".format(n, m, c, r))