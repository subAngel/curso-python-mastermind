import random

print("ADIVINANZA")
numero_ganador = random.randint(1,10)
numero_elegido = int(input("Di un numero: "))

if numero_elegido == numero_ganador:
    print("Felicidades!!!")

if numero_elegido > 10:
    print("Te has pasado un poco... Era entre 1 y 10")
if numero_elegido < 1:
    print("Te has quedado corto")

print("Tu numero ganador es {}".format(numero_ganador))