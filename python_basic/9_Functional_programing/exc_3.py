numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square = lambda x: x ** 2
cube = lambda x: x ** 3

squares = list(map(square, numbers))
cubes = list(map(cube, numbers))

print("Oryginal list: ")
print(numbers)

print("Squared list: ")
print(squares)

print("Cubed list: ")
print(cubes)