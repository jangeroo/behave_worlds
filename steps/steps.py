from behave import given, when, then
import utils.types


@given("I have deposited '{amount:Dollar}' into my account")
def step_impl(context, amount):
    print(f'\tGIVEN I have deposited {amount} into my account')
    context.account = context.Account()
    context.Teller.deposit(amount, context.account)
    print()


@when("I withdraw '{amount:Dollar}'")
def step_impl(context, amount):
    print(f'\tWHEN I withdraw {amount}')
    context.Teller.withdraw(amount, context.account)
    print()


@then("'{amount:Dollar}' should be dispensed")
def step_impl(context, amount):
    print(f'\tTHEN {amount} should be dispensed')
    print()


@then("I should have '{balance:Dollar}' left in my account")
def step_impl(context, balance):
    print(f'\tTHEN I should have {balance} left in my account')
    actual = context.Teller.get_balance(context.account)
    assert actual == balance,\
        f'EXPECTED: {balance}, GOT: {actual}'
    print()
