def increment(x: int):
    """
    Инкремент: обозначается двумя знаками плюс "++" и увеличивает значение переменной на 1.
    x = x + 1 or x += 1
    """
    while x < 10:
        x = x + 1
        print(x)


def decrement(x: int):
    """
    Декремент: обозначается двумя знаками минус "--" и уменьшает значение переменной на 1.
    x = x - 1 or x -= 1
    """
    while x > 0:
        x = x - 1
        print(x)


if __name__ == '__main__':
    increment(0)
    decrement(10)
