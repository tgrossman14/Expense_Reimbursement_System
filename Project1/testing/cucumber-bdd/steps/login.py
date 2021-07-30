from behave import *
from testing.mercury.poms.login_page import MASHLoginPage


@given('a user is on the MASH login page')
def test_on_home_page(context):
    pass


@when('the user pushes the login button')
def test_user_pushes_login_button(context):
    pass


@when('the user pushes the ENTER button')
def test_user_pushes_enter_button(context):
    pass


@then('the user is redirected to the dashboard of the associated employee or manager')
def test_user_redirected_to_correct_dash(context):
    pass


@then('the user is redirected to the login page')
def test_login_page_reset(context):
    pass