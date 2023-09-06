from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver


class BasePage:

    def __init__(self, logged_in_browser):
        self.driver = logged_in_browser

    def get_current_url(self):
        return self.driver.current_url

    def navigate_to(self,url):
        self.driver.get(url)

    def explicitly_wait_and_find_element(self,interval,locator_type_and_locator_tuple):
        return WebDriverWait(self.driver, interval).until(
                ec.presence_of_element_located(locator_type_and_locator_tuple))

    def scroll_down_browser_window(self):
        self.driver.execute_script("window.scrollBy(0, 500);")

    def take_screenshot(self,file_path):
        self.driver.save_screenshot(file_path)

    def explicitly_wait_and_visible_all_elements(self,interval,locator_type_and_locator_tuple):
        return WebDriverWait(self.driver, interval).until(
            ec.visibility_of_all_elements_located(locator_type_and_locator_tuple))
