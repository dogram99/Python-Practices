from practice1.factorial import *


def main():
    num_fib = f(5)
    print(num_fib)
    # fun(1, 2, 3, name='Alex')


def fun(*args, **kwargs):
    print(args)
    print(kwargs)


main()
