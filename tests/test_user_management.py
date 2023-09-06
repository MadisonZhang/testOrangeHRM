from selenium.webdriver.support.wait import WebDriverWait

from test_units import *
from utilities.constants import CANDIDATE_FN, CANDIDATE_LN, USER_NAME, USER_STATUS, USER_ROLE, USER_PWD, \
   MAX_WAIT_INTERVAL
from utilities.page_objects.admin_page import Admin_Page
from utilities.page_objects.index_page import Index_Page
import time

class Test_03_Admin:

    # Test case 03-01: enter new record for user management:
   def test_create_new_user(self, logged_in_browser):
      # click on Recruitment tab and add new candidate record:
      index_page = Index_Page(logged_in_browser)
      index_page.click_admin()
      admin_page = Admin_Page(logged_in_browser)
      admin_page.click_add_new_record()
      # select user role
      admin_page.select_user_role(USER_ROLE)
      # select user status
      admin_page.select_user_status(USER_STATUS)
      # fill employee name
      admin_page.fill_employee_name_for_hint(CANDIDATE_FN)
      autosuggestions = admin_page.explicitly_wait_and_visible_all_elements(MAX_WAIT_INTERVAL, admin_page.EMPLOYEE_HIDDEN_OPTION_1)
      WebDriverWait(logged_in_browser, 10).until(lambda driver: next((option for option in autosuggestions if option.text == (CANDIDATE_FN+' '+CANDIDATE_LN)), None)).click()
      # fill user name
      admin_page.create_user_name(USER_NAME)
      # fill user password
      admin_page.create_password(USER_PWD)
      # confirm password
      admin_page.confirm_password(USER_PWD)
      # click save
      admin_page.click_save_button()

   def test_search_user(self, logged_in_browser):
      admin_page = Admin_Page(logged_in_browser)
      # wait page to refresh and fill in employee name and click from autosuggestion
      time.sleep(5)
      admin_page.fill_employee_name_for_hint(CANDIDATE_FN)
      autosuggestions = admin_page.explicitly_wait_and_visible_all_elements(MAX_WAIT_INTERVAL, admin_page.EMPLOYEE_HIDDEN_OPTION_2)
      WebDriverWait(logged_in_browser, 10).until(lambda driver: next((option for option in autosuggestions if option.text == (CANDIDATE_FN+' '+CANDIDATE_LN)), None)).click()
      admin_page.click_save_button()

      user_name_label = admin_page.get_user_name()
      user_role_label = admin_page.get_user_role()
      employee_name_label = admin_page.get_employee_name()
      user_status_label = admin_page.get_user_status()
      assert user_name_label == USER_NAME
      assert user_role_label == USER_ROLE
      assert employee_name_label == (CANDIDATE_FN+' '+CANDIDATE_LN)
      assert user_status_label == USER_STATUS
   # end of test case 03
