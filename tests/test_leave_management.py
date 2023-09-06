from selenium.webdriver.support.wait import WebDriverWait

from test_units import *
from utilities.constants import CANDIDATE_FN, CANDIDATE_LN, LEAVE_TYPE, LEAVE_START_DATE, MAX_WAIT_INTERVAL, \
    LEAVE_STATUS
from utilities.page_objects.index_page import Index_Page
from utilities.page_objects.leave_page import Leave_Page


class Test_05_Leave_Management:
    # Test case 05: assign leave for target employee
    def test_assign_leave(self, logged_in_browser):
        # click on Leave tab and click assign_leave:
        index_page = Index_Page(logged_in_browser)
        index_page.click_leave()
        leave_page = Leave_Page(logged_in_browser)
        leave_page.click_assign_leave()

        # fill in employee name and click from autosuggestion
        leave_page.search_employee_1(CANDIDATE_FN)
        autosuggestions = leave_page.explicitly_wait_and_visible_all_elements(MAX_WAIT_INTERVAL, leave_page.EMP_HIDDEN_OPTION)
        WebDriverWait(logged_in_browser, 10).until(lambda driver: next((option for option in autosuggestions if option.text == (CANDIDATE_FN+' '+CANDIDATE_LN)), None)).click()
        # select leave type
        leave_page.select_leave_type(LEAVE_TYPE)
        # fill in leave start date
        leave_page.fill_start_date(LEAVE_START_DATE)
        # click assign button
        leave_page.click_assign_button()
        leave_page.click_assign_button()
        # accept alert
        leave_page.accept_alert()
        # click leave list to view scheduled leave
        leave_page.click_leave_list()
        # deselect existing leave type and select again
        leave_page.deselect_and_select_leave_statue(LEAVE_STATUS)
        # type employee name in search bar and click from autosuggestion
        leave_page.search_employee_2(CANDIDATE_FN)
        autosuggestions = leave_page.explicitly_wait_and_visible_all_elements(MAX_WAIT_INTERVAL, leave_page.HIDDEN_DROPDOWN_OPTION)
        WebDriverWait(logged_in_browser, 10).until(lambda driver: next((option for option in autosuggestions if option.text == (CANDIDATE_FN+' '+CANDIDATE_LN)), None)).click()
        # click search button
        leave_page.click_search_button()

        leave_period_label = leave_page.get_leave_period_tag()
        emp_name_label = leave_page.get_emp_name_tag()
        leave_type_label = leave_page.get_leave_type_tag()
        assert leave_period_label == LEAVE_START_DATE
        assert emp_name_label == (CANDIDATE_FN+' '+CANDIDATE_LN)
        assert leave_type_label == LEAVE_TYPE
        # end of test case 05

