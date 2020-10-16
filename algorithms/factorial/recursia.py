def f(n: int):
    """Факториал числа через рекурсию"""
    assert n >= 0, 'Факториал отр. не определен'
    if n == 0:
        return 1

    res = f(n - 1) * n
    return res
