def foo():
    return foo2()


def foo2():
    return foo3()


def foo3():
    return 3


if __name__ == '__main__':
    print(foo())
