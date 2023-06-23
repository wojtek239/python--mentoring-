class Rectangle:
    """ opis modelu """
    def __init__(self, long_: float, width_: float):
        self.long = long_
        self.width = width_

    def get_area(self) -> float:
        """opi"""
        return self.long * self.width

    def get_perimeter(self) -> float:
        return 2 * (self.long + self.width)


rectangle1 = Rectangle(4, 10)
print(f'long is: {rectangle1.long}')
print(f'width is: {rectangle1.width}')


print(f'area is: {rectangle1.get_area()}')


print(f'perimeter is: {rectangle1.get_perimeter()}')
