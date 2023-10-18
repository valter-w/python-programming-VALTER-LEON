from shape2d import Shape2D

class Rectangle(Shape2D):
    def __init__(self, x=0, y=0, width=1, height=1):
        """Initializes a rectangle of size width * height with center at (x,y)"""
        super().__init__(x, y)

        if not Shape2D._is_numeric(width):
            raise TypeError("argument 'width' must be of type 'int' or 'float'")
        elif width <= 0:
            raise ValueError("argument 'width' must be > 0")
        else:
            self._width = width

        if not Shape2D._is_numeric(height):
            raise TypeError("argument 'height' must be of type 'int' or 'float'")
        elif height <= 0:
            raise ValueError("argument 'height' must be > 0")
        else:
            self._height = height

    def __repr__(self):
        return f"Rectangle(x={self.x}, y={self.y})"
    
    def __str__(self):
        return (f"rectangle of size {self.width} * {self.height}"
                f" with its center at ({self.x},{self.y})."
        )
    
    def __eq__(self, other):
        """Checks if two rectangles are of equal width and height."""
        return (
            isinstance(other, Rectangle) and
            self.width == other.width and
            self.height == other.height
        )
    
    def is_inside(self, x, y):
        """Checks if a point (x,y) are within the rectangles's area."""
        # let super class check argument type
        super().is_inside(x, y)

        within_x = (self.x - self.width/2) < x < (self.x + self.width/2)
        within_y = (self.y - self.height/2) < y < (self.y + self.height/2)
        return within_x and within_y

    def is_square(self):
        """Checks if width and height are equal."""
        return self.width == self.height
    
    @property
    def area(self):
        return self.width * self.height

    @property
    def height(self):
        return self._height
    
    @property
    def perimeter(self):
        return 2 * self.width + 2 * self.height
    
    @property
    def width(self):
        return self._width        