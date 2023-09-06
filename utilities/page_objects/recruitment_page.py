from utilities.page_objects.base_page import BasePage
from utilities.constants import MAX_WAIT_INTERVAL
from selenium.webdriver.common.by import By
import time

class Recruitment_Page(BasePage):
    # Add new candidate page
    ADD_NEW_RECORD = (By.XPATH, "//div[@class='orangehrm-header-container']/button")
    PAGE_TITLE = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
    SECTION_TITLE = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title']")
    FIRST_NAME = (By.XPATH, "//input[@name='firstName']")
    LAST_NAME = (By.XPATH, "//input[@name='lastName']")
    VACANCY = (By.XPATH, "//div[@class='oxd-select-wrapper']/div/div[2]")
    HIDDEN_DROPDOWN_OPTION = (By.CSS_SELECTOR, "div[role='listbox']")
    EMAIL = (By.XPATH, "//div[@class='oxd-form-row']/div/div[1]/div/div[2]/input")
    RESUME = (By.XPATH, "//input[@class='oxd-file-input']")
    APPLICATION_DATE = (By.XPATH, "//div[@class='oxd-date-input']/input")
    SAVE_BUTTON_1 = (By.XPATH, "//button[@type='submit']")

    # Application stage - shortlist
    SAVED_CANDIDATE_NAME_TAG = (By.XPATH, "//div[@class='oxd-grid-3 orangehrm-full-width-grid']/div[1]/div/div[2]/p")
    APPLICATION_STAGE = (By.XPATH, "//div[@class='orangehrm-recruitment']/div[1]/p")
    SHORTLIST_BUTTON = (By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--success']")
    SAVE_BUTTON_2 = (By.XPATH,"//div[@class='oxd-form-actions']/button[2]")

    # Application stage - schedule interview, interview passed
    SAVE_BUTTON_3 = (By.XPATH, "//div[@class='orangehrm-recruitment-actions']/button[2]")
    INTERVIEWER_POSITION = (By.XPATH, "//div[@class='oxd-form-row'][2]//div[@class='oxd-grid-item oxd-grid-item--gutters']//input")
    INTERVIEWER_NAME = (By.XPATH, "//div[@class='oxd-autocomplete-text-input oxd-autocomplete-text-input--active']/input")
    INTERVIEW_DATE = (By.XPATH,"//div[@class='oxd-date-input']/input")
    SAVE_BUTTON_4 = (By.XPATH, "//div[@class='orangehrm-recruitment']/div[2]/button[3]")

    # Application stage = offer job, hire
    OFFER_JOB = (By.XPATH, "//div[@class='orangehrm-recruitment']/div[2]/button[3]")
    HIRE = (By.XPATH, "//div[@class='orangehrm-recruitment']/div[2]/button[3]")

    def get_page_title(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.PAGE_TITLE).text

    def get_section_title(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.SECTION_TITLE).text
    def click_add_new_record(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.ADD_NEW_RECORD).click()

    def fill_first_name(self, fn):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.FIRST_NAME).send_keys(fn)
        time.sleep(1)

    def fill_last_name(self, ln):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.LAST_NAME).send_keys(ln)
        time.sleep(1)

    def select_vacancy(self, position):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.VACANCY).click()
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.HIDDEN_DROPDOWN_OPTION).find_element(By.XPATH, f"//span[text()='{position}']").click()

    def fill_email(self, email):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.EMAIL).send_keys(email)
        time.sleep(1)

    def upload_resume(self, filepath):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.RESUME).send_keys(filepath)

    def fill_application_date(self, date):
        self.driver.execute_script("arguments[0].value = arguments[1];",self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.APPLICATION_DATE),date)
        time.sleep(1)

    def click_save_button_1(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.SAVE_BUTTON_1).click()

    def get_saved_candidate_name(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.SAVED_CANDIDATE_NAME_TAG).text

    def get_application_stage(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.APPLICATION_STAGE).text

    def click_shortlist(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.SHORTLIST_BUTTON).click()

    def click_save_button_2(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.SAVE_BUTTON_2).click()

    def click_save_button_3(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.SAVE_BUTTON_3).click()

    def fill_interviewer_position(self, interviewer_position):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.INTERVIEWER_POSITION).send_keys(interviewer_position)
        time.sleep(1)

    def fill_interviewer_name_for_hint(self, interviewer_firstname):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.INTERVIEWER_NAME).send_keys(interviewer_firstname)
        time.sleep(1)

    def fill_interview_date(self, date):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.INTERVIEW_DATE).send_keys(date)
        time.sleep(1)

    def click_save_button_4(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.SAVE_BUTTON_4).click()

