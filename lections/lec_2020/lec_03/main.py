def main():
    res = foo(123)
    print(res)


def foo(x: int) -> str:
    return 'Default x = ' + str(type(x)) + ' Return x = ' + str(type(str(x))) + '=' + str(x)


if __name__ == '__main__':
    main()
