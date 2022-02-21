
def pregunta():
    pregunta = input("Estas seguro? [S/N]: ")
    if pregunta == "S":
        return True
    elif pregunta == "N":
        return False


def main():
    print(pregunta())


if __name__ == '__main__':
    main()