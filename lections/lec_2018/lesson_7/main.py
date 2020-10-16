def main():
    matryoshka(10)
    print('Факториал:')
    print(f(5))
    print('Алгоритм Евклида:')
    print(gcd(3, 3))
    print(gcd(6, 3))
    print(gcd(3, 6))
    print('Возведение в степень:')
    print(pow(2, 69))
    print(pow(2.10, 3))
    print('Ханойские башни:')
    print(test(2, 2, 2))


def matryoshka(n):
    if n == 1:
        print('Матрёшечка')
    else:
        print('Вверх матрёшки n=', n)
        matryoshka(n - 1)
        print('Низ матрёшки n=', n)


def f(n: int):
    assert n >= 0, 'Факториал отр. не определен'
    if n == 0:
        return 1

    return f(n - 1) * n


def gcd(a: int, b: int):
    return a if b == 0 else gcd(b, a % b)


def pow(a: float, n: int):
    assert n >= 0, 'Степень должна быть положительная'
    if n == 0:
        return 1
    elif n % 2 == 1:
        return a * pow(a, n - 1)
    else:  # n - четное
        return pow(a ** 2, n // 2)


def test(k: int, i: int, tmp: int):
    tmp = 6 - k - i
    return tmp


main()
