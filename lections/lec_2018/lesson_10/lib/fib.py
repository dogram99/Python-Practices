def bad_ex_fib(n):
    if n <= 1:
        return n
    return bad_ex_fib(n - 1) + bad_ex_fib(n - 2)


# print(bad_ex_fib(5))


def fun_fib(n: int):
    fib = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
        print(fib[i])
    return fib[n]


fun_fib(6)
