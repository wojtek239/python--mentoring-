import re


def find_s(string: str) -> list:
    """
    checks if string has at least two letters s
    """
    string_set = r"\b\w*ss+\b"
    result = re.findall(string_set, string, re.IGNORECASE)
    return result


text = "hiss hisssss His"
result = find_s(text)
print(result)