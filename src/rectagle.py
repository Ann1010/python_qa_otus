from python_qa_otus.src.figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b):
        if a <= 0 or b <= 0:
            raise ValueError("нельзя создать прямоугольник")
        super().__init__(name='Прямоугольник')
        self.a = a
        self.b = b

    def get_area(self) -> float:
        return self.a * self.b

    def get_perimeter(self) -> float:
        return 2 * (self.a + self.b)
