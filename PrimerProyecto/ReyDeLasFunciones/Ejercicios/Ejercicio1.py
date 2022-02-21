def main():
    ast = 0
    lines = int(input("Cuantas final de asteriscos quieres?"))
    for i in range(lines):
        ast += 1
        print("*" * (ast))


if __name__ == "__main__":
    main()