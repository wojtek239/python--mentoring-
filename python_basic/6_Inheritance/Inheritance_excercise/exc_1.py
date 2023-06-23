class Shape:
    def __init__(self):
        pass

    def get_area(self):
        """
        to calculate the area
        """
        return 0


class Square(Shape):
    def __init__(self, length_: float):
        super.__init__()
        self.length = length_

    def get_area(self) -> float:
        return self.length ** 2


shape = Shape()
print(shape.get_area())

square = Square(5.0)
print(square.get_area())
