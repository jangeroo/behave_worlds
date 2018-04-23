print('*** DEFAULT ENVIRONMENT ***\n')

from steps.default_world import *


def before_all(context):
    context.Account = Account
    context.Teller = Teller
