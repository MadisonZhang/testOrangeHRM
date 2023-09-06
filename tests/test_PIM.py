from selenium.webdriver.support.wait import WebDriverWait

from test_units import *
from utilities.constants import CANDIDATE_FN, CANDIDATE_LN, EMP_ID, EMP_SIN, EMP_NATIONALITY, EMP_DOB, POSITION_VACANCY, \
    MAX_WAIT_INTERVAL
from utilities.page_objects.PIM_page import PIM_Page
from utilities.page_objects.index_page import Index_Page
import time


class Test_04_PIM:
    # Test case 04-01: search for target employee:
    def test_employee_search(self, logged_in_browser):
        # click on PIM tab and search for target employee:
        index_page = Index_Page(logged_in_browser)
        index_page.click_pim()
        pim_page = PIM_Page(logged_in_browser)

        pim_page.fill_emp_name_for_hint(CANDIDATE_FN)
        autosuggestions = pim_page.explicitly_wait_and_visible_all_elements(MAX_WAIT_INTERVAL, pim_page.EMP_HIDDEN_OPTION)
        WebDriverWait(logged_in_browser, 10).until(lambda driver: next((option for option in autosuggestions if option.text == (CANDIDATE_FN+' '+CANDIDATE_LN)), None)).click()
        pim_page.click_search_button()

        emp_first_name_label = pim_page.get_emp_first_name_tag()
        emp_last_name_label = pim_page.get_emp_last_name_tag()
        emp_job_position_label = pim_page.get_job_position()
        assert emp_first_name_label == CANDIDATE_FN
        assert emp_last_name_label == CANDIDATE_LN
        assert emp_job_position_label == POSITION_VACANCY

    def test_edit_personal_details(self, logged_in_browser):
        pim_page = PIM_Page(logged_in_browser)
        pim_page.click_edit_button()
        # wait for page to load and create employee id
        time.sleep(5)
        pim_page.create_emp_id(EMP_ID)
        # fill in employee SIN
        pim_page.fill_sin(EMP_SIN)
        # select employee nationality
        pim_page.select_nationality(EMP_NATIONALITY)
        # fill in employee DOB
        pim_page.eneter_DOB(EMP_DOB)
        # select employee gender - female
        pim_page.select_gender()
        # click save
        pim_page.click_save_button()

        emp_id_label = pim_page.get_emp_id_tag()
        emp_sin_label = pim_page.get_emp_sin_tag()
        emp_nationality_label = pim_page.get_emp_nationality()
        emp_DOB_label = pim_page.get_emp_DOB()
        assert emp_id_label == EMP_ID
        assert emp_sin_label == EMP_SIN
        assert emp_nationality_label == EMP_NATIONALITY
        assert emp_DOB_label == EMP_DOB

