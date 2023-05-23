# rectangle 6x7
for i in range(6):
    for j in range(7):
        print("*", end="")
    print("")
print("\n")

# square 5 empty inside

for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print("\n")

# Christmas Tree
stars = "*"
print(stars.center(10))

for i in range(4):
    for j in range(2):
        stars += "*"

    print(stars.center(10))


