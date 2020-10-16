def check_sorted(A, ascending=True):
    """Проверка отсортированности за O(len(a))"""
    flag = True
    N = len(A)
    s = 2 * int(ascending) - 1
    for i in range(0, N - 1):
        if s * A[i] > s * A[i + 1]:
            flag = False
            break
    return flag


A = [6, 1, 3, 7, 4, 9, 4, 2]
res = check_sorted(A)
print(res)
