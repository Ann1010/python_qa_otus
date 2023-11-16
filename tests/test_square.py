import math

import pytest

from python_qa_otus.src.square import Square
from python_qa_otus.src.triangle import Triangle


@pytest.mark.square
class TestSquare:
    @pytest.mark.area
    @pytest.mark.parametrize("side_a", [5, 0.1], ids=["integer", "float"])
    def test_check_area(self, side_a):
        """Проверка вычисления площади квадрата"""
        rec = Square(side_a)
        assert rec.get_area() == side_a * side_a, \
            f"Полученная площадь квадрата отличается от ожидаемой"

    @pytest.mark.perimeter
    @pytest.mark.parametrize("side_a", [5, 0.1], ids=["integer", "float"])
    def test_check_perimeter(self, side_a):
        """Проверка вычисления периметра квадрата"""
        rec = Square(side_a)
        assert rec.get_perimeter() == 4 * side_a, \
            f"Полученный периметр квадрата отличается от ожидаемого"

    @pytest.mark.add
    def test_check_add_with_triangle(self):
        """Проверка сложения квадрата с треугольником"""
        rec = Square(5)
        triangle = Triangle(2, 4, 3)
        assert rec.add_area(triangle) == rec.get_area() + triangle.get_area(), \
            "Сумма двух фигур отличается от ожидаемой"

    @pytest.mark.negative
    @pytest.mark.parametrize("side_a", [0, -3], ids=["side_a=0", "side_a<0"])
    def test_rectangle_negative(self, side_a):
        """Проверка невозможности создания квадрата со стороной <= 0"""
        with pytest.raises(ValueError):
            Square(side_a)
