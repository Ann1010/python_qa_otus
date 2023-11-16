import math

from python_qa_otus.src.figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Нельзя создать Треугольник")
        elif a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Нельзя создать Треугольник")
        super().__init__(name='Треугольник')
        self.a = a
        self.b = b
        self.c = c

    def get_area(self) -> float:
        p = self.get_perimeter()/2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def get_perimeter(self) -> float:
        return self.a + self.b + self.c
