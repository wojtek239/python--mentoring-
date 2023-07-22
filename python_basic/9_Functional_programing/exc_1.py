add_15 = lambda x: x + 15
multiply = lambda x, y: x * y

values = [5, 15, 240]

added_val = list(map(add_15, values))
print(f'result of adding is: ', added_val)

list_x = [1, 2, 3, 4]
list_y = [5, 6, 7, 8]

products = list(map(multiply, list_x, list_y))
print(f'results of multiplying are: ', products)
