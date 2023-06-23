class Vechicle:
    def __init__(self, v_max_: int, mileage_: float):
        self.v_max = v_max_
        self.mileage = mileage_

    def add_mileage(self, value: float):
        self.mileage += value


vechicle1 = Vechicle(200, 50000)

print(f"v_max: {vechicle1.v_max}")
print(f"mileage: {vechicle1.mileage}")

new_mileage = float(input("pls enter added mileage: "))

vechicle1.add_mileage(new_mileage)
print(f"new mileage is: {vechicle1.mileage}")
