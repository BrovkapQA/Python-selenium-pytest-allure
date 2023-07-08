import pytest
from selenium import webdriver
from utilities import ReadConfiguration


@pytest.fixture(scope="function")
def setup_and_teardown(request):
    browser = ReadConfiguration.read_configuration("basic info", "browser")
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Provide a valid browser name from this list chrome/firefox/edge")

    driver.maximize_window()
    base_url = ReadConfiguration.read_configuration("basic info", "url")
    driver.get(base_url)
    request.cls.driver = driver
    yield
    driver.quit()



