def multiply_numbers(*args: int) -> int:
    """
    multiply every number given
    """
    if len(args) == 0:
        return 0

    result = 1
    for num in args:
        result *= num
    return result

