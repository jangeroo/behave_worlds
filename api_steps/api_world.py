from steps.default_world import *


class APIAccount(Account):

    def get_balance():
        print(f'\t    API ACCOUNT: get balance')
        print(f'\t    - account = GET atm.app/account')
        print(f'\t    - return account.balance')
        return '$80'


class APITeller(Teller):

    def withdraw(amount):
        print(f'\t    API TELLER: withdraw {amount}')
        print(f'\t    - POST atm.app/withdraw?amount={amount}')
