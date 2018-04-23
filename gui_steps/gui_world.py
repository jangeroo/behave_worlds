from steps.default_world import *


class GUIAccount(Account):

    def get_balance():
        print(f'\t    GUI ACCOUNT: get balance')
        print(f'\t    - open(\'/account\')')
        print(f'\t    - balance = get_element(\'balance\')')
        print(f'\t    - return balance')
        return '$80'


class GUITeller(Teller):

    def withdraw(amount):
        print(f'\t    GUI TELLER: withdraw {amount}')
        print(f'\t    - open(\'/withdraw\')')
        print(f'\t    - amount_field.fill({amount})')
        print(f'\t    - withdraw_button.click()')
