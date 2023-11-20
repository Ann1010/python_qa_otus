import math

import pytest

from python_qa_otus.src.circle import Circle
from python_qa_otus.src.triangle import Triangle


@pytest.mark.circle
class TestCircle:
    @pytest.mark.area
    @pytest.mark.parametrize("radius", [5, 0.1], ids=["integer", "float"])
    def test_check_area(self, radius):
        """Проверка вычисления площади круга"""
        circle = Circle(radius)
        assert circle.get_area() == math.pi * radius**2, \
            "Полученная площадь круга отличается от ожидаемой"

    @pytest.mark.perimeter
    @pytest.mark.parametrize("radius", [5, 0.1], ids=["integer", "float"])
    def test_check_perimeter(self, radius):
        """Проверка вычисления периметра круга"""
        circle = Circle(radius)
        assert circle.get_perimeter() == 2 * math.pi * radius, \
            "Полученный периметр круга отличается от ожидаемого"

    @pytest.mark.add
    def test_check_add_with_triangle(self):
        """Проверка сложения круга с треугольником"""
        circle = Circle(5)
        triangle = Triangle(2, 4, 3)
        assert circle.add_area(triangle) == circle.get_area() + triangle.get_area(), \
            "Сумма двух фигур отличается от ожидаемой"

    @pytest.mark.negative
    @pytest.mark.parametrize("radius", [0, -3], ids=["r=0", "r<0"])
    def test_rectangle_negative(self, radius):
        """Проверка невозможности создания круга с радиусом <= 0"""
        with pytest.raises(ValueError):
            Circle(radius)
