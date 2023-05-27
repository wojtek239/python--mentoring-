numbers_list = []

while True:
    number = input("please enter number or type 'stop' to stop: ")

    if number == 'stop' or len(numbers_list) > 10:
        break

    numbers_list.append(int(number))

even_numbers = []
for i in numbers_list:
    if i % 2 == 0:
        even_numbers.append(i)
print(f"even numbers form list are:", even_numbers)


# while number := input("please enter number or type 'stop' to stop: "):
#     if len(numbers_list) > 10:
#         break
#
#     numbers_list.append(int(number))
#
#
# if number := input("please enter number or type 'stop' to stop: "):
#     print(number)
