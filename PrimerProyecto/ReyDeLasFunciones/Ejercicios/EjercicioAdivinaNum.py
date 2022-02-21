from random import randint


def adivina(num):
    num_user = int(input("adivina el numero: "))
    if num_user == num:
        print("Has adivinado!!")
    else:
        adivina(num)


def main():
    num = randint(1, 100)
    adivina(num)


if __name__ == '__main__':
    main()