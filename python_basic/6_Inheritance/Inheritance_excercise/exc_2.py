class Vehicle:
    def __init__(self, number_: int, v_max_: float):
        self.number = number_
        self.v_max = v_max_

    def get_description(self):
        """
        to get description of vehicle such ass:
        """
        return f"Number of vehicle is: {self.number}, and v max is: {self.v_max}"


class Tram(Vehicle):
    def __init__(self, number_: int, v_max_: float, wagon_nr_: int):
        pass


class Bus(Vehicle):
    def __init__(self, number_: int, v_max_: float, fuel_consumption_: float):
        pass


def main():
    pass


if __name__ == '__main__':
    main()

# two depots for bus and tram