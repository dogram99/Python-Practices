import algorithms.factorial.cycle as cyc
import algorithms.factorial.recursia as rec


def test_factorial(factorial):
    print('\nТестируем:', factorial.__doc__)

    print('testcase #1: ', end='')
    n = 5
    n_factorial = 120
    n = factorial(n)
    print('Ok' if n == n_factorial else 'Fail')

    print('testcase #2: ', end='')
    n = 0
    n_factorial = 1
    n = factorial(n)
    print('Ok' if n == n_factorial else 'Fail')

    print('testcase #3: ', end='')
    n = 10
    n_factorial = 3628800
    n = factorial(n)
    print('Ok' if n == n_factorial else 'Fail')


test_factorial(cyc.f)
test_factorial(rec.f)
