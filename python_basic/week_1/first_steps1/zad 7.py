weight_kg = float(input("podaj swoją wagę [kg]: "))
height_cm = float(input("podaj swój wzrost [cm]: "))

height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)

print("twoje BMI to: ", round(bmi, 2))
