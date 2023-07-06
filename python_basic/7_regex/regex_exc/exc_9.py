import re


def get_number_format(number: float) -> string:
    """
     check if given number has good format
    """
    nr_set = r"^[-+]?[0-9]+(\.[0-9]+)?$"
    if re.match(nr_set, number):
        print("number has good format")
    else:
        print("number doesn't have good format")


number1 = 123,2341515132135
get_number_format(number1)

number2 = 123,
get_number_format(number2)

