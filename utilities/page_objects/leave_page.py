from utilities.page_objects.base_page import BasePage
from utilities.constants import MAX_WAIT_INTERVAL
from selenium.webdriver.common.by import By
import time

class Leave_Page(BasePage):
    ASSIGN_LEAVE = (By.XPATH,"//li[@class='oxd-topbar-body-nav-tab'][3]")
    EMPLOYEE_NAME = (By.XPATH,"//div[@class='oxd-form-row'][1]//input[@data-v-75e744cd = '']")
    EMP_HIDDEN_OPTION = (By.CSS_SELECTOR, "div.oxd-grid-item.oxd-grid-item--gutters:nth-child(1) div[role='listbox']")
    LEAVE_TYPE_1 = (By.XPATH, "//div[@class='oxd-form-row'][2]//div[@class='oxd-select-text--after']")
    HIDDEN_DROPDOWN_OPTION = (By.CSS_SELECTOR, "div[role='listbox']")
    START_DATE = (By.XPATH,"//div[@class='oxd-form-row'][3]/div/div[1]//input[@placeholder='yyyy-mm-dd']")
    ASSIGN_BUTTON = (By.XPATH,"//div[@class='oxd-form-actions']/button")

    CONFIRM_BUTTON = (By.XPATH,"//div[@class='oxd-dialog-container-default--inner']//button[@type='button'][2]")

    LEAVE_LIST_BUTTON = (By.XPATH,"//li[@class='oxd-topbar-body-nav-tab'][3]")
    DESELECT_LEAVE_TYPE = (By.XPATH,"//div[@class='oxd-form-row'][1]/div/div[@class='oxd-grid-item oxd-grid-item--gutters'][3]//i[@class='oxd-icon bi-x --clear']")
    LEAVE_TYPE_2 = (By.XPATH, "//div[@class='oxd-form-row'][1]/div/div[@class='oxd-grid-item oxd-grid-item--gutters'][3]//div[@class='oxd-select-text--after']")
    EMP_NAME_SEARCH_BAR = (By.XPATH,"//div[@class='oxd-form-row'][2]/div/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]//input[@data-v-75e744cd = '']")
    SEARCH_BUTTON = (By.XPATH,"//div[@class='oxd-form-actions']/button[2]")

    LEAVE_PERIOD_TAG = (By.XPATH,"//div[@class='oxd-table-body']//div[@class='oxd-table-cell oxd-padding-cell'][2]/div")
    EMP_NAME_TAG = (By.XPATH,"//div[@class='oxd-table-body']//div[@class='oxd-table-cell oxd-padding-cell'][3]/div")
    LEAVE_TYPE_TAG = (By.XPATH,"//div[@class='oxd-table-body']//div[@class='oxd-table-cell oxd-padding-cell'][4]/div")

    def click_assign_leave(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.ASSIGN_LEAVE).click()

    def search_employee_1(self, employee_first_name):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.EMPLOYEE_NAME).send_keys(employee_first_name)
        time.sleep(1)

    def select_leave_type(self, leave_type):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.LEAVE_TYPE_1).click()
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.HIDDEN_DROPDOWN_OPTION).find_element(By.XPATH, f"//span[text()='{leave_type}']").click()
        time.sleep(1)

    def fill_start_date(self, start_date):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.START_DATE).send_keys(start_date)
        time.sleep(1)

    def click_assign_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.ASSIGN_BUTTON).click()

    def accept_alert(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.CONFIRM_BUTTON).click()

    def click_leave_list(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.LEAVE_LIST_BUTTON).click()

    def deselect_and_select_leave_statue(self, leave_status):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.DESELECT_LEAVE_TYPE).click()
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.LEAVE_TYPE_2).click()
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.HIDDEN_DROPDOWN_OPTION).find_element(By.XPATH, f"//span[text()='{leave_status}']").click()
        time.sleep(1)

    def search_employee_2(self, employee_first_name):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.EMP_NAME_SEARCH_BAR).send_keys(employee_first_name)
        time.sleep(1)

    def click_search_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.SEARCH_BUTTON).click()

    def get_leave_period_tag(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.LEAVE_PERIOD_TAG).text

    def get_emp_name_tag(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.EMP_NAME_TAG).text

    def get_leave_type_tag(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.LEAVE_TYPE_TAG).text












