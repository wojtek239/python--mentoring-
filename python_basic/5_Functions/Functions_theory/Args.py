def sum_numbers(*args):
    sum = 0
    for val in args:
        sum += val

    return sum
print(sum_numbers())
print(sum_numbers(1))
print(sum_numbers(-1, 2, 3))