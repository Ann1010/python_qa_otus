import math

from python_qa_otus.src.figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Нельзя создать Круг")
        super().__init__(name='Круг')
        self.radius = radius

    def get_area(self) -> float:
        return math.pi * self.radius**2

    def get_perimeter(self) -> float:
        return 2 * math.pi * self.radius
