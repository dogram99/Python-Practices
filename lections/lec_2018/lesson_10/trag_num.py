def trajectories_num(n):
    k = [0, 1] + [0] * n
    for i in range(2, n + 1):
        k[i] = k[i - 2] + k[i - 1]
        print(k[i])
    return k[n]


def count_min_cost(n: int, price: list):
    c = [None, price[1], price[1] + price[2]] + [0] * (n - 2)
    for i in range(3, n + 1):
        c[i] = price[i] + min(c[i - 1], c[i - 2])
    return c[n]


# Так создавать двумерные массивы нельзя!!
# m = 3
# n = 3
# a = [[0] * m] * n
# print(a)

# Правильный способ создания двумерных массивов
m = 3
n = 3
a = [[0] * m for i in range(n)]
print(a)