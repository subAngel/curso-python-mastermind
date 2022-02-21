def suma(numero, *args):
    if args:
        return sum(args) + numero
    return numero


def main():
    print(suma(1,2,4,5))


if __name__ == '__main__':
    main()