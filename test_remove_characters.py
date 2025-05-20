import unittest
from remove_characters import remove_characters

class TestRemoveCharacters(unittest.TestCase):
    def test_remove_characters(self):
        self.assertEqual(remove_characters('abcd', 'c'), 'abd')

    def test_empty_input(self):
        self.assertEqual(remove_characters('', 'c'), '')

    def test_empty_to_remove(self):
        self.assertEqual(remove_characters('abcd', ''), 'abcd')

    def test_nothing_to_remove(self):
        self.assertEqual(remove_characters('abcd', 'efg'), 'abcd')

    def test_same_remove_and_input(self):
        self.assertEqual(remove_characters('abcd', 'abcd'), '')

if __name__ == '__main__':
    unittest.main()
