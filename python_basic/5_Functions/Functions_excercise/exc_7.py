def get_fuel_lv() -> int:
    """
    to get fuel levels
    """
    while True:
        fuel_lv = int(input("pls enter starting amount of fuel from 5000 to 30000l: "))
        if 5000 <= fuel_lv <= 30000:
            return fuel_lv


def get_astronaut_amount() -> int:
    """
    to get number of astronauts
    """
    while True:
        astronaut_amount = int(input("pls enter number of astronauts from 1 to 7: "))
        if 0 < astronaut_amount < 7:
            return astronaut_amount


def simulate_rocket_flight(fuel_lv: int, astronaut_amount: int) -> int:
    """
    calculate distance and fuel usage accounting astronauts
    """
    distance = 0
    fuel_consumption_per_100km = 300 + 100 * astronaut_amount
    while fuel_lv >= fuel_consumption_per_100km:
        distance += 100
        fuel_lv -= fuel_consumption_per_100km
        print("actual distance is: {} km".format(distance))

    return distance


def show_result(distance: int):
    """
    to show result
    """
    if distance > 2000:
        print("rocket has arrived to the orbit")
    else:
        print("rocket didn't arrive to the orbit")


fuel_lv = get_fuel_lv()
astronaut_amount = get_astronaut_amount()
final_distance = simulate_rocket_flight(fuel_lv, astronaut_amount)
show_result(final_distance)

