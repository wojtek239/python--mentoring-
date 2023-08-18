from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, account_number, owner_name):
        self.account_number = account_number
        self.owner_name = owner_name

    @abstractmethod
    def validate_user_identity(self):
        pass

    @abstractmethod
    def calculate_interest_rate(self):
        pass

    @abstractmethod
    def register_account(self):
        pass


class PersonalAccount(BankAccount):
    def validate_user_identity(self):
        print("Client ID verification (personal account)")

    def calculate_interest_rate(self):
        print("Borrowing rate calculation (personal account)")

    def register_account(self):
        print("Personal account rejestration")


class BusinessAccount(BankAccount):
    def validate_user_identity(self):
        print("Client ID verification (company account)")

    def calculate_interest_rate(self):
        print("Borrowing rate calculation (company account)")

    def register_account(self):
        print("Company account rejestration")


class SavingsAccount(BankAccount):
    def validate_user_identity(self):
        print("Client ID verification (saving account)")

    def calculate_interest_rate(self):
        print("Borrowing rate calculation (saving account)")

    def register_account(self):
        print("Saving account rejestration")


class BankAccountFactory:
    def create_account(self, account_type, account_number, owner_name):
        if account_type == "personal":
            return PersonalAccount(account_number, owner_name)
        elif account_type == "business":
            return BusinessAccount(account_number, owner_name)
        elif account_type == "savings":
            return SavingsAccount(account_number, owner_name)
        else:
            raise ValueError("Invalid account type")


account_factory = BankAccountFactory()

account_type = input("Choose account type (personal/business/savings): ")
account_number = input("Enter account number: ")
owner_name = input("Enter client name and surname: ")

account = account_factory.create_account(account_type, account_number, owner_name)
account.validate_user_identity()
account.calculate_interest_rate()
account.register_account()
