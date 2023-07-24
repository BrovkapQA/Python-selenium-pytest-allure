import pytest
import os
import json
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from globals import dir_global
from pages.nav_menu.footer_nav_menu import FooterNavMenu
from pages.nav_menu.main_nav_menu import MainNavMenu
from pages.akpp_page import AkppPage
from pages.calendar_page import CalendarPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage
from utilities import configuration_utilities


@pytest.fixture(scope="session")
def json_data() -> dict:
    json_path = os.path.join(dir_global.DATA_FILES_PATH, "test_data.json")
    with open(json_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


def pytest_runtest_setup(item):
    global driver
    browser = configuration_utilities.read_configuration("basic info", "browser")
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Provide a valid browser name from this list chrome/firefox/edge")

    print("Running test:", item.name)
    driver.maximize_window()
    base_url = configuration_utilities.read_configuration("basic info", "url")
    driver.get(base_url)
    item.cls.driver = driver
    wait = WebDriverWait(driver, 10)
    item.cls.wait = wait
    item.cls.login_page = LoginPage(driver, wait)
    item.cls.main_page = MainPage(driver, wait)
    item.cls.main_nav_menu = MainNavMenu(driver, wait)
    item.cls.calendar_page = CalendarPage(driver, wait)
    item.cls.forgot_password_page = ForgotPasswordPage(driver, wait)
    item.cls.registration_page = RegistrationPage(driver, wait)
    item.cls.akpp_page = AkppPage(driver, wait)
    item.cls.footer_nav_menu = FooterNavMenu(driver, wait)


def pytest_runtest_teardown():
    driver.quit()
