import time

from behave import step
from hamcrest import assert_that, equal_to


@step('the user logs in')
def step_impl(context):
    print("Given the user logs in")
    # time.sleep(30)


@step('the user does something')
def step_impl(context):
    print("When the user does something")


@step('the user gets a result')
def step_impl(context):
    print("Then the user gets a result")