from circle import Circle
from rectangle import Rectangle
from sphere import Sphere
from cube import Cube
import math

def test_circle():
    circle_1 = Circle()
    circle_2 = Circle(x=2, y=-2, radius=1)
    assert circle_1 == circle_2, "Two circles of equal size are equal, regardless of coordinates."
    assert not circle_1 < circle_2, "A circle is not less than another cirle of the same size."
    assert not circle_1 > circle_2, "A circle is not greater than another cirle of the same size."

    big_circle = Circle(radius=2)
    assert circle_1 != big_circle, "Two circles of different size are not equal."
    assert circle_1 < big_circle, "A smaller circle is less than a larger circle."
    assert circle_1 <= big_circle, "A smaller circle is less than or equal to a larger circle."
    assert not circle_1 > big_circle, "A smaller circle is not greater than a larger circle."
    assert not circle_1 >= big_circle, "A smaller circle is not greater than or equal to a larger circle."

    assert circle_1.is_unit_circle(), "A circle with radius 1 (unit) and center at (0, 0) is a unit circle."
    assert not circle_2.is_unit_circle(), "A circle with its center NOT at (0,0) is not a unit circle."
    assert not big_circle.is_unit_circle(), "A circle with a radius other than 1 (unit) is not a unit circle."

    assert circle_1.is_inside(0.5, 0.5), "The point (0.5,0.5) should be inside 'circle_1'."
    assert circle_1.is_inside(-0.5, -0.5), "The point (-0.5,-0.5) should be inside 'circle_1'."
    assert not circle_1.is_inside(1, 1), "The point (1,1) should not be inside 'circle_1'."
    assert not circle_1.is_inside(-1, -1), "The point (-1,-1) should not be inside 'circle_1'."
    
    
    rectangle = Rectangle(width=1, height=math.pi)
    assert rectangle.area == circle_1.area, "'rectangle' and 'circle_1' should have the same area."
    assert rectangle != circle_1, "A circle and rectangle should not be considered equal, even though they have the same area."



def test_rectangle():
    rectangle_1 = Rectangle()
    rectangle_2 = Rectangle(x=2, y=-2)
    assert rectangle_1 == rectangle_2, "Two rectangle of equal size should be considered equal regardless of coordinates."
    assert not rectangle_1 < rectangle_2, "A rectangle should not be considered less than another rectangle with the same area."
    assert not rectangle_1 > rectangle_2, "A rectangle should not be considered greater than another rectangle with the same area."

    big_rectangle = Rectangle(width=2, height=2)
    assert rectangle_1 != big_rectangle, "Two rectangles with different areas should be considered inequal."
    assert rectangle_1 < big_rectangle, "A rectangle with smaller area should be considered less than a rectangle with larger area."
    assert rectangle_1 <= big_rectangle, "A rectangle with smaller area should be considered less than or equal to a rectangle with larger area."
    assert not rectangle_1 > big_rectangle, "A rectangle with smaller area shoul not be considered greater than a rectangle with larger area."
    assert not rectangle_1 >= big_rectangle, "A rectangle with smaller area shoul not be considered greater than or equal to a rectangle with larger area."

    assert rectangle_1.is_inside(0.25, 0.25), "The point (0.25,0.25) should be inside 'rectangle_1'."
    assert rectangle_1.is_inside(-0.25, -0.25), "The point (-0.25,-0.25) should be inside 'rectangle_1'."
    assert not rectangle_1.is_inside(1, 1), "The point (1,1) should not be inside 'rectangle_1'."
    assert not rectangle_1.is_inside(-1, -1), "The point (-1,-1) should not be inside 'rectangle_1'."

    assert rectangle_1.is_square(), "A rectangle with the same width and height is a square."
    assert not Rectangle(width=1, height=2).is_square(), "A rectangle with different width and height is not a square."

    assert Rectangle(width=1, height=2) != Rectangle(width=2, height=1), "Equal rectangles must have equal proportions (and area)."



