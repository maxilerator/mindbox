import unittest

from circle import Circle
from triangle import Triangle


class TestFigure(unittest.TestCase):

    def test_circle_area(self):
        circle = Circle(3)
        self.assertEqual(circle.area(), 28.274333882308138)

    def test_triangle_area(self):
        triangle = Triangle([3, 4, 5])
        self.assertEqual(triangle.area(), 6)

    def test_is_right_angled(self):
        not_rectangular = Triangle([2, 2, 3])
        self.assertFalse(not_rectangular.is_rectangular())

        rectangular = Triangle([3, 4, 5])
        self.assertTrue(rectangular.is_rectangular())


if __name__ == '__main__':
    unittest.main()
