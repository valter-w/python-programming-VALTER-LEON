from circle import Circle
from rectangle import Rectangle
from sphere import Sphere
from cube import Cube
import math

def test_circle():
    circle_1 = Circle()
    circle_2 = Circle(x=2, y=-2, radius=1)
    assert circle_1 == circle_2, "Two circles of equal size should be considered equal."
    assert not circle_1 < circle_2, "A circle should not be considered less than another cirle of the same size."
    assert not circle_1 > circle_2, "A circle should not be considered greater than another cirle of the same size."

    big_circle = Circle(radius=2)
    assert circle_1 != big_circle, "Two circles of different size should be considered inequal."
    assert circle_1 < big_circle, "A smaller circle should be considered less than a larger circle."
    assert circle_1 <= big_circle, "A smaller circle should be considered less than or equal to a larger circle."
    assert not circle_1 > big_circle, "A smaller circle should not be considered greater than a larger circle."
    assert not circle_1 >= big_circle, "A smaller circle should not be considered greater than or equal to a larger circle."

    assert circle_1.is_unit_circle(), "A circle with radius 1 (unit) and center at (0, 0) should be considered a unit circle."
    assert not circle_2.is_unit_circle(), "A circle with its center NOT at (0, 0) should NOT be considered a unit circle."
    assert not big_circle.is_unit_circle(), "A circle with a radius other than 1 (unit) should not be considered a unit circle."

    assert not circle_1.is_inside(1, 1), "The point (1,1) should not be considered inside the unit circle."
    assert not circle_1.is_inside(-1, -1), "The point (1,1) should not be considered inside the unit circle."
    assert circle_1.is_inside(0.5, 0.5), "The point (0.5,0.5) should be considered inside the unit circle."
    assert circle_1.is_inside(-0.5, -0.5), "The point (0.5,0.5) should be considered inside the unit circle."
    
    rectangle = Rectangle(width=1, height=math.pi)
    assert rectangle.area == circle_1.area, "'rectangle' and 'circle_1' should have the same area."
    assert rectangle != circle_1, "A circle and rectangle should not be considered equal, even though they have the same area."