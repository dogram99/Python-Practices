from random import randint


def main():
    array = []

    for i in range(randint(1, 5)):
        array.append(i)

    print(bytes(array))


if __name__ == '__main__':
    main()
