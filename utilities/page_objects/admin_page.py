from utilities.page_objects.base_page import BasePage
from utilities.constants import MAX_WAIT_INTERVAL
from selenium.webdriver.common.by import By
import time

class Admin_Page(BasePage):

    ADD_NEW_RECORD = (By.XPATH,"//div[@class='orangehrm-header-container']/button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
    USER_ROLE = (By.XPATH,"//div[@class='oxd-grid-2 orangehrm-full-width-grid']//div[@class='oxd-select-text--after' and @data-v-67d2aedf=''][1]")
    HIDDEN_DROPDOWN_OPTION = (By.CSS_SELECTOR, "div[role='listbox']")
    USER_STATUS = (By.XPATH,"//div[@class='oxd-grid-2 orangehrm-full-width-grid']//div[@class='oxd-grid-item oxd-grid-item--gutters'][3]//div[@class='oxd-select-text--after' and @data-v-67d2aedf='']")
    EMPLOYEE_NAME = (By.XPATH,"//input[@data-v-75e744cd = '']")
    EMPLOYEE_HIDDEN_OPTION_1 = (By.CSS_SELECTOR, "div.oxd-grid-item.oxd-grid-item--gutters:nth-child(2) div[role='listbox']")
    USER_NAME = (By.XPATH,"//div[@class='oxd-grid-item oxd-grid-item--gutters'][4]//input[@data-v-1f99f73c='']")
    CREATE_PWD = (By.XPATH,"//div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']//input[@type='password']")
    CONFIRM_PWD = (By.XPATH,"//div[@class='oxd-form-row user-password-row']//div[@class='oxd-grid-item oxd-grid-item--gutters']//input[@type='password']")
    SAVE_BUTTON = (By.XPATH,"//div[@class='oxd-form-actions']/button[2]")
    SEARCH_BAR = (By.XPATH,"//div[@class='oxd-grid-item oxd-grid-item--gutters'][3]//input[@data-v-75e744cd = '']")
    EMPLOYEE_HIDDEN_OPTION_2 = (By.CSS_SELECTOR, "div.oxd-grid-item.oxd-grid-item--gutters:nth-child(3) div[role='listbox']")

    USER_NAME_TAG = (By.XPATH, "//div[@class='oxd-table-card']//div[@class='oxd-table-cell oxd-padding-cell'][2]/div")
    USER_ROLE_TAG = (By.XPATH, "//div[@class='oxd-table-card']//div[@class='oxd-table-cell oxd-padding-cell'][3]/div")
    EMPLOYEE_NAME_TAG = (By.XPATH, "//div[@class='oxd-table-card']//div[@class='oxd-table-cell oxd-padding-cell'][4]/div")
    USER_STATUS_TAG = (By.XPATH, "//div[@class='oxd-table-card']//div[@class='oxd-table-cell oxd-padding-cell'][5]/div")

    def click_add_new_record(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.ADD_NEW_RECORD).click()

    def select_user_role(self, user_role):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.USER_ROLE).click()
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.HIDDEN_DROPDOWN_OPTION).find_element(By.XPATH, f"//span[text()='{user_role}']").click()

    def select_user_status(self, user_status):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.USER_STATUS).click()
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.HIDDEN_DROPDOWN_OPTION).find_element(By.XPATH, f"//span[text()='{user_status}']").click()

    def fill_employee_name_for_hint(self, employee_first_name):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.EMPLOYEE_NAME).send_keys(employee_first_name)
        time.sleep(1)

    def create_user_name(self, user_name):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.USER_NAME).send_keys(user_name)
        time.sleep(1)

    def create_password(self, pwd):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.CREATE_PWD).send_keys(pwd)
        time.sleep(1)

    def confirm_password(self, pwd):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.CONFIRM_PWD).send_keys(pwd)
        time.sleep(1)

    def click_save_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.SAVE_BUTTON).click()


    def search_employee_name(self, employee_first_name):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.SEARCH_BAR).send_keys(employee_first_name)
        time.sleep(1)

    def click_search_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.SAVE_BUTTON).click()

    def get_user_name(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.USER_NAME_TAG).text

    def get_user_role(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.USER_ROLE_TAG).text

    def get_employee_name(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.EMPLOYEE_NAME_TAG).text

    def get_user_status(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.USER_STATUS_TAG).text