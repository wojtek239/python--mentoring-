users_number = int(input("please enter your number: "))
sum_of_numbers = 0
numbers = []
for i in range(1, users_number + 1):
    sum_of_numbers += i
    numbers.append(i)
print(f'sum from 1 to users number equals', sum_of_numbers, sum(numbers))


