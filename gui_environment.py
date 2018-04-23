print('--- GUI ENVIRONMENT ---\n')

from gui_steps.gui_world import *


def before_all(context):
    context.Account = GUIAccount
    context.Teller = GUITeller
