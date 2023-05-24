users_weight = float(input("please enter your weight in kg: "))
users_height = float(input("please enter your height in m: "))
BMI = round(users_weight / (users_height ** 2), 2)
print(f"your BMI is: ", BMI)
if BMI < 18.5:
    print("underweight")
elif 18.5 <= BMI <= 24:
    print("normal weight")
elif 24 < BMI <= 26.5:
    print("slight overweight")
elif BMI > 26.5 and BMI < 30:
    print("overweight")
elif 30 <= BMI <= 35:
    print("obesity lv 1")
elif 35 < BMI <= 40:
    print("obesity lv 2")
else:
    print("obesity lv 3")
