from linkedlist import Node, LinkedList
import unittest

class TestNode(unittest.TestCase):
    def setUp(self):
        """Create a few nodes for testing"""
        self.node1 = Node('Jake')
        self.node2 = Node('Jake')
        self.node3 = Node('jake')

    def test_init(self):
        """Tests that we can construct new nodes w/ correct attributes"""
        self.assertEqual(self.node1.item, 'Jake')
        self.assertEqual(self.node1.link, None)

    def test_eq(self):
        """Tests that nodes are equal if they have the same items"""
        self.assertEqual(self.node1, self.node1)    # object is equal to itself
        self.assertEqual(self.node1, self.node2)    # objects with same items are equal
        self.assertNotEqual(self.node1, self.node3) # objects with different items (Jake vs jake) are not equal

    def test_repr(self):
        """Tests string representation"""
        self.assertEqual(repr(self.node1), "Node(Jake)")

class TestLinkedList(unittest.TestCase):

    def test_init_empty(self):
        """Initializes a new empty linked list"""
        LL1 = LinkedList()
        self.assertEqual(len(LL1), 0)
        self.assertIsNone(LL1.get_head())
        self.assertIsNone(LL1.get_tail())

    def test_addfirst(self):
        """Iteratively adds to end, then removes from front"""
        n = 100
        LL1 = LinkedList()
        
        for i in range(n):
            self.assertEqual(len(LL1), i)
            LL1.add_first(i)
            self.assertEqual(LL1.get_head(), i)
            self.assertEqual(LL1.get_tail(), 0)
        
        # expect: head -->Node(n-1)-->Node(n-2)-->...-->Node(2)-->Node(1)-->Node(0)
        #         tail -----------------------------------------------------^

    def test_addlast(self):
        """Iteratively adds to end, then removes from front"""
        n = 100
        LL1 = LinkedList()

        for i in range(n):
            self.assertEqual(len(LL1), i)
            LL1.add_last(i)
            self.assertEqual(LL1.get_head(), 0)
            self.assertEqual(LL1.get_tail(), i)
        
        # expect: head -->Node(0)-->Node(1)-->Node(2)-->...-->Node(n-1)
        #         tail ---------------------------------------^

    def test_init_items(self):
        """Initializes a new linked list with some items"""
        n = 100
        LL1 = LinkedList(range(n))
        # expect: head -->Node(0)-->Node(1)-->Node(2)-->...-->Node(n-1)
        #         tail ---------------------------------------^

        self.assertEqual(len(LL1), n)
        self.assertEqual(LL1.get_head(), 0)
        self.assertEqual(LL1.get_tail(), n-1)

        

    def test_removefirst(self):
        """Adds a few items"""
        n = 100
        LL1 = LinkedList(range(n))

        # expect: head -->Node(0)-->Node(1)-->Node(2)-->...-->Node(n-1)
        #         tail ---------------------------------------^
        for i in range(n):
            self.assertEqual(len(LL1), n-i)
            self.assertEqual(LL1.get_head(), i)
            self.assertEqual(LL1.get_tail(), n-1)
            self.assertEqual(LL1.remove_first(), i)
            

        self.assertIsNone(LL1.get_head())
        self.assertIsNone(LL1.get_tail())

    def test26_removefirst_empty(self):
        """Remove first from empty LinkedList"""
        LL1 = LinkedList()
        self.assertRaises(RuntimeError, LL1.remove_first)

    def test_removelast(self):
        """Adds a few items"""
        n = 100
        LL1 = LinkedList(range(n))

        # expect: head -->Node(0)-->Node(1)-->Node(2)-->...-->Node(n-1)
        #         tail ---------------------------------------^
        for i in range(n):
            self.assertEqual(len(LL1), n-i)
            self.assertEqual(LL1.get_head(), 0)
            self.assertEqual(LL1.get_tail(), n-1-i)
            self.assertEqual(LL1.remove_last(), n-1-i)

        self.assertIsNone(LL1.get_head())
        self.assertIsNone(LL1.get_tail())

    def test28_removefirst_empty(self):
        """Remove last from empty LinkedList"""
        LL1 = LinkedList()
        self.assertRaises(RuntimeError, LL1.remove_last)

if __name__ == '__main__':
    unittest.main()