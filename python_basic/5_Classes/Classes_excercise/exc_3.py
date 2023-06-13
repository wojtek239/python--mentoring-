class Rectangle:
    def __init__(self, long_: float, width_: float):
        self.long = long_
        self.width = width_

    def area(self):
        return self.long * self.width

    def perimeter(self):
        return 2 * (self.long + self.width)


rectangle1 = Rectangle(4, 10)
print(f'long is: {rectangle1.long}')
print(f'width is: {rectangle1.width}')


print(f'area is: {rectangle1.area()}')


print(f'perimeter is: {rectangle1.perimeter()}')

