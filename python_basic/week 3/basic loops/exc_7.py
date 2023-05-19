# square
side = int(3)
for i in range(side):
    for j in range(side):
        print('*', end=' ')
    print()
print('\n')

# line
print('* ' * 10)
print()
print('\n')

# right triangle

for i in range(1, 5):
    print(('*' * i).center(1))
print('\n')

# Christmas tree

for i in range(1, 6):
    print(('*' * i).center(2))

print("*".center(9,"-"))
print("***".center(9,"-"))
print("*****".center(9,"-"))
print("*******".center(9,"-"))
print("*********")

stars = "*"
print(stars.center(10))

for i in range(4):
    for j in range(2):
        stars += "*"

    print(stars.center(10))
