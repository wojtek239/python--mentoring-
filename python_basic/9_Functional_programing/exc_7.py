nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square = lambda x: x ** 2
new_sums = list(filter(lambda x: x % 2 == 0, map(square, nums)))
print(f'New list is: ', new_sums)
