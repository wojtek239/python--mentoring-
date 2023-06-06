class Vechicle:
    def __init__(self, wheels_number_, brand_, colour_):
        self.wheels_number = wheels_number_
        self.brand = brand_
        self.colour = colour_

    def describe_vechicle(self):
        print("you're in a vehicle that:" )
        print("it has {} wheels, it's {} brand and it's colour is {}".format(
            self.wheels_number, self.brand, self.colour))


def main():
    car =  Vechicle(4, "BMW", "blue")
    truck = Vechicle(10, "TIR", "Pink")

    car.describe_vechicle()
    truck.describe_vechicle()


if __name__ == "__main__":
    main()