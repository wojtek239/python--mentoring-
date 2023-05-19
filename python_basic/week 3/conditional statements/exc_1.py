first = float(input("type first lenght: "))
second = float(input("type second lenght: "))
third = float(input("type third lenght: "))

longest = max([first, second, third])
# max finds the biggest value
if longest == first:
    shorter1 = second
    shorter2 = third
# czemu tylko przy pierwszej wartośi trzeba dać == a poźniej już = .wyświetla mi się błąd więc zmieniłem i działa
elif longest == second:
    shorter1 = first
    shorter2 = third
else:
    shorter1 = first
    shorter2 = second

# co jest ze zmiennymi po warunku
if shorter1 ** 2 + shorter2 ** 2 == longest ** 2:
    print("this is the right triangle. ")
else:
    print("this is not the right triangle. ")
