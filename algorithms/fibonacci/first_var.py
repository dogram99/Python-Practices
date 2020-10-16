def f(n: int):
    """Вычисление чисел Фибоначчи"""
    array = []
    start_numb = f1 = f2 = 1
    array.append(start_numb)

    for i in range(2, n):
        f1, f2, = f2, f1 + f2
        array.append(f2)

    return array


print(f(8))
