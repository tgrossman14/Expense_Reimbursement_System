class ManagerDashPage:
    approval_column_id = 'approval_column'
    amount_column_id = 'amount_column'
    approve_button_id = 'approve_button'
    deny_button_id = 'deny_button'
    confirm_button_id = 'confirm_button'
    stats_page_link = 'stats_page'
    reimbursement_id = 'reimbursement_row'

    def __init__(self, driver):
        self.driver = driver
    
    def click_reimbursement(self):
        self.driver.find_element_by_id(self.reimbursement_id).click()

    def click_approve_button(self):
        self.driver.find_element_by_id(self.approve_button_id).click()

    def click_deny_button(self):
        self.driver.find_element_by_id(self.deny_button_id).click()

    def click_confirm_button(self):
        self.driver.find_element_by_id(self.confirm_button_id).click()
    
    def go_to_stats(self):
        self.driver.find_element_by_id(self.stats_page_link).click()
