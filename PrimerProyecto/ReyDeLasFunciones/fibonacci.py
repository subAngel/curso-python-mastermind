
def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b


def main():
    n = int(input("Ingrese el numero de suceciones a mostrar: "))
    fib(n)


if __name__ == "__main__":
    main()
