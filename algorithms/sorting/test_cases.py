from algorithms.sorting import insert, choise, bubble


def test_sort(sort_algorithm):
    print('\nТестируем:', sort_algorithm.__doc__)
    print('testcase #1: ', end='')
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print('Ok' if A == A_sorted else 'Fail')

    print('testcase #2: ', end='')
    B = list(range(10, 20)) + list(range(0, 10))
    B_sorted = list(range(20))
    sort_algorithm(B)
    print('Ok' if B == B_sorted else 'Fail')

    print('testcase #3: ', end='')
    C = [4, 2, 4, 2, 1]
    C_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(C)
    print('Ok' if C == C_sorted else 'Fail')


if __name__ == '__main__':
    test_sort(insert.sort)
    test_sort(choise.sort)
    test_sort(bubble.sort)
