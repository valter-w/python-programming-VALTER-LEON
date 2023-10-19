from shape3d import Shape3D
import math

class Sphere(Shape3D):
    """Represents a sphere in a three-dimensional space."""
    def __init__(self, x=0, y=0, z=0, radius=1):
        """Initialize a sphere of given radius with its center at (x,y,z)"""
        super().__init__(x, y, z)

        if not Shape3D._is_numeric(radius):
            raise TypeError("argument 'radius' must be of type 'int' or 'float'")
        elif radius <= 0:
            raise ValueError("argument 'radius' must be > 0")
        else:
            self._radius = radius

    def __repr__(self):
        return f"Sphere(x={self.x}, y={self.y}, z={self.z}, radius={self.radius})"
    
    def __str__(self):
        return (f"sphere with a radius {self.radius}"
                f" and its center at ({self.x},{self.y},{self.z})"
        )
    
    def __eq__(self, other):
        """Checks if two spheres are of equal radius, regardless of coordinates."""
        return isinstance(other, Sphere) and self.radius == other.radius
    
    def is_inside(self, x, y, z):
        """Checks if a point (x,y) are within the cirle's area."""
        # let super class check argument type
        super().is_inside(x, y, z)
        
        delta_x = self.x - x
        delta_y = self.y - y
        delta_z = self.z - z
        distance = math.sqrt(delta_x**2 + delta_y**2 + delta_z**2)
        return distance < self.radius

    @property
    def area(self):
        return 4 * math.pi * self._radius**2
    
    @property
    def circumference(self):
        return 2 * math.pi * self._radius
        
    @property
    def radius(self):
        return self._radius
    
    @property
    def volume(self):
        return (4 * math.pi * self.radius**3) / 3