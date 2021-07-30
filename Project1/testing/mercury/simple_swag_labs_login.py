# Must place WebDriver on PATH
# Import webdriver from selenium

from selenium import webdriver
import time
from testing.mercury.poms.swaglabs.swag_labs_login_page import SwagLabsLoginPage
from testing.mercury.poms.swaglabs.inventory_page import InventoryPage
from testing.mercury.poms.swaglabs.cart_page import CartPage
from testing.mercury.poms.swaglabs.checkout_step_one_page import CheckoutStepOne
from testing.mercury.poms.swaglabs.checkout_step_two_page import CheckoutStepTwo
# Explicit waits require imports:
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# Correctly located ems may raise a NoSuchElementException. The em may not have rendered yet
# Selenium waits allow driver to wait a certain amount of time before attempting to grab and interact w/ an em


# Can pass in driver to Chrome() if not on PATH.
driver = webdriver.Chrome(executable_path=r"C:\Users\Tal\6-7-2021-pyjwa\chromedriver")


# Implicit waits- Driver polls the DOM for a specified number of seconds before trying to find any em that has not been rendered.
# Will wait for a maximum number of seconds and poll periodically during that time for the em
# Implicit waits not preferred. Applies to all web ems and the wait for the lifetime of the driver.
driver.implicitly_wait(5)


# Explicit waits- Waits for a certain condition to occur before interacting with ems.
# Applies only to specified ems.
WebDriverWait(driver, 5, 1).until(EC.visibility_of_element_located(By.CLASS_NAME('bot_column')))

# Navigate to home page of Swag Labs
driver.get('https://www.saucedemo.com/')

# Using POM to login to SwagLabs
sll_page = SwagLabsLoginPage(driver)
sll_page.enter_credentials()
sll_page.click_login_button()
sll_page.hit_enter_button_to_login()

# On inventory page theoretically. Can be checked
assert 'inventory' in driver.current_url

inv_page = InventoryPage(driver)
inv_page.add_backpack_to_cart()
inv_page.go_to_shopping_cart()


# Check if in cart
assert 'cart' in driver.current_url

cart_page = CartPage(driver)
cart_page.checkout()

# Check if in first step of checkout
assert 'checkout-step-one' in driver.current_url

cos1_page = CheckoutStepOne(driver)
cos1_page.enter_personal_info()

# Finish checkout
assert 'checkout-step-two' in driver.current_url

cos2_page = CheckoutStepTwo(driver)
cos2_page.click_finish()

# Check if driver is complete
assert 'checkout-complete' in driver.current_url

# Seconds waited before next step is proceeded to
# time.sleep(1)


# Close- Closes current window
# Quit- Closes browser and stops executable. Effectively teardown
driver.quit()