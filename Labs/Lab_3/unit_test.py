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
    assert not rectangle_1.is_inside(-1, 1), "The point (1,1) should not be inside 'rectangle_1'."

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