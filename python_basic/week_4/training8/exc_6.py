def count_digit_frequency(num: int) -> dict[str, int]:
    """ opis funkcji """
    digit_frequency = {}
    for digit in str(num):
        if digit in digit_frequency:
            digit_frequency[digit] += 1
        else:
            digit_frequency[digit] = 1

    return digit_frequency


number = 6000000111111
frequency = count_digit_frequency(number)
print(frequency)
