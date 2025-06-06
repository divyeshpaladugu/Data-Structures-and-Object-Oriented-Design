import unittest
from mod2.factorial import factorial


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)

unittest.main()