def f(n: int):
    """Факториал числа через цикл"""
    assert n >= 0, 'Факториал отр. не определен'
    if n == 0:
        return 1

    f = 1
    i = 0

    while i < n:
        i += 1
        f = f * i

    return f
