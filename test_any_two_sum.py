import unittest
from any_two_sum import any_two_sum

class TestAnyTwoSum(unittest.TestCase):
    def test_any_two_sum_positive_case(self):
        self.assertTrue(any_two_sum([1, 3, 4, 5], 7))

    def test_any_two_sum_negative_case(self):
        self.assertFalse(any_two_sum([1, 3, 4, 5], 2))

    def test_any_two_sum_empty_input(self):
        self.assertFalse(any_two_sum([], 5))

    def test_any_two_sum_single_element(self):
        self.assertFalse(any_two_sum([1], 1))

    def test_any_two_sum_multiple_solutions(self):
        self.assertTrue(any_two_sum([2, 4, 3, 1, 5, 6], 10))

    def test_any_two_sum_duplicate_elements(self):
        self.assertTrue(any_two_sum([3, 3, 4, 2], 6))

if __name__ == '__main__':
    unittest.main()