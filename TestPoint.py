import unittest
from Point import Point # import class Point from file Point.py

class TestPoint(unittest.TestCase):
    def setUp(self):
        """Create some points for future tests"""
        self.p1 = Point(3, 4)
        self.p2 = Point(5, 6)
        self.p3 = Point(4, 3)
    def test_init(self):
        """Tests that points are initialied with the correct attributes"""
        self.assertEqual(self.p1.x, 3)
        self.assertEqual(self.p1.y, 4)
        self.assertEqual(self.p2.x, 5)
        self.assertEqual(self.p2.y, 6)
    
    def test_eq(self):
        """Tests that self and other are equal"""
        self.assertEqual(self.p1, self.p1)
        self.assertNotEqual(self.p1, self.p2)


    def test_equidistant(self):
        """Tests if two points are equivalent distance from the origin"""
        self.assertEqual(self.p1.equidistant(self.p1), True)
        self.assertEqual(self.p1.equidistant(self.p3), True)
        self.assertNotEqual(self.p1.equidistant(self.p2), True)

    def test_within(self):
        """Tests if self and other are within distance from each other"""
        self.assertEqual(self.p1.within(0, self.p1), True)
        self.assertNotEqual(self.p1.within(0, self.p2), True)


if __name__ == '__main__':
    unittest.main()