# def is_prime(number):
#     if number <= 1:
#         return False
#     elif number <= 3:
#         return True
#     elif number % 2 == 0 or number % 3 == 0:
#         return False
#     i = 5
#     while i * i <= number:
#         if number % i == 0 or number % (i + 2) == 0:
#             return False
#         i += 6
#     return True


def is_prime(num: int) -> bool:
    dividers = []
    if num > 0:

        for divider in range(1, num + 1):
            if num % divider == 0:
                dividers.append(divider)

        if len(dividers) == 2:
            return True

    return False
