numbers = [1, -10, 2, 5, 10, -5, -20, 0, -30]

filtered_numbers = [num for num in numbers if num < 0]
example_tuple = tuple([num for num in numbers if num < 0])
# NOK (num for num in numbers if num < 0) its gen

example_dict = {str(num): num for num in numbers}
print(example_dict)

a = set()
b = {5}
print(type(b))
example_set = {num for num in numbers}
print(example_set)
print(type(example_set))
