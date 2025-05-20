import unittest
import random
from SeparateChainingHashTable import SeparateChainingHashTable
from LinearProbingHashTable import LinearProbingHashTable

class TestHashTableFactory:
    def test_put_get_sequential(self):
        """Test put and get operations sequentially."""
        hash_table = self.create_hash_table()
        keys = list(range(100))
        for key in keys:
            hash_table[key] = key
        for key in keys:
            self.assertEqual(hash_table[key], key)

    def test_put_get_remove_sequential(self):
        """Test put, get, and remove operations sequentially."""
        hash_table = self.create_hash_table()
        keys = list(range(100))
        for key in keys:
            hash_table[key] = key
        for key in keys:
            self.assertEqual(hash_table[key], key)
        for key in keys:
            del hash_table[key]
            with self.assertRaises(KeyError):
                _ = hash_table[key]

    def create_hash_table(self):
        """Create a hash table instance."""
        raise NotImplementedError("create_hash_table method not implemented in TestHashTableFactory")

class TestSeparateChainingHashTable(unittest.TestCase, TestHashTableFactory):
    """Test cases for SeparateChainingHashTable."""
    def create_hash_table(self):
        return SeparateChainingHashTable()

class TestLinearProbingHashTable(unittest.TestCase, TestHashTableFactory):
    """Test cases for LinearProbingHashTable."""
    def create_hash_table(self):
        return LinearProbingHashTable()

if __name__ == '__main__':
    unittest.main()