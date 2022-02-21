def medir_largos(iterables, *args, sumar_todo=False):
    if args:
        largos = [len(iterables)]
        for a in args:
            largos.append(len(a))
        if sumar_todo:
            largos = max(largos)
        return largos
    return len(iterables)


def main():
    print(medir_largos("hola"))
    print(medir_largos("hola", "como", "estas", "?", sumar_todo=True))


if __name__ == '__main__':
    main()
