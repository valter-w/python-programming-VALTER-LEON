from shape2d import Shape2D
import math

class Circle(Shape2D):
    """Represents a circle in a two-dimensional space."""
    def __init__(self, x=0, y=0, radius=1):
        """Initializes a circle of given radius with its center at (x,y)"""
        super().__init__(x, y)

        if not Shape2D._is_numeric(radius):
            raise TypeError("argument 'radius' must be of type 'int' or 'float'")
        elif radius <= 0:
            raise ValueError("argument 'radius' must be > 0")
        else:
            self._radius = radius

    def __repr__(self):
        return f"Circle(x={self.x}, y={self.y}, radius={self.radius})"
    
    def __str__(self):
        return (f"circle with a radius {self.radius}"
                f" with its center at ({self.x},{self.y})"
        )
    
    def __eq__(self, other):
        """Checks if two circles are of equal radius, regardless of coordinates."""
        return isinstance(other, Circle) and self.radius == other.radius
    
    def is_inside(self, x, y):
        """Checks if a point (x,y) are within the cirle's area."""
        # let super class check arguments' types
        super().is_inside(x, y)
        
        # calculate Euclidean distance in a 2D space
        delta_x = self.x - x
        delta_y = self.y - y
        distance = math.sqrt(delta_x**2 + delta_y**2)
        return distance < self.radius
    
    def is_unit_circle(self):
        return self.x == 0 and self.y == 0 and self.radius == 1

    @property
    def area(self):
        return math.pi * self._radius**2
    
    @property
    def circumference(self):
        return 2 * math.pi * self._radius
    
    @property
    def perimeter(self):
        return self.circumference()
        
    @property
    def radius(self):
        return self._radius
