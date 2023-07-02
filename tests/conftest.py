import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://becbt.online/login")
    driver.maximize_window()

    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def login_page(driver):
    wait = WebDriverWait(driver, 10)
    return LoginPage(driver, wait)


@pytest.fixture(scope="function")
def main_page(driver):
    wait = WebDriverWait(driver, 10)
    return MainPage(driver, wait)

@pytest.fixture(scope="function")
def registration_page(driver):
    wait = WebDriverWait(driver, 10)
    return RegistrationPage(driver, wait)