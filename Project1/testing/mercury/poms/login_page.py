from selenium.webdriver.common.keys import Keys


class MASHLoginPage:
    email_box_id = 'email'
    password_box_id = 'password'
    login_button_id = 'login-button'

    def __init__(self, driver):
        self.driver = driver

    def enter_manager_credentials(self):
        self.driver.find_element_by_id(self.email_box_id).send_keys('standard_user')
        self.driver.find_element_by_id(self.password_box_id).send_keys('secret_sauce')
    
    def enter_employee_credentials(self):
        self.driver.find_element_by_id(self.email_box_id).send_keys('standard_user')
        self.driver.find_element_by_id(self.password_box_id).send_keys('secret_sauce')
    
    def invalid_credentials(self):
        self.driver.find_element_by_id(self.email_box_id).send_keys('standard_user')
        self.driver.find_element_by_id(self.password_box_id).send_keys('secret_sauce')
    

    def click_login_button(self):
        self.driver.find_element_by_id(self.login_button_id).click()
    
    def hit_enter_button_to_login(self):
        self.driver.find_element_by_id(self.password_box_id).send_keys(Keys.ENTER)
