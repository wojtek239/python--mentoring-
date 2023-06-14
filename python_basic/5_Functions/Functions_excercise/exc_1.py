
nums = [4, 6, 8, 24, 12, 2]


def find_max_index(nums_: int):
    max_value = float('-inf')
    max_index = None

    for index, num in enumerate(nums):
        if num > max_value:
            max_value = num
            max_index = index

    return max_index


max_index = find_max_index(nums)
print(max_index)
