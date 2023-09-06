from utilities.page_objects.base_page import BasePage
from utilities.constants import MAX_WAIT_INTERVAL
from selenium.webdriver.common.by import By
import time

class PIM_Page(BasePage):
    SEARCH_BAR_EMP_NAME = (By.XPATH,"//div[@class='oxd-grid-item oxd-grid-item--gutters'][1]//input[@data-v-75e744cd = '']")
    EMP_HIDDEN_OPTION = (By.CSS_SELECTOR, "div.oxd-grid-item.oxd-grid-item--gutters:nth-child(1) div[role='listbox']")
    SAVE_BUTTON_1 = (By.XPATH,"//div[@class='oxd-form-actions']/button[2]")

    EMP_FIRST_NAME_TAG = (By.XPATH,"//div[@class='oxd-table-cell oxd-padding-cell'][3]/div")
    EMP_LAST_NAME_TAG = (By.XPATH,"//div[@class='oxd-table-cell oxd-padding-cell'][4]/div")
    JOB_TITLE_TAG = (By.XPATH,"//div[@class='oxd-table-cell oxd-padding-cell'][5]/div")
    SAVE_BUTTON_2 = (By.XPATH,"//div[@class='oxd-table-cell-actions']/button[2]")

    EMP_ID = (By.XPATH, "//div[@class='oxd-form-row'][2]/div[1]/div[1]//input")
    SIN = (By.XPATH,"//div[@class='oxd-form-row'][2]/div[3]/div[1]//input")
    NATIONALITY = (By.XPATH, "//div[@class='oxd-form-row'][3]/div[1]/div[1]//div[@class='oxd-select-text--after']")
    HIDDEN_OPTION = (By.CSS_SELECTOR, "div[role='listbox']")
    DOB = (By.XPATH,"//div[@class='oxd-form-row'][3]/div[2]/div[1]//input[@placeholder='yyyy-mm-dd']")
    GENDER_FEMALE = (By.XPATH,"//div[@class='--gender-grouped-field']/div[2]//div[@class='oxd-radio-wrapper']")
    SAVE_BUTTON_3 = (By.XPATH, "//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@type='submit']")
    NATIONALITY_TAG = (By.XPATH, "//div[@class='oxd-form-row'][3]/div[1]/div[1]//div[@class='oxd-select-text-input']")

    def fill_emp_name_for_hint(self, employee_first_name):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.SEARCH_BAR_EMP_NAME).send_keys(employee_first_name)
        time.sleep(1)

    def click_search_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.SAVE_BUTTON_1).click()

    def get_emp_first_name_tag(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.EMP_FIRST_NAME_TAG).text

    def get_emp_last_name_tag(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.EMP_LAST_NAME_TAG).text

    def get_job_position(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.JOB_TITLE_TAG).text

    def click_edit_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.SAVE_BUTTON_2).click()

    def create_emp_id(self, emp_id):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.EMP_ID).send_keys(emp_id)
        time.sleep(1)

    def fill_sin(self, emp_sin):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.SIN).send_keys(emp_sin)
        time.sleep(1)

    def select_nationality(self, nationality):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.NATIONALITY).click()
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.HIDDEN_OPTION).find_element(By.XPATH, f"//span[text()='{nationality}']").click()
        time.sleep(1)

    def eneter_DOB(self, DOB):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.DOB).send_keys(DOB)
        time.sleep(1)

    def select_gender(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.GENDER_FEMALE).click()
        time.sleep(1)

    def click_save_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.SAVE_BUTTON_3).click()

    def get_emp_id_tag(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.EMP_ID).get_attribute("value")

    def get_emp_sin_tag(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.SIN).get_attribute("value")

    def get_emp_nationality(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.NATIONALITY_TAG).text

    def get_emp_DOB(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.DOB).get_attribute("value")


