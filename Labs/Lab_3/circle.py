from shape2d import Shape2D
import math

class Circle(Shape2D):
    def __init__(self, x=0, y=0, radius=1):
        super().__init__(x, y)

        if not Shape2D._is_numeric(radius):
            raise TypeError("argument 'radius' must be of type 'int' or 'float'")
        elif radius <= 0:
            raise ValueError("argument 'radius' must be > 0")
        else:
            self._radius = radius

    def __repr__(self):
        return f"Circle(x={self.x}, y={self.y}, radius={self.radius})"
    
    def __eq__(self, other):
        return (
            isinstance(other, Circle) and 
            self.radius == other.radius
        )
    
    def is_inside(self, x, y):
        # let super class check argument type
        super().is_inside(x, y)
        
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
