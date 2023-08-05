examp = (i for i in range(10))
print(examp)

print(next(examp))
print(next(examp))
print(next(examp))


examp = (i for i in range(10))

for number in examp:
    print(number)
# bez użycia iteracji "examp" będzie jedynie obiektem generatora a nie listą
