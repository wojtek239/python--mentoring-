import random
random_set = set(random.sample(range(5, 121), 15))
print(random_set)
number = ()
set = {number for number in random_set if number % 2 != 0}
print(set)