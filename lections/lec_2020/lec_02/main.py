def main():
    # sum =  a, b, c = 1, 2, 3
    # print(type(sum))

    # x, y = 1, 2
    # x, y = y, x
    # print(x, y)

    t = (1, 2, 3, 4, 5)
    a, b, *rest = t
    print(a, b)
    print(rest)
    # Поэлементная распаковка кортежа
    print(*t)


main()
