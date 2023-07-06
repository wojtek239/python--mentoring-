import re


def get_hex_colour(colour: str) -> str:
    str_set = r"^#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?$"
    if re.match(str_set, colour):
        print("given string is a correct form of hex colour writing")
    else:
        print("given string is not a correct form")


colour1 = "#AB4B72"
get_hex_colour(colour1)
colour2 = "#ab43"
get_hex_colour(colour2)
