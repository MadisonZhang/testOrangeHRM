import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def driver():
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()

@pytest.fixture(scope="session")
def url():
    return "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
@pytest.fixture(scope="session")
def logged_in_browser(driver, url):
    driver.get(url)
    yield driver

