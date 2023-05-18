number1 = float(input("please enter first number: "))
number2 = float(input("please enter second number: "))
if number1 % 2 == 0 and number2 % 2 == 0:
    print("both numbers are even")
elif number1 % 2 == 0 and number2 % 2 != 0:
    print("first number is even")
elif number1 % 2 != 0 and number2 % 2 == 0:
    print("second number is even")
else:
    print("none of them is even")
    