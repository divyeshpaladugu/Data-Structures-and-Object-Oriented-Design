import unittest
from mod4.Stack import Stack

class TestStack(unittest.TestCase):
    def test_init(self):
        """"""
        s = Stack()
        self.assertEqual(len(s), 0)
        self.assertTrue(s.is_empty())







unittest.main()