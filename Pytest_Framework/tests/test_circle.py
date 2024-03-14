import pytest
import math
import source.Shapes as shape

class TestCircle:

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = shape.Circle(10)

    def teardown_method(self, method):

        print(f"Tearing down {method}")
        del self.circle

    def test_radius(self):

        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):

        result = self.circle.perimeter()
        expected = 2 * math.pi

        assert True

    def test_not_same_area_rectangle(self, my_rectangle):
        assert self.circle.area() != my_rectangle.area()
