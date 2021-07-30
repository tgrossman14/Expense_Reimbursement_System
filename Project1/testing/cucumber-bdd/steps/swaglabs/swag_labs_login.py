# Step definition file- Details the source code for the tests specified to be written in the feature file. This is also called "Glue Code"

from behave import *
from testing.mercury.poms.swaglabs.swag_labs_login_page import SwagLabsLoginPage

@given('a user is on the home page of Swag Labs')
def test_on_home_page(context):
    context.driver.get('https://www.saucedemo.com/')


@given('a user enters the correct username and the correct password')
def test_user_enters_username(context):
    context.sll_page.enter_credentials()

@when('the user pushes the submit button')
def test_user_presses_submit(context):
    context.sll_page.click_login_button()

@then('the user is redirected to the dashboard')
def user_is_redirected(context):
    assert 'inventory' in context.driver.current_url

@when('the user pushes the enter button')
def test_user_hits_enter(context):
    context.sll_page.hit_enter_button_to_login()

@then('the user is redirected to the dashboard anyway')
def user_is_redirected(context):
    pass
