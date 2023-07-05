import re


def check_string(string: str) -> str:
    """
    checks if string has right set of signs
    """
    str_set = "^[a-zA-Z0-9]+$"
    if re.match(str_set, string):
        print("String has only set of letters (a-z, A-Z) and numbers (0-9).")
    else:
        print("String has different set of letters than (a-z, A-Z) and numbers (0-9).")


check_string("Abc123")
check_string("Test!")
