# Simulate an end user clicking keyboard keys. Keys class.
from selenium.webdriver.common.keys import Keys

# POM- Page Object Model. Serves as a repository of locators for ems on a webpage. Often includes useful methods for interacting w/ these ems.
# POM design pattern- Saves time via reusability to later grab ems from this page. Can be tedious to make a POM for each view in a UI.


# Base page class to be inherited from
class SwagLabsLoginPage:
    # Define ems that should exist in the repository. Only use the locators
    username_box_id = 'user-name'
    password_box_id = 'password'
    login_button_id = 'login-button'

    # Common to see driver passed into the class constructor.
    def __init__(self, driver):
        self.driver = driver
    
    def enter_credentials(self):
        # Basic selection of a web element by ID. ID is one of the 8 basic "Selenium locators"
        # NoSuchElementException raised for an invalid ID or an unrendered
        # Typing into boxes
        # Do not hard code credentials normally. Use envrionment variables instead.
        self.driver.find_element_by_id(self.username_box_id).send_keys('standard_user')
        self.driver.find_element_by_id(self.password_box_id).send_keys('secret_sauce')
    
    def click_login_button(self):
        self.driver.find_element_by_id(self.login_button_id).click()
    
    def hit_enter_button_to_login(self):
        self.driver.find_element_by_id(self.password_box_id).send_keys(Keys.ENTER)
