class Point:
    def __init__(self, x, y):
        """Initializes a 2-D point with x- and y- coordinates"""
        self.x = x
        self.y = y

    def __eq__(self, other):
        """Checks that self and other are equal"""
        return self.x == other.x and self.y == other.y

    def equidistant(self, other):
         """Checks if two points are equivalent distance from the origin"""
         return (self.x**2 + self.y**2)**(1/2) == (other.x**2 + other.y**2)**(1/2)

    def within(self, distance, other):
        """Checks if self and other are within distance from each other"""
        return distance >= ((other.x-self.x)**2+(other.y-self.y)**2)**(1/2)
