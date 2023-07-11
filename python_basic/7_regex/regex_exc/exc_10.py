import re


def get_dates(data: str) -> str:
    """
    gets only dates from given data
    """
    # (\d{4}-\d{2}-\d{2})|(\d{2}/\d{2}/\d{2})|(\d{4}.\d{2}.\d{2})|(\d{4}-[a-z]+-\d{2})
    str_set = r"\b\d{4}[-./](?:\d{2}|\w{3,})[-./](?:\d{2}|\w{3,})\b"
    dates = re.findall(str_set, data)
    return dates


data = "2019-03-11: 23.5, 19/03/12: 12.7, 2019.03.13: 11.1, 2019-marzec-14: 14.3"
dates = get_dates(data)
print(dates)
