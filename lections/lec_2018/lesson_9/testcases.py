import lections.lec_2018.lesson_9.sorts.hoar as hoar


def test_sort():
    print('testcase #1: ', end='')
    list_for_sort = [4, 2, 5, 1, 3]
    sort_list = [1, 2, 3, 4, 5]
    hoar.sort(list_for_sort)
    print('Ok' if list_for_sort == sort_list else 'Fail')


if __name__ == '__main__':
    test_sort()
