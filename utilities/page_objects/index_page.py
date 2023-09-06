from utilities.page_objects.base_page import BasePage
from utilities.constants import MAX_WAIT_INTERVAL
from selenium.webdriver.common.by import By

class Index_Page(BasePage):
    ADMIN = (By.XPATH, "//div[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a")
    PIM = (By.XPATH, "//div[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a")
    LEAVE = (By.XPATH, "//div[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a")
    RECRUITMENT = (By.XPATH, "//div[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a")

    def click_admin(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.ADMIN).click()

    def click_pim(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.PIM).click()

    def click_leave(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.LEAVE).click()

    def click_recruitment(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.RECRUITMENT).click()

