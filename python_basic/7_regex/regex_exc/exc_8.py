import re


def get_numbers(sign_string: str) -> str:
    str_set = r"\b\d+\b"
    numbers = re.findall(str_set, sign_string)
    return numbers


string = "2 cats and 3 dogs"
result = get_numbers(string)
print(result)

