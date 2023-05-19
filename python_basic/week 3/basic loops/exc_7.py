# square
side = int(3)
for i in range(side):
    for j in range(side):
        print('*', end=' ')
    print()
print('\n')

# line
line = int(10)
for i in range(line):
    print('*', end=' ')
print()
print('\n')

# right triangle

for i in range(1, 5):
    print(('*' * i).center(1))
print('\n')

# Christmas tree

for i in range(1, 6):
    print(('*' * i).center(2))

