class CartPage:
    
    checkout_button_class = 'checkout_button'

    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        self.driver.find_element_by_class_name(self.checkout_button_class).click()
