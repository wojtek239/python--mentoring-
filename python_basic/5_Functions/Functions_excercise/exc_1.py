
nums = [4, 6, 8, 24, 12, 2]

def find_max_index(nums):
    max_value = max(nums)
    for i, num in enumerate(nums):
        if num == max_value:
            return i
index = find_max_index(nums)
print(f'biggest index is: {index}')

