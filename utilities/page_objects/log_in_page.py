from utilities.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from utilities.constants import MAX_WAIT_INTERVAL

class Log_In_Page(BasePage):
    USER_NAME = (By.XPATH, "//input[@name='username']")
    PASSWORD = (By.XPATH, "//input[@name='password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")

    def fill_user_name(self, username):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.USER_NAME).send_keys(username)

    def fill_password(self, pw):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.PASSWORD).send_keys(pw)

    def click_submit_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.SUBMIT_BUTTON).click()