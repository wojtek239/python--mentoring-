#property
class Circle:
    def __init__(self, radius_):
        self.radius = radius_

    @property
    def radius(self):
        return self.radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive value.")
        self._radius = value

circle = Circle(5)
print(circle.radius)
circle.radius = 10
print(circle.radius)


#abstractmethod
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


square = Square(5)
print(square.area())

#dataclass
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    city: str


person = Person("Wojtek", 23, "Zdunska Wola")
print(person)

#classmethod
class MyClass:
    count = 0

    def __init__(self, value):
        self.value = value
        MyClass.count += 1

    @classmethod
    def get_count(cls):
        pass

#staticmethod

class MathUtil:
    @staticmethod
    def add(a, b):
        return a + b
result = MathUtil.add(5, 3)
print(result)