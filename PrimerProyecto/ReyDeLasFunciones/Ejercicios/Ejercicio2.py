
def potencia(number):
    pot = number**2
    return pot


def main():
    number = int(input("Introduzca un numero: "))
    print("{} al cuadrado es {}".format(number, potencia(number)))


if __name__ == '__main__':
    main()