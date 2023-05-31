def count_digit_frequency(number):
    number_str = str(number)
    digit_frequency = {}

    for digit in number_str:
        if digit.isdigit():
            if digit in digit_frequency:
                digit_frequency[digit] += 1
            else:
                digit_frequency[digit] = 1
    return digit_frequency


number = 49694039546355109387513503289523895
frequency = count_digit_frequency(number)
print(frequency)
