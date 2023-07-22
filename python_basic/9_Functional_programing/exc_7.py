nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = list(map(lambda x: x ** 2, nums))
new_sums = list(filter(lambda x: x % 2 == 0, squares))
print(f'New list is: ', new_sums)


