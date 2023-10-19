from circle import Circle
from rectangle import Rectangle
from sphere import Sphere
from cube import Cube
import math

def test_circle():
    circle_1 = Circle()
    circle_2 = Circle(x=2, y=-2, radius=1)
    assert circle_1 == circle_2, "equality check (==) failed"
    assert not circle_1 < circle_2, "< comparison failed"
    assert not circle_1 > circle_2, "> comparison failed"

    big_circle = Circle(radius=2)
    assert circle_1 != big_circle, "inequality check (!=) failed"
    assert circle_1 < big_circle, "< comparison failed"
    assert circle_1 <= big_circle, "<= comparison failed"
    assert not circle_1 > big_circle, "> comparison failed"
    assert not circle_1 >= big_circle, ">= comparison failed"

    assert circle_1.is_unit_circle(), "unit circle not identified"
    assert not circle_2.is_unit_circle(), "unit circle incorrectly identified"
    assert not big_circle.is_unit_circle(), "unit circle incorrectly identified"

    assert circle_1.is_inside(0.5, 0.5), "point not recognized as inside shape"
    assert circle_1.is_inside(-0.5, -0.5), "point not recognized as inside shape"
    assert not circle_1.is_inside(1, 1), "point incorrectly recognized as inside shape"
    assert not circle_1.is_inside(-1, -1), "point incorrectly recognized as inside shape"
    circle_1.translate(20, 20)
    assert not circle_1.is_inside(0.5, 0.5), "point incorrectly recognized as inside shape"
    
    # rectangle will have same area as circle_1
    rectangle = Rectangle(width=1, height=math.pi)
    assert rectangle.area == circle_1.area, "equality check (==) of different 2D shapes failed"
    assert rectangle != circle_1, "inequality check (!=) failed"



def test_rectangle():
    rectangle_1 = Rectangle()
    rectangle_2 = Rectangle(x=2, y=-2)
    assert rectangle_1 == rectangle_2, "equality check (==) failed"
    assert not rectangle_1 < rectangle_2, "< comparison failed"
    assert not rectangle_1 > rectangle_2, "> comparison failed"

    big_rectangle = Rectangle(width=2, height=2)
    assert rectangle_1 != big_rectangle, "inequality check (!=) failed"
    assert rectangle_1 < big_rectangle, "< comparison failed"
    assert rectangle_1 <= big_rectangle, "<= comparison failed"
    assert not rectangle_1 > big_rectangle, "> comparison failed"
    assert not rectangle_1 >= big_rectangle, ">= comparison failed"

    assert rectangle_1.is_inside(0.25, 0.25), "point not recognized as inside shape"
    assert rectangle_1.is_inside(-0.25, -0.25), "point not recognized as inside shape"
    assert not rectangle_1.is_inside(1, 1), "point incorrectly recognized as inside shape"
    assert not rectangle_1.is_inside(-1, -1), "point incorrectly recognized as inside shape"
    rectangle_1.translate(20, 20)
    assert not rectangle_1.is_inside(0.5, 0.5), "point incorrectly recognized as inside shape"

    assert rectangle_1.is_square(), "rectangle not recognized as a square"
    assert not Rectangle(width=1, height=2).is_square(), "rectangle incorrectly recognized as a square"

    # two rectangles with same area but different proportions
    assert Rectangle(width=1, height=2) != Rectangle(width=2, height=1), "equality check (==) failed"



def test_area_operators():
    """Test '+' and '-' operators with two-dimensional shapes"""
    unit_circle = Circle(radius=1)
    assert unit_circle + 100 == unit_circle.area + 100, "addition (+) failed"
    assert unit_circle + unit_circle == 2 * math.pi, "addition (+) failed"

    assert unit_circle - math.pi == 0, "subtraction (-) failed"
    assert unit_circle - unit_circle == 0, "subtraction (-) failed"



def test_sphere():
    sphere_1 = Sphere(radius=1)
    sphere_2 = Sphere(x=2, y=-2, z=10, radius=1)
    assert sphere_1 == sphere_2, "equality check (==) failed"
    assert not sphere_1 < sphere_2, "< comparison failed"
    assert not sphere_1 > sphere_2, "> comparison failed"

    big_sphere = Sphere(radius=2)
    assert sphere_1 != big_sphere, "inequality check (!=) failed"
    assert sphere_1 < big_sphere, "< comparison failed"
    assert sphere_1 <= big_sphere, "<= comparison failed"
    assert not sphere_1 > big_sphere, "> comparison failed"
    assert not sphere_1 >= big_sphere, ">= comparison failed"

    assert sphere_1.is_inside(0.5, 0.5, 0.5), "point not recognized as inside shape"
    assert sphere_1.is_inside(-0.5, -0.5, +0.5), "point not recognized as inside shape"
    assert not sphere_1.is_inside(1, 1, 1), "point incorrectly recognized as inside shape"
    assert not sphere_1.is_inside(-1, -1, -1), "point incorrectly recognized as inside shape"
    sphere_1.translate(20, 20, 20)
    assert not sphere_1.is_inside(0.5, 0.5, 0.5), "point incorrectly recognized as inside shape"



def test_cube():
    cube_1 = Cube(side_length=1)
    cube_2 = Cube(x=2, y=-2, z=10, side_length=1)
    assert cube_1 == cube_2, "equality check (==) failed"
    assert not cube_1 < cube_2, "< comparison failed"
    assert not cube_1 > cube_2, "> comparison failed"

    big_cube = Cube(side_length=2)
    assert cube_1 != big_cube, "inequality check (!=) failed"
    assert cube_1 < big_cube, "< comparison failed"
    assert cube_1 <= big_cube, "<= comparison failed"
    assert not cube_1 > big_cube, "> comparison failed"
    assert not cube_1 >= big_cube, ">= comparison failed"

    assert cube_1.is_inside(0.25, 0.25, 0.25), "point not recognized as inside shape"
    assert cube_1.is_inside(-0.25, -0.25, -0.25), "point not recognized as inside shape"
    assert not cube_1.is_inside(1, 1, 1), "point incorrectly recognized as inside shape"
    assert not cube_1.is_inside(-1, -1, 1), "point incorrectly recognized as inside shape"
    cube_1.translate(20, 20, 20)
    assert not cube_1.is_inside(0.5, 0.5, 0.5), "point incorrectly recognized as inside shape"



def test_volume_operators():
    """Test '+' and '-' operators with three-dimensional shapes"""
    sphere = Sphere(radius=1)
    assert sphere + 100 == sphere.volume + 100, "addition (+) failed"
    assert sphere + sphere == (8 * math.pi)/3, "addition (+) failed"

    assert sphere - (4 * math.pi)/3 == 0, "subtraction (-) failed"
    assert sphere - sphere == 0, "subtraction (-) failed"