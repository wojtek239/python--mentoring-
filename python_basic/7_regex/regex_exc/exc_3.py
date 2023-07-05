import re


def check_string(string: str) -> str:
    """
    check if string has any set of small letters divided with sign
    """
    str_set = r"^[a-z]+_[a-z]+$"
    if re.match(str_set, string):
        print("string has set of small letters divided by sign")
    else:
        print("string does not have set of small letters divided by sign")


check_string("aaa_bdb")
check_string("abc_dfr")
check_string("dcr")
