
user_number = int(input("please enter number: "))
dividers = []

for div in range(1, user_number):
    if not user_number % div:
        dividers.append(div)

if sum(dividers) == user_number:
    print("This number is perfect!")
else:
    print("This number is ugly !")

# everytime there is no change while dividing, dividers_sum grows by 1
