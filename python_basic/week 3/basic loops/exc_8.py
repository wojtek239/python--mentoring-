from statistics import mean

numbers = []
for i in range(10):
    numbers.append(i)

average = sum(numbers) / len(numbers)
print(average)
print(mean(numbers))

