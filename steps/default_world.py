class Account():
    def __init__(self):
        print(f'\t\t... creating new account')
        self.balance = 0

class Teller():
    def deposit(amount, account):
        print(f'\t\t... depositing {amount}')
        account.balance += amount

    def withdraw(amount, account):
        print(f'\t\t... withdrawing {amount}')
        account.balance -= amount

    def get_balance(account):
        print(f'\t\t... getting balance')
        return account.balance

