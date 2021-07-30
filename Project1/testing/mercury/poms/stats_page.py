class StatsPage:
    manager_dash_link = 'manager_dash'

    def __init__(self, driver):
        self.driver = driver
    
    def go_to_manager_dash(self):
        self.driver.find_element_by_id(self.manager_dash_link).click()