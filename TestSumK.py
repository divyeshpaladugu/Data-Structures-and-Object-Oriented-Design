import unittest
from mod2.sum_k import sum_k
#from file import class
#from file improt method

class TestSumK(unittest.TestCase):
    def test_basic_behavior(self):
        """Verify sum_k works with some low positive ints"""
        self.assertEqual(sum_k(1), 1)
        self.assertEqual(sum_k(2), 3)
        self.assertEqual(sum_k(3), 6)
        self.assertEqual(sum_k(4), 10)
        
        self.assertNotEqual(sum_k(4), 11)

    def test_zero(self):
        """Verifies correct reult with 0"""
        self.assertEqual(sum_k(0), 0)

    def tes_negative(self):
        """Verifies I get a value error if i pass in a negative"""
        self.assertRaises(ValueError, sum_k, -1)

unittest.main()