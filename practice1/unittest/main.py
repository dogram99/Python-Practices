import unittest
from practice1.factorial import *


class TestStringMethods(unittest.TestCase):

    def test_fib(self):
        self.assertEqual(f(5), 120)
        self.assertEqual(f(3), 6)


if __name__ == '__main__':
    unittest.main()
