from python_qa_otus.src.figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        if side_a <= 0 or side_b <= 0:
            raise ValueError("нельзя создать прямоугольник")
        super().__init__(name='Прямоугольник')
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self) -> float:
        return self.side_a * self.side_b

    def get_perimeter(self) -> float:
        return 2 * (self.side_a + self.side_b)
