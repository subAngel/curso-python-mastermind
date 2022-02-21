def fibonacci_recursivo(n):
    if n <= 1:
        return 1
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)


def potencia(numero, base=2):
    result = numero
    for a in range(1, base):
        result *= numero
    return result


def main():
    # for a in range(10):
    #     print(fibonacci_recursivo(a))
    print(potencia(4))
    print(potencia(4, 3))


if __name__=="__main__":
    main()