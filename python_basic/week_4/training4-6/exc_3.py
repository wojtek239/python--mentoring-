numbers_list = []

while True:
    number = input("please enter number or type 'stop' to stop: ")
    if number == 'stop':
        break
    if len(numbers_list) > 10:
        break

    number = int(number)
    numbers_list.append(number)

even_numbers = []
for i in numbers_list:
    if i % 2 == 0:
        even_numbers.append(i)
print(f"even numbers form list are:", even_numbers)
