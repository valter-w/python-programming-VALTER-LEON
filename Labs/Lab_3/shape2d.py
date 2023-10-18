class Shape2D:
    def __init__(self, x=0, y=0):
        self.translate(x, y)

    def __repr__(self):
        return f"Shape2D(x={self._x}, y={self._y})"

    def _is_numeric(arg):
        return type(arg) in [int, float]
    
    def area(self):
        return 0

    def is_inside(self, x, y):
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