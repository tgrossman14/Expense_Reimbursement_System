class CheckoutStepTwo:

    finish_button_id = 'finish'

    def __init__(self, driver):
        self.driver = driver
    
    def click_finish(self):
        self.driver.find_element_by_id(self.finish_button_id).click()
