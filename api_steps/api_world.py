from steps.default_world import *


# Note: Class methods call the default_world methods only because there's no real implementation of the other worlds

class APIAccount(Account):
    def __init__(self):
        print(f'\t    API ACCOUNT: creating new account')
        print(f'\t    - POST atm.app/account/create')
        super().__init__()


class APITeller(Teller):
    def deposit(amount, account):
        print(f'\t    API TELLER: deposit {amount}')
        print(f'\t    - POST atm.app/deposit?amount={amount}')
        Teller.deposit(amount, account)

    def withdraw(amount, account):
        print(f'\t    API TELLER: withdraw {amount}')
        print(f'\t    - POST atm.app/withdraw?amount={amount}')
        Teller.withdraw(amount, account)

    def get_balance(account):
        print(f'\t    API ACCOUNT: get balance')
        print(f'\t    - account = GET atm.app/account')
        print(f'\t    - return account.balance')
        return Teller.get_balance(account)
