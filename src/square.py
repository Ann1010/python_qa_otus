from python_qa_otus.src.rectagle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("Нельзя создать Квадрат")
        super().__init__(side_a=side_a, side_b=side_a)
        self.side_a = side_a
