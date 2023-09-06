
from test_units import *
from utilities.constants import USERNAME, LOG_IN_URL, PASSWORD, INDEX_URL
from utilities.page_objects.log_in_page import Log_In_Page



class Test_01_Log_in:

    # Test log in:
    def test_log_in(self, driver):
        log_in_page = Log_In_Page(driver)
        log_in_page.navigate_to(LOG_IN_URL)
        log_in_page.fill_user_name(USERNAME)
        log_in_page.fill_password(PASSWORD)
        log_in_page.click_submit_button()
        assert log_in_page.get_current_url() == INDEX_URL, "Login test passed"


