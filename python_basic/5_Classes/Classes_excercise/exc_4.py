from math import ceil


class BankAccount:
    FEE = 2

    def __init__(self, account_nr_: int, owner_name_: str, balance_: float):
        self.account_nr = account_nr_
        self.owner_name = owner_name_
        self.balance = balance_

    def deposit(self, amount_: float):
        # za kazde 100 zł x prowozji
        provision = ceil(amount_ // 100) * self.FEE

        self.balance += amount_ - provision
        print(f'after payment, which is: {amount_}, provision will be: {provision}')

    def withdrawal(self, amount_: float):
        if amount_ <= self.balance:
            self.balance -= amount_
            print("withdrawal done.")
        else:
            print("na bro. u broke")

    def change_ownership(self, new_owner_: str):
        self.new_owner = new_owner_


    def display(self):

        print(f'information about account: ')
        print(f'account number is: {self.account_nr}')
        print(f'owner name is: {self.owner_name}')
        print(f'balance is: {self.balance}')


account1 = BankAccount(1029103, "ja", 9999999)
account1.display()

account1.deposit(1)
account1.display()

account1.withdrawal(999999999999999999999999999)
account1.display()

account1.change_ownership("obiwan kenobi")
account1.display()
