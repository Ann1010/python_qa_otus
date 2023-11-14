from rectagle import Rectangle


class Square(Rectangle):
    def __init__(self, a):
        if a <= 0:
            raise ValueError("Нельзя создать Квадрат")
        super().__init__(a=a, b=a)
        self.a = a
