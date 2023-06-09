class Vechicle:
    def __init__(self, wheels_number_, brand_, colour_):
        self.__wheels_number = wheels_number_
        self._brand = brand_
        self.colour = colour_

    '''getter field __wheels_number'''
    def get_wheels_number(self):
        return self.__wheels_number

    '''getter field __wheels_number'''
    def set_wheels_number(self, wheels_number_):
        self.__wheels_number = wheels_number_


def main():
    car = Vechicle(4, "Audi", "blue")
    truck = Vechicle(10, "TIR", "pink")

    print(car.__wheels_number)
    print(car.get_wheels_number())
    print(car._brand)
    print(car.colour)

    truck.__wheels_number = 12
    truck.set_wheels_number(12)


if __name__ == "__main__":
    main()
