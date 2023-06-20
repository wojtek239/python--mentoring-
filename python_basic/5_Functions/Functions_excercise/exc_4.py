
def multiply_numbers(*args: int) -> int:
    """
    multiply every number given
    """
    if len(args) == 0:
        return None

    result = 1
    for num in args:
        result *= num
        return result


user_input = input("please enter numbers: ")
numbers = [int(num) for num in user_input.split()]

print(multiply_numbers(*numbers))
