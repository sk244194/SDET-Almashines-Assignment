import pytest
from selenium import webdriver

# Can only name the conftest.py otherwise pytest would not be able to find it

# Fixtures are used to automate setup and teardown phases for testing
# setup -> like opening website inputting details and so on..
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.almashines.com/dtc/account")
    yield driver
    driver.quit()