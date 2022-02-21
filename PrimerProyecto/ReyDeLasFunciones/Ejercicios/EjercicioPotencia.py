def potencia(*nums, base, potencia=False):
    if nums:
        resultado = nums**base
        return resultado
    return nums**2


def main():
    print(potencia(3, 4))


if __name__ == '__main__':
    main()

