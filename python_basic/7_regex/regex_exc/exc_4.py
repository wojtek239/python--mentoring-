import re


def find_s(string: str) -> list:
    """
    checks if string has at least two letters s
    """
    # r"\b\w*ss+\b"
    string_set = r"s{2,}"
    result = re.findall(string_set, string, re.IGNORECASE)
    return result


text = "hiss hisssss His"
result = find_s(text)
print(result)
