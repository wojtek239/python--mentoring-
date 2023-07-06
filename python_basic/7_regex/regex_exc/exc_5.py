import re


def find_string(string: str) -> list:
    """
    finds a string with max 6 letters and without a/A
    """
    str_set = r"\b(?=\w{6}\b)(?![Aa])\w+"
    result = re.findall(str_set, string)
    return result


text = "unique dejifs eda addsfe njieadniadnaeijn 3443oij 4ke3"
result = find_string(text)
print(result)
