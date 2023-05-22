# side np. first_side itd.
first = float(input("type first lenght: "))
second = float(input("type second lenght: "))
third = float(input("type third lenght: "))

sides = [first, second, third]
longest = max(sides)

sides.remove(longest)
shorter1, shorter2 = sides

# co jest ze zmiennymi po warunku
if shorter1 ** 2 + shorter2 ** 2 == longest ** 2:
    print("this is the right triangle. ")
else:
    print("this is not the right triangle. ")


# 2 sposób
sides = [first, second, third]
sides.sort(reverse=True)

a, b, c = sides
