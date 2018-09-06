from steps.default_world import *


# Note: Class methods call the default_world methods only because there's no real implementation of the other worlds

class GUIAccount(Account):
    def __init__(self):
        print(f'\t    GUI ACCOUNT: creating new account')
        print(f'\t    - open(\'/\')')
        print(f'\t    - new_account_button.click()')
        super().__init__()


class GUITeller(Teller):
    def deposit(amount, account):
        print(f'\t    GUI TELLER: deposit {amount}')
        print(f'\t    - open(\'/deposit\')')
        print(f'\t    - amount_field.fill({amount})')
        print(f'\t    - deposit_button.click()')
        Teller.deposit(amount, account)

    def withdraw(amount, account):
        print(f'\t    GUI TELLER: withdraw {amount}')
        print(f'\t    - open(\'/withdraw\')')
        print(f'\t    - amount_field.fill({amount})')
        print(f'\t    - withdraw_button.click()')
        Teller.withdraw(amount, account)

    def get_balance(account):
        print(f'\t    GUI ACCOUNT: get balance')
        print(f'\t    - open(\'/account\')')
        print(f'\t    - balance = get_element(\'balance\')')
        print(f'\t    - return balance')
        return Teller.get_balance(account)
