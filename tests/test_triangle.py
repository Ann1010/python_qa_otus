import math

import pytest

from python_qa_otus.src.rectagle import Rectangle
from python_qa_otus.src.triangle import Triangle


@pytest.mark.triangle
class TestTriangle:
    @pytest.mark.area
    @pytest.mark.parametrize(("side_a", "side_b", "side_c"), [(5, 8, 7), (5.3, 9.1, 7.1)], ids=["integer", "float"])
    def test_check_area(self, side_a, side_b, side_c):
        """Проверка вычисления площади треугольника"""
        rec = Triangle(side_a, side_b, side_c)
        p = rec.get_perimeter() / 2
        assert rec.get_area() == math.sqrt(p * (p - side_a) * (p - side_b) * (p - side_c)), \
            f"Полученная площадь треугольника отличается от ожидаемой"

    @pytest.mark.perimeter
    @pytest.mark.parametrize(("side_a", "side_b", "side_c"), [(5, 8, 7), (5.3, 9.1, 7.1)], ids=["integer", "float"])
    def test_check_perimeter(self, side_a, side_b, side_c):
        """Проверка вычисления периметра треугольника"""
        rec = Triangle(side_a, side_b, side_c)
        assert rec.get_perimeter() == side_a + side_b + side_c, \
            f"Полученный периметр треугольника отличается от ожидаемого"

    @pytest.mark.add
    def test_check_add_with_triangle(self):
        """Проверка сложения треугольника с прямоугольником"""
        rec = Triangle(2, 4, 3)
        triangle = Rectangle(5, 4)
        assert rec.add_area(triangle) == rec.get_area() + triangle.get_area(), \
            "Сумма двух фигур отличается от ожидаемой"

    @pytest.mark.negative
    @pytest.mark.parametrize(("side_a", "side_b", "side_c"), [(2, 3, 5), (5, 2, 3), (2, 5, 3), (2, 2, 5),
                                                              (5, 2, 2), (2, 5, 2)],
                             ids=["a+b=c", "b+c=a", "a+c=b", "a+b<c", "b+c<a", "a+c<b"])
    def test_rectangle_negative(self, side_a, side_b, side_c):
        """Проверка невозможности создания треугольника с условием: сумма двух сторон меньше третьей"""
        with pytest.raises(ValueError):
            Triangle(side_a, side_b, side_c)
