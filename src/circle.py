import math

from figure import Figure


class Circle(Figure):
    def __init__(self, r):
        if r <= 0:
            raise ValueError("Нельзя создать Круг")
        super().__init__(name='Круг')
        self.r = r

    def get_area(self) -> float:
        return math.pi * self.r**2

    def get_perimetr(self) -> float:
        return  2 * math.pi * self.r