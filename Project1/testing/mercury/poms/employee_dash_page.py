class EmployeeDashPage:
    approval_column_id = 'approval_column'
    amount_column_id = 'amount_column'
    reason_box_id = 'reason_box'
    amount_box_id = 'amount_box'
    submit_button_id = 'submit_button'

    def __init__(self, driver):
        self.driver = driver

    def enter_valid_amount(self):
        self.driver.find_element_by_id(self.amount_box_id).send_keys('111.11')

    def enter_invalid_amount(self):
        self.driver.find_element_by_id(self.amount_box_id).send_keys('abcd')

    def enter_valid_reason(self):
        self.driver.find_element_by_id(self.reason_box_id).send_keys('Lorem ipsum')

    def enter_invalid_reason(self):
        self.driver.find_element_by_id(self.reason_box_id).send_keys('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec non est fermentum, mattis ipsum dictum, finibus elit.')

    def submit_new_reimbursement(self):
        self.driver.find_element_by_id(self.submit_button_id).click()
