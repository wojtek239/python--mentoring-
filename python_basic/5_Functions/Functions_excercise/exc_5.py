def combine_numbers(**kwargs: int) -> list:
    """
combine both odd and even numbers
    :param kwargs: int
    :return: list
    """
    odd_numbers = []
    even_numbers = []

    for key, value in kwargs.items():
        if value % 2 == 0:
            even_numbers.append(value)
        else:
            odd_numbers.append(value)

    combined_list = []
    for i in range(len(odd_numbers)):
        combined_list.append(odd_numbers[i])
        if i < len(even_numbers):
            combined_list.append(even_numbers[i])

    return combined_list


numbers = {
    'num1': 1,
    'num2': 2,
    'num3': 3,
    'num4': 4,
    'num5': 5,
    'num6': 6
}

result = combine_numbers(**numbers)
print(result)