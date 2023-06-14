def get_index_of_max_element(nums: list[int]) -> int:
    """
    Return the max value and index of this number
    """
    max_value = max(nums)
    for idx, num in enumerate(nums):
        if num == max_value:
            return idx


def main():
    nums = [4, 6, 8, 24, 12, 2]

    index = get_index_of_max_element(nums)
    print(f'biggest index is: {index}')


if __name__ == "__main__":
    main()
