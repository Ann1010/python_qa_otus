import pytest

from python_qa_otus.src.rectagle import Rectangle
from python_qa_otus.src.triangle import Triangle


@pytest.mark.rectangle
class TestRectangle:
    @pytest.mark.area
    @pytest.mark.parametrize(("side_a", "side_b"), [(5, 8), (5.3, 9.1)], ids=["integer", "float"])
    def test_check_area(self, side_a, side_b):
        """Проверка вычисления площади прямоугольника"""
        rectangle = Rectangle(side_a, side_b)
        assert rectangle.get_area() == side_a * side_b, \
            "Полученная площадь прямоугольника отличается от ожидаемой"

    @pytest.mark.perimeter
    @pytest.mark.parametrize(("side_a", "side_b"), [(5, 8), (5.3, 9.1)], ids=["integer", "float"])
    def test_check_perimeter(self, side_a, side_b):
        """Проверка вычисления периметра прямоугольника"""
        rectangle = Rectangle(side_a, side_b)
        assert rectangle.get_perimeter() == 2 * (side_a + side_b), \
            "Полученный периметр прямоугольника отличается от ожидаемого"

    @pytest.mark.add
    def test_check_add_with_triangle(self):
        """Проверка сложения прямоугольника с треугольником"""
        rectangle = Rectangle(5, 3)
        triangle = Triangle(2, 4, 3)
        assert rectangle.add_area(triangle) == rectangle.get_area() + triangle.get_area(), \
            "Сумма двух фигур отличается от ожидаемой"

    @pytest.mark.negative
    @pytest.mark.parametrize(("side_a", "side_b"), [(0, 8), (5, 0), (-3, 1), (3, -1)], ids=["a=0", "b=0", "a<0", "b<0"])
    def test_rectangle_negative(self, side_a, side_b):
        """Проверка невозможности создания прямоугольника со стороной <= 0"""
        with pytest.raises(ValueError):
            Rectangle(side_a, side_b)
