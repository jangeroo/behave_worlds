from behave import *


@given('we have behave installed')
def step_impl(context):
    print('behave is installed')


@when('we implement a test')
def step_impl(context):
    assert True is not False


@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False


@given(u'a set of specific users')
def step_impl(context):
    pass
    print('here is the table')
    print(context.table)
    print(step.name)
    # print(context.table.headers)
    # print(context.table.rows)
    # raise NotImplementedError(u'STEP: Given a set of specific users')


@when(u'we count the number of people in each department')
def step_impl(context):
    # print(context.table)
    # raise NotImplementedError(u'STEP: When we count the number of people in each department')
    pass


@then(u'we will find two people in "Silly Walks"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then we will find two people in "Silly Walks"')


@then(u'we will find one person in "Beer Cans"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then we will find one person in "Beer Cans"')
