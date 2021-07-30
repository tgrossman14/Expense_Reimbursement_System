class InventoryPage:

    backpack_button_id = 'add-to-cart-sauce-labs-backpack'
    cart_link_css_selector = '#shopping_cart_container > a'

    def __init__(self, driver):
        self.driver = driver
    
    def add_backpack_to_cart(self):
        # Purchase backpack
        self.driver.find_element_by_id(self.backpack_button_id).click()

    def go_to_shopping_cart(self):
        # The link to view cart has no ID. Using CSS selector to locate em instead
        self.driver.find_element_by_css_selector(self.cart_link_css_selector).click()
