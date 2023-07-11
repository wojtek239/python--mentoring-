import re


def get_company_name(email_adress: str) -> list:
    """
    to get company name from email adress
    """
    # (\w+)@([a-zA-Z]+).([a-zA-Z]+)
    str_set = r"@([a-zA-Z]+)\.com$"
    match = re.search(str_set, email_adress)
    if match:
        return match.group(1)
    else:
        return None


adress = "username@companyname.com"
company_name = get_company_name(adress)
if company_name:
    print("company name is: ", company_name)
else:
    print("there is no company name here")

