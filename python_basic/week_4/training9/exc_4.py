rainfall_data = {}
while True:
    city = input("please enter city name (or type in blank space to end): ")
    if city == " ":
        break

    rainfall = float(input("please enter rainfall (in mm): "))

    if city in rainfall_data:
        rainfall_data[city] += rainfall
    else:
        rainfall_data[city] = rainfall

print("\n rainfall overview: ")

for city, rainfall in rainfall_data.items():
    print(f"{city}: {rainfall}")
