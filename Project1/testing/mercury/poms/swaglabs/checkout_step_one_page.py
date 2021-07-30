class CheckoutStepOne:

    # xpath- XML path language. Last resort (especially full xpath). Powerful, but unstable.
    first_name_box_xpath = '//*[@id="first-name"]'
    last_name_box_id = 'last-name'
    postal_code_box_id = 'postal-code'
    continue_button_id = 'continue'

    def __init__(self, driver):
        self.driver = driver

    def enter_personal_info(self):
        self.driver.find_element_by_xpath(self.first_name_box_xpath).send_keys('first')
        self.driver.find_element_by_id(self.last_name_box_id).send_keys('last')
        self.driver.find_element_by_id(self.postal_code_box_id).send_keys('12345')
        self.driver.find_element_by_id(self.continue_button_id).click()
