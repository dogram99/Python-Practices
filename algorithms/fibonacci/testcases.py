import algorithms.fibonacci.first_var as fibonacci


def test_fibonacci(fib):
    print('\nТестируем:', fib.__doc__)

    print('testcase #1: ', end='')
    f = 5
    f_fib = [1, 2, 3, 5]
    f = fib(f)
    print('Ok' if f == f_fib else 'Fail')

    print('testcase #2: ', end='')
    f = 10
    f_fib = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    f = fib(f)
    print('Ok' if f == f_fib else 'Fail')

    print('testcase #3: ', end='')
    f = -1
    f_fib = [1]
    f = fib(f)
    print('Ok' if f == f_fib else 'Fail')


test_fibonacci(fibonacci.f)
