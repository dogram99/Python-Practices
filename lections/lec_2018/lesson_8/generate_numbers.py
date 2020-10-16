def main():
    generate_numbers(2, 4)


def generate_numbers(N: int, M: int, prefix=None):
    """ Генерирует все числа (с лидирующими незначащими нулями)
    в N-ричной системе счисления (N <= 10)
    длины M
    """
    if M == 0:
        print(prefix)
        return
    prefix = prefix or []
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M - 1, prefix)
        prefix.pop()


main()
