def sort(A: list):
    """Быстрая сортировка, сортировка Хоара, часто называемая qsort"""
    if len(A) <= 1:
        return
    barrier = A[0]
    L = []
    M = []
    R = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    k = 0
    sort(L)
    sort(R)
    for x in L + M + R:
        A[k] = x
        k += 1
