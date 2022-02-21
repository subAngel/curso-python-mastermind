def isPar(num):
    if num%2 == 1:
        return False
    else:
        return True


def main():
    print(isPar(4))
    print(isPar(3))


if __name__ == "__main__":
    main()