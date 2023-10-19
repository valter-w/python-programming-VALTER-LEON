from shape3d import Shape3D

class Cube(Shape3D):
    """Represents a cube in a three-dimensional space."""
    def __init__(self, x=0, y=0, z=0, side_length=1):
        """Initialize a cube of given length with its center at (x,y,z)"""
        super().__init__(x, y, z)

        if not Shape3D._is_numeric(side_length):
            raise TypeError("argument 'side_length' must be of type 'int' or 'float'")
        elif side_length <= 0:
            raise ValueError("argument 'side_length' must be > 0")
        else:
            self._side_length = side_length

    def __repr__(self):
        return (f"Cube(x={self.x}, y={self.y}, z={self.z}, "
                f"side_length={self.side_length})"
        )
    
    def __str__(self):
        return (f"cube with a side length of {self.side_length}"
                f" and its center at ({self.x},{self.y},{self.z})"
        )
    
    def __eq__(self, other):
        """Checks if two cubes are of equal size, regardless of coordinates."""
        return isinstance(other, Cube) and self.side_length == other.side_length
    
    def is_inside(self, x, y, z):
        """Checks if a point (x,y,z) is within the cube's body."""
        # let super class check argument type
        super().is_inside(x, y, z)
        
        half_length = self.side_length / 2
        within_x = (self.x - half_length) < x < (self.x +  half_length)
        within_y = (self.y -  half_length) < y < (self.y +  half_length)
        within_z = (self.z -  half_length) < z < (self.z +  half_length)
        return within_x and within_y and within_z
    
    @property
    def area(self):
        # sum the area of cube's 6 sides
        return 6 * self.side_length**2
    
    @property
    def side_length(self):
        return self._side_length
    
    @property
    def volume(self):
        return self.side_length**3