from behave import step


@step('the user logs in')
def step_impl(context):
    print("Given the user logs in")


@step('the user does something')
def step_impl(context):
    print("When the user does something")


@step('the user gets a result')
def step_impl(context):
    print("Then the user gets a result")