class Vechicle:
    def __init__(self, wheels_number_, colour_):
        self.wheels_number = wheels_number_
        self.colour = colour_

    def drive(self):
        print("im driving on {} wheels.".format(self.wheels_number))


def main():
    audi = Vechicle(4, "red")
    audi.drive()


if __name__ == "__main__":
    main()