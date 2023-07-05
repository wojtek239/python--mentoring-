import re


def check_start(string: str) -> str:
    """
    checks if string starts with b or (0-9)
    """
    string_set = r"^([0-9]|[bB])"
    if re.match(string_set, string):
        print("string starts with 0-9 or b/B")
    else:
        print("string does not start with 0-9 or b/B")


check_start("ecih3u847042y")
check_start("Bajdwoeifj4[3fj")
check_start("4 -3232")

