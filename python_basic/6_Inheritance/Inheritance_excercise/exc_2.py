class Vehicle:
    def __init__(self, number_: str, v_max_: float):
        self.number = number_
        self.v_max = v_max_

    def get_description(self):
        """
        to get description of vehicle such ass:
        """
        return f"Number of vehicle is: {self.number}, and v max is: {self.v_max}"


class Tram(Vehicle):
    def __init__(self, number_: str, v_max_: float, wagon_nr_: int):
        super().__init__(number_, v_max_)
        self.wagon_nr_ = wagon_nr_

    def get_description(self):
        """
        to get description of tram
        """
        return f"Tram {self.number}:v max: {self.v_max}, wagons: {self.wagon_nr_}"
        pass


class Bus(Vehicle):
    def __init__(self, number_: str, v_max_: float, fuel_consumption_: float):
        super().__init__(number_, v_max_)
        self.fuel_consumption_ = fuel_consumption_

    def get_description(self):
        """
        to get description of bus
        """
        return f"Bus {self.number}:v max: {self.v_max}, " \
               f"fuel consumption: {self.fuel_consumption_}"
        pass


class Depot:
    def __init__(self, name_: str):
        self.name = name_
        self.vehicles = []

    def add_vehicle(self, vehicle_: str):
        """
        to add more vehicles to depot
        """
        self.vehicles.append(vehicle_)

    def get_description(self):
        """
        to get description of depot with vehicles
        """
        description = f"{self.name} Depot\n"
        for vehicle in self.vehicles:
            description += vehicle.get_description()
        return description


tram1 = Tram("T1", 70, 2)
tram2 = Tram("T2", 60, 3)
bus1 = Bus("B1", 50, 200)
bus2 = Bus("B2", 55, 180)

tram_depot = Depot("Tram Depot")
bus_depot = Depot("Bus Depot")

tram_depot.add_vehicle("tram1")
tram_depot.add_vehicle("tram2")

bus_depot.add_vehicle("bus1")
bus_depot.add_vehicle("bus2")

print(tram_depot.get_description())
print(bus_depot.get_description())