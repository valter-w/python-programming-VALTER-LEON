class Shape2D:
    """A super class for classes representing shapes in a 2D space."""
    def __init__(self, x=0, y=0):
        """Initializes a new shape with its center at (x,y)."""
        self.translate(x, y)

    def __repr__(self):
        return f"Shape2D(x={self._x}, y={self._y})"
    
    def __str__(self):
        return f"two-dimensional shape with its center at ({self.x},{self.y})"
    
    def __add__(self, other):
        """Adds the area of two shapes or a shape's area and a number."""
        if isinstance(other, Shape2D):
            return self.area + other.area
        elif Shape2D._is_numeric(other):
            return self.area + other
        else:
            raise TypeError(f"unsupported operand type(s) for +: "
                            f"'{type(self).__name__}' and "
                            f"'{type(other).__name__}'"
            )
        
    def __radd__(self, other):
        """Adds the area of two shapes or a shape's area and a number."""
        return self.__add__(other)
    
    def __sub__(self, other):
        """Subtracts area with another shape's area, or a number."""
        if isinstance(other, Shape2D):
            return self.area - other.area
        elif Shape2D._is_numeric(other):
            return self.area - other
        else:
            raise TypeError(f"unsupported operand type(s) for -: "
                            f"'{type(self).__name__}' and "
                            f"'{type(other).__name__}'"
            )
        
    def __rsub__(self, other):
        """Subtracts another shape's area, or a number, with area."""
        return self.__sub__(other)
    
    def __lt__(self, other):
        """Compares area of two shapes."""
        Shape2D._check_operands(self, other, "<")
        return self.area < other.area
    
    def __le__(self, other):
        """Compares area of two shapes."""
        Shape2D._check_operands(self, other, "<=")
        return self.area <= other.area
    
    def __gt__(self, other):
        """Compares area of two shapes."""
        Shape2D._check_operands(self, other, ">")
        return self.area > other.area
    
    def __ge__(self, other):
        """Compares area of two shapes."""
        Shape2D._check_operands(self, other, ">=")
        return self.area >= other.area

    def _is_numeric(arg):
        return type(arg) in [int, float]
    
    # Helpful function for overloaded comparison operators
    def _check_operands(l_operand, r_operand, operator):
        # Use dunder attribute typ(obj).__name__ to get an objects's 
        # class name a helpful for error message
        # Source: https://sparkbyexamples.com/python/getting-the-class-name-of-an-instance/
        if not isinstance(r_operand, Shape2D):
            raise TypeError(f"unsupported operand type(s) for {operator}: "
                            f"'{type(l_operand).__name__}' and "
                            f"'{type(r_operand).__name__}'"
            )

    def is_inside(self, x, y):
        """Checks if a point (x, y) are within the shape."""
        # checking types, useful for subclasses:
        if not Shape2D._is_numeric(x):
            raise TypeError("both arguments must be of type 'int' or 'float'")
        
        if not Shape2D._is_numeric(y):
            raise TypeError("both arguments must be of type 'int' or 'float'")

        return False
    


    def translate(self, x, y):
        """Changes the (x,y) coordinates of the shape."""
        if not Shape2D._is_numeric(x):
            raise TypeError("argument 'x' must be of type 'int' or 'float'")
        self._x = x

        if not Shape2D._is_numeric(y):
            raise TypeError("argument 'y' must be of type 'int' or 'float'")
        self._y = y

    @property
    def perimeter(self):
        return 0

    @property
    def area(self):
        return 0

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y