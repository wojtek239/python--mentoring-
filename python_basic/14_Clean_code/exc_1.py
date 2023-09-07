import re


def email(user: str):
    """Sends an email to the single user"""
    pass


def get_gmail_users(ursers):
    """Select users with the gmail.com domain using a generator"""
    gmail_regex = r"\S*?@gmail\.com"
    for user in users:
        if re.match(gmail_regex, user):
            yield user


def email_gmail_users(users):
    """Sends an email to the users with the gmail.com domain"""
    for user in get_gmail_users(users):
        email(user)


users = ["jan.grab@gmail.com", "ania.kowalska@onet.pl", "excited.girl@yahoo.com",
         "dg.soldier@o2.pl"]


email_gmail_users(users)
