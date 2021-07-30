from behave import *


@given('a user is on the manager dashboard page')
def test_on_manager_dashboard(context):
    pass


@when('the user tries to access their dashboard without logging in')
def test_user_has_not_logged_in(context):
    pass


@then('the user is redirected to the login page')
def test_redirected_to_login_page(context):
    pass


@when('a user has started a manager session')
def test_user_has_logged_in(context):
    pass


@then('the user is able to view the manager dashboard')
def test_user_can_view_manager_dashboard(context):
    pass
