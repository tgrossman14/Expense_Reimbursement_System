from selenium import webdriver
from testing.mercury.poms.login_page import MASHLoginPage
from testing.mercury.poms.employee_dash_page import EmployeeDashPage
from testing.mercury.poms.manager_dash_page import ManagerDashPage

driver = webdriver.Chrome(executable_path=r"C:\Users\Tal\6-7-2021-pyjwa\chromedriver")


# Navigate to home page
driver.get('http://localhost:5000/login.html')


# Login page #
ml_page = MASHLoginPage(driver)
ml_page.enter_credentials()
ml_page.click_login_button()
ml_page.hit_enter_button_to_login()


# Employee dash page #
assert 'employee' in driver.current_url
ed_page = EmployeeDashPage()
ed_page.click_amount_column()
ed_page.click_approval_column()
# Correct reimbursement
ed_page.enter_valid_amount()
ed_page.enter_valid_reason()
ed_page.submit_new_reimbursement()
# Incorrect reimbursement1
ed_page.enter_valid_amount()
ed_page.enter_invalid_reason()
ed_page.submit_new_reimbursement()
# Incorrect reimbursement2
ed_page.enter_invalid_amount()
ed_page.enter_valid_reason()
ed_page.submit_new_reimbursement()
# Incorrect reimbursement3
ed_page.enter_invalid_amount()
ed_page.enter_invalid_reason()
ed_page.submit_new_reimbursement()

# Manager dash page #
assert 'manager' in driver.current_url
md_page = ManagerDashPage()
md_page.click_amount_column()
md_page.click_approval_column()
md_page.click_approve_button()
md_page.click_deny_button()
md_page.click_confirm_button()

# Close driver #
driver.quit()
