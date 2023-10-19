class Shape3D:
    """A super class for classes representing shapes in a 3D space."""
    def __init__(self, x=0, y=0, z=0):
        """Initializes a new shape with its center at (x,y,z)."""
        self.translate(x, y, z)

    def __repr__(self):
        return f"Shape3D(x={self.x}, y={self.y}, z={self.z})"
    
    def __str__(self):
        return ("three-dimensional shape with its center at "
                f"({self.x},{self.y},{self.z})"
        )
    
    def __add__(self, other):
        """Adds the volume of two shapes or a shape's volume and a number."""
        if isinstance(other, Shape3D):
            return self.volume + other.volume
        elif Shape3D._is_numeric(other):
            return self.volume + other
        else:
            raise TypeError(f"unsupported operand type(s) for +: "
                            f"'{type(self).__name__}' and "
                            f"'{type(other).__name__}'"
            )
        
    def __radd__(self, other):
        """Adds the volume of two shapes or a shape's volume and a number."""
        return self.__add__(other)
    
    def __sub__(self, other):
        """Subtracts volume with another shape's volume, or a number."""
        if isinstance(other, Shape3D):
            return self.volume - other.volume
        elif Shape3D._is_numeric(other):
            return self.volume - other
        else:
            raise TypeError(f"unsupported operand type(s) for -: "
                            f"'{type(self).__name__}' and "
                            f"'{type(other).__name__}'"
            )
        
    def __rsub__(self, other):
        """Subtracts volume with another shape's volume, or a number."""
        return self.__sub__(other)
    
    def __lt__(self, other):
        """Compares volume of two shapes."""
        Shape3D._check_operands(self, other, "<")
        return self.volume < other.volume
    
    def __le__(self, other):
        """Compares volume of two shapes."""
        Shape3D._check_operands(self, other, "<=")
        return self.volume <= other.volume
    
    def __gt__(self, other):
        """Compares volume of two shapes."""
        Shape3D._check_operands(self, other, ">")
        return self.volume > other.volume
    
    def __ge__(self, other):
        """Compares volume of two shapes."""
        Shape3D._check_operands(self, other, ">=")
        return self.volume >= other.volume

    def _is_numeric(arg):
        return type(arg) in [int, float]
    
    
    def _check_operands(l_operand, r_operand, operator):
        # Use dunder attribute typ(obj).__name__ to get an objects's 
        # class name a helpful for error message
        # Source: https://sparkbyexamples.com/python/getting-the-class-name-of-an-instance/
        if not isinstance(r_operand, Shape3D):
            raise TypeError(f"unsupported operand type(s) for {operator}: "
                            f"'{type(l_operand).__name__}' and "
                            f"'{type(r_operand).__name__}'"
            )

    def is_inside(self, x, y, z):
        """Checks if a point (x,y,z) are within the shape."""
        # checking types, useful for subclasses:
        if not Shape3D._is_numeric(x):
            raise TypeError("all 3 arguments must be of type 'int' or 'float'")
        
        if not Shape3D._is_numeric(y):
            raise TypeError("all 3 arguments must be of type 'int' or 'float'")
        
        if not Shape3D._is_numeric(z):
            raise TypeError("all 3 arguments must be of type 'int' or 'float'")

        return False
    


    def translate(self, x, y, z):
        """Changes the (x,y,z) coordinates of the shape."""
        if not Shape3D._is_numeric(x):
            raise TypeError("argument 'x' must be of type 'int' or 'float'")
        self._x = x

        if not Shape3D._is_numeric(y):
            raise TypeError("argument 'y' must be of type 'int' or 'float'")
        self._y = y

        if not Shape3D._is_numeric(z):
            raise TypeError("argument 'z' must be of type 'int' or 'float'")
        self._z = z


    @property
    def area(self):
        return 0
    
    @property
    def volume(self):
        return 0

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z