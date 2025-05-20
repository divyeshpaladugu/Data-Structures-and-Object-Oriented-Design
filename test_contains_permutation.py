import unittest
from contains_permutation import contains_permutation

class TestContainsPermutation(unittest.TestCase):
    def test_contains_permutation(self):
        self.assertTrue(contains_permutation('abcdef', 'cab'))
        self.assertTrue(contains_permutation('keyboard', 'boy'))
        self.assertFalse(contains_permutation('patriots', 'sit'))

    def test_contains_permutation_empty_input(self):
        self.assertFalse(contains_permutation('', 'abc'))

    def test_contains_permutation_empty_pattern(self):
        self.assertTrue(contains_permutation('abcdef', ''))

    def test_contains_permutation_input_shorter_than_pattern(self):
        self.assertFalse(contains_permutation('abc', 'abcd'))

    def test_contains_permutation_same_input_and_pattern(self):
        self.assertTrue(contains_permutation('abc', 'abc'))

    def test_contains_permutation_input_with_permutation_at_end(self):
        self.assertTrue(contains_permutation('xyzabc', 'abc'))

if __name__ == '__main__':
    unittest.main()