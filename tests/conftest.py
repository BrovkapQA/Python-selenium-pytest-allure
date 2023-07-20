import pytest
from selenium import webdriver

from pages.Nav_menu_page import NavMenuPage
from pages.akpp_page import AkppPage
from pages.calendar_page import CalendarPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage
from utilities import ReadConfiguration


def pytest_runtest_setup(item):
    global driver
    browser = ReadConfiguration.read_configuration("basic info", "browser")
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
    item.cls.driver = driver
    item.cls.login_page = LoginPage(driver)
    item.cls.main_page = MainPage(driver)
    item.cls.nav_menu_page = NavMenuPage(driver)
    item.cls.calendar_page = CalendarPage(driver)
    item.cls.forgot_password_page = ForgotPasswordPage(driver)
    item.cls.registration_page = RegistrationPage(driver)
    item.cls.akpp_page = AkppPage(driver)


def pytest_runtest_teardown():
    driver.quit()
