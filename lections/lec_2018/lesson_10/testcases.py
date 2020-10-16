import lections.lec_2018.lesson_10.lib.binary_search as search


def test_find():
    print('testcase #1: ', end='')
    key = 7
    arr = [1, 3, 3, 5, 6, 6, 8, 9]
    left_bound = search.left_bound(arr, key)
    right_bound = search.right_bound(arr, key)
    print(left_bound, right_bound)
    print('Ok' if key > left_bound or key < right_bound else 'Fail')


if __name__ == '__main__':
    test_find()
