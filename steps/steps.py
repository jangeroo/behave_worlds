from behave import given, when, then


@given("I have deposited '{amount}' into my account")
def step_impl(context, amount):
    print(f'\tGIVEN I have deposited {amount} into my account\n')


@when("I withdraw '{amount}'")
def step_impl(context, amount):
    print(f'\tWHEN I withdraw {amount}')
    context.Teller.withdraw(amount)
    print()


@then("'{amount}' should be dispensed")
def step_impl(context, amount):
    print(f'\tTHEN {amount} should be dispensed\n')


@then("I should have '{balance}' left in my account")
def step_impl(context, balance):
    print(f'\tTHEN I should have {balance} left in my account')
    actual = context.Account.get_balance()
    assert actual == balance,\
        f'EXPECTED: {balance}, GOT: {actual}'
    print()
