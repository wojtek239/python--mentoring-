class Tank:
    def __init__(self, name_: str, capacity_: float):
        self.name = name_
        self.capacity = capacity_
        self.current_water = 0

    def pour_water(self, volume_: float):
        if self.current_water + volume_ <= self.capacity:
            self.current_water += volume_
            print(f'you have poured  {volume_} litres of water to {Tank}')