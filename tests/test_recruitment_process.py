from selenium.webdriver.support.wait import WebDriverWait

from test_units import *
from utilities.constants import CANDIDATE_FN, CANDIDATE_LN, POSITION_VACANCY, CANDIDATE_EMAIL, RESUME_LOCAL_PATH, \
    APPLICATION_DATE, INTERVIEWER_POSITION, INTERVIEWER_FULL_NAME, INTERVIEWER_FIRST_NAME, INTERVIEW_DATE, \
    MAX_WAIT_INTERVAL, SCREENSHOT_PATH
from utilities.page_objects.index_page import Index_Page
from utilities.page_objects.recruitment_page import Recruitment_Page


class Test_02_Recruitment:

    #Test case 02-01: enter new record for recruitment:
    def test_create_new_candidate(self, logged_in_browser):
        # Click on Recruitment tab and add new candidate record:
        index_page = Index_Page(logged_in_browser)
        index_page.click_recruitment()
        recruitment_page = Recruitment_Page(logged_in_browser)
        assert recruitment_page.get_page_title() == "Recruitment", "Target page loaded successfully"
        recruitment_page.click_add_new_record()
        assert recruitment_page.get_section_title() == "Add Candidate", "Target page loaded successfully"

        # Fill in candidate information and save:
        recruitment_page.fill_first_name(CANDIDATE_FN)
        recruitment_page.fill_last_name(CANDIDATE_LN)
        recruitment_page.select_vacancy(POSITION_VACANCY)
        recruitment_page.fill_email(CANDIDATE_EMAIL)
        recruitment_page.upload_resume(RESUME_LOCAL_PATH)
        recruitment_page.fill_application_date(APPLICATION_DATE)
        recruitment_page.click_save_button_1()
        candidate_name_tag = recruitment_page.get_saved_candidate_name()
        assert candidate_name_tag == (CANDIDATE_FN +' '+CANDIDATE_LN)
        application_stage_1 = recruitment_page.get_application_stage()
        assert application_stage_1.__contains__("Application Initiated")

    #Test case 02-02: Click shortlist and save:
    def test_shortlist(self, logged_in_browser):
        recruitment_page = Recruitment_Page(logged_in_browser)
        recruitment_page.click_shortlist()
        recruitment_page.click_save_button_2()
        application_stage_2 = recruitment_page.get_application_stage()
        assert application_stage_2.__contains__("Shortlisted")

    #Test case 02-03: Click schedule interview and fill in information:
    def test_schedule_interview(self, logged_in_browser):
        recruitment_page = Recruitment_Page(logged_in_browser)
        recruitment_page.click_save_button_3()
        # select vacant job position
        recruitment_page.fill_interviewer_position(INTERVIEWER_POSITION)
        # type interviewer first name and click from autosuggestion
        recruitment_page.fill_interviewer_name_for_hint(INTERVIEWER_FIRST_NAME)
        autosuggestions = recruitment_page.explicitly_wait_and_visible_all_elements(MAX_WAIT_INTERVAL,recruitment_page.HIDDEN_DROPDOWN_OPTION)
        WebDriverWait(logged_in_browser, 10).until(lambda driver:next((option for option in autosuggestions if option.text == INTERVIEWER_FULL_NAME), None)).click()
        # schedule interview date
        recruitment_page.fill_interview_date(INTERVIEW_DATE)
        # click save and proceed
        recruitment_page.click_save_button_2()
        application_stage_3 = recruitment_page.get_application_stage()
        assert application_stage_3.__contains__("Interview Scheduled")

    #Test case 02-04: Click interview passed and save:
    def test_click_interview_passed(self, logged_in_browser):
        recruitment_page = Recruitment_Page(logged_in_browser)
        recruitment_page.click_save_button_4()
        recruitment_page.click_save_button_2()
        application_stage_4 = recruitment_page.get_application_stage()
        assert application_stage_4.__contains__("Interview Passed")

    #Test case 02-05: Click offer jop and save:
    def test_click_offer_job(self, logged_in_browser):
        recruitment_page = Recruitment_Page(logged_in_browser)
        recruitment_page.click_save_button_4()
        recruitment_page.click_save_button_2()
        application_stage_5 = recruitment_page.get_application_stage()
        assert application_stage_5.__contains__("Job Offered")

    #Test case 02-06: Click offer jop and save screenshot of progresses:
    def test_click_hire(self, logged_in_browser):
        recruitment_page = Recruitment_Page(logged_in_browser)
        recruitment_page.click_save_button_4()
        recruitment_page.click_save_button_2()
        application_stage_6 = recruitment_page.get_application_stage()
        assert application_stage_6.__contains__("Hired")
        recruitment_page.scroll_down_browser_window()
        recruitment_page.take_screenshot(SCREENSHOT_PATH)

    # End of test case 02