def test_area_operators():
    """Test '+' and '-' operators with two-dimensional shapes"""
    unit_circle = Circle(radius=1)
    assert unit_circle + 100 == unit_circle.area + 100, "When adding a number to a 2D shape, the number should be added to the shape's area."
    assert unit_circle + unit_circle == 2 * math.pi, "When adding two 2D shapes, their areas should be added."

    assert unit_circle - math.pi == 0, "When subtracting a number from a 2D shape, the number should be subtracted from the shape's area."
    assert unit_circle - unit_circle == 0, "When subtracting one 2D shape from another, it's the area that should be subtracted."



def test_sphere():
    sphere_1 = Sphere(radius=1)
    sphere_2 = Sphere(x=2, y=-2, z=10, radius=1)
    assert sphere_1 == sphere_2, "Two spheres of equal size are equal, regardless of coordinates."
    assert not sphere_1 < sphere_2, "A sphere is not less than another sphere of the same size."
    assert not sphere_1 > sphere_2, "A sphere is not greater than another sphere of the same size."

    big_sphere = Sphere(radius=2)
    assert sphere_1 != big_sphere, "Two spheres of different size are not equal."
    assert sphere_1 < big_sphere, "A smaller sphere is less than a larger sphere."
    assert sphere_1 <= big_sphere, "A smaller sphere is less than or equal to a larger sphere."
    assert not sphere_1 > big_sphere, "A smaller sphere is not greater than a larger sphere."
    assert not sphere_1 >= big_sphere, "A smaller sphere is not greater than or equal to a larger sphere."

    assert sphere_1.is_inside(0.5, 0.5, 0.5), "The point (0.5,0.5,0.5) should be inside 'sphere_1'."
    assert sphere_1.is_inside(-0.5, -0.5, +0.5), "The point (-0.5,-0.5,-0.5) should be inside 'sphere_1'."
    assert not sphere_1.is_inside(1, 1, 1), "The point (1,1,1) should not be inside 'sphere_1'."
    assert not sphere_1.is_inside(-1, -1, -1), "The point (-1,-1,-1) should not be inside 'sphere_1'."



def test_cube():
    cube_1 = Cube(side_length=1)
    cube_2 = Cube(x=2, y=-2, z=10, side_length=1)
    assert cube_1 == cube_2, "Two cubes of equal size should be considered equal regardless of coordinates."
    assert not cube_1 < cube_2, "A cube should not be considered less than another cube of the same size"
    assert not cube_1 > cube_2, "A cube should not be considered greater than another cube of the same size."

    big_cube = Cube(side_length=2)
    assert cube_1 != big_cube, "Two cubes of different size are inequal."
    assert cube_1 < big_cube, "A smaller cube is less than a larger cube."
    assert cube_1 <= big_cube, "A smaller cube is less than or equal to a larger cube."
    assert not cube_1 > big_cube, "A smaller cube is not greater than a larger cube."
    assert not cube_1 >= big_cube, "A smaller cube is not greater than or equal to a larger cube"

    assert cube_1.is_inside(0.25, 0.25, 0.25), "The point (0.25,0.25) should be inside 'cube_1'."
    assert cube_1.is_inside(-0.25, -0.25, -0.25), "The point (-0.25,-0.25,-0.25) should be inside 'cube_1'."
    assert not cube_1.is_inside(1, 1, 1), "The point (1,1,1) should not be inside 'cube_1'."
    assert not cube_1.is_inside(-1, -1, 1), "The point (-1,-1,-1) should not be inside 'cube_1'."



def test_volume_operators():
    """Test '+' and '-' operators with three-dimensional shapes"""
    sphere = Sphere(radius=1)
    assert sphere + 100 == sphere.volume + 100, "When adding a number to a 3D shape, the number should be added to the shape's volume."
    assert sphere + sphere == (8 * math.pi)/3, "When adding two 3D shapes, their volumes should be added."

    assert sphere - (4 * math.pi)/3 == 0, "When subtracting a number from a 3D shape, the number should be subtracted from the shape's volume."
    assert sphere - sphere == 0, "When subtracting one 3D shape from another, it's the volume that should be subtracted."