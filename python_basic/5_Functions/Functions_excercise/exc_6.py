import collections


def get_filtered_numbers(numbers: list[int]) -> list[int]:
    """
    filter numbers with only two digits

    """
    filtered_list = []

    for num in numbers:
        if 10 <= num <= 99:
            filtered_list.append(num)
        return filtered_list


input_list = [1, 5, 8, 12, 35, 656, 656264, 6526436, 643435, 7554, 765, 64, 65, 5434]
result = get_filtered_numbers(input_list)

print(result)