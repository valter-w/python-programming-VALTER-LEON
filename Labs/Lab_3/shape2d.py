class Shape2D:
    def __init__(self, x=0, y=0):
        self.translate(x, y)

    def __repr__(self):
        return f"Shape2D(x={self._x}, y={self._y})"
    
    def __add__(self, other):
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
        return self.__add__(other)
    
    def __sub__(self, other):
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
        return self.__sub__(other)
    
    def __lt__(self, other):
        Shape2D._check_operands(self, other, "<")
        return self.area < other.area
    
    def __le__(self, other):
        Shape2D._check_operands(self, other, "<=")
        return self.area <= other.area
    
    def __gt__(self, other):
        Shape2D._check_operands(self, other, ">")
        return self.area > other.area
    
    def __ge__(self, other):
        Shape2D._check_operands(self, other, ">=")
        return self.area >= other.area

    def _is_numeric(arg):
        return type(arg) in [int, float]
    
    # Use dunder attribute __name__ to get objects class name 
    # for error message
    # Source: https://sparkbyexamples.com/python/getting-the-class-name-of-an-instance/
    def _check_operands(l_operand, r_operand, operator):
        if not isinstance(r_operand, Shape2D):
            raise TypeError(f"unsupported operand type(s) for {operator}: "
                            f"'{type(l_operand).__name__}' and "
                            f"'{type(r_operand).__name__}'"
            )
    
    def area(self):
        return 0

    def is_inside(self, x, y):
        # checking types, useful for subclasses:
        if not Shape2D._is_numeric(x):
            raise TypeError("both arguments must be of type 'int' or 'float'")
        
        if not Shape2D._is_numeric(y):
            raise TypeError("both arguments must be of type 'int' or 'float'")

        return False
    
    def perimeter(self):
        return 0

    def translate(self, x, y):
        if not Shape2D._is_numeric(x):
            raise TypeError("argument 'x' must be of type 'int' or 'float'")
        self._x = x

        if not Shape2D._is_numeric(y):
            raise TypeError("argument 'y' must be of type 'int' or 'float'")
        self._y = y

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y