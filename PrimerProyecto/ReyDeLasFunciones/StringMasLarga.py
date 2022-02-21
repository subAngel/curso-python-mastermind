def string_mas_larga(cadena, *args, sumar_todo=False):
    if args:
        largos = [cadena]
        for i in args:
            largos.append(i)
        largos.sort()
        return largos
    return cadena


def main():
    print(string_mas_larga("hola", "adffdgagagad", "comadfafadfadgagagado", "estas"))
    #print(string_mas_larga("hola"))


if __name__ == '__main__':
    main()