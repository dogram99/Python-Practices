import unittest
from lections.lec_2018.lesson_8.sorts.qsort import *


class MyTestCase(unittest.TestCase):
    def test_sort(self):
        self.assertTrue(True, False)
        list_for_sort = [4, 2, 5, 1, 3]
        sort_list = [1, 2, 3, 4, 5]


if __name__ == '__main__':
    unittest.main()
