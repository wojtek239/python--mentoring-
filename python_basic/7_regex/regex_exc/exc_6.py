import re


def check_html(text: str) -> list:
    """
    check if given text is a correct html code
    """
    str_set = r"<\w+>.*?</\w+>"
    result = re.findall(str_set, text)
    return result


text1 = "<p>Learn about regular expressions here.</p> <p>You\'re going to love " \
        "them!</p>"
result = check_html(text1)
print(result)
