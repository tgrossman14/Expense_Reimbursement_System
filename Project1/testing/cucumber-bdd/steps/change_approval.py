from behave import *


@given('a user is on the manager dashboard page and a user is in a manager session')
def test_user_on_manager_dash_and_in_session(context):
    pass

@when('a user clicks the approve button')
def test_user_clicks_approve_button(context):
    pass

@then('the reimbursement\'s approval changes to "approved"')
def test_reimbursement_approval_is_approved(context):
    pass

@when('a user clicks the deny button')
def test_user_clicks_deny_button(context):
    pass

@then('the reimbursement\'s approval changes to "denied"')
def test_reimbursement_approval_is_approved(context):
    pass

@when('a user clicks the confirm approvals button')
def test_user_clicks_confirm_button(context):
    pass

@then('all reimbursement approval changes are made')
def test_approvals_changed(context):
    pass
