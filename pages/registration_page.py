import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    FIRSTNAME = (By.XPATH, "//input[@id='firstname']")
    LASTNAME = (By.XPATH, "//input[@id='lastname']")
    MIDDLENAME = (By.XPATH, "//input[@id='middlename']")
    REGISTRATION_EMAIL = (By.XPATH, "//input[@id='email']")
    REGISTRATION_PASSWORD = (By.XPATH, "//input[@id='password']")
    CONFIRM_BUTTON = (By.XPATH, "//button[@class='new-registration__btn']")
    CALENDAR = (By.XPATH, "//input[@id='birthDay']")
    YEAR = (By.XPATH, "//input[@class='numInput cur-year']")
    MONTH = (By.XPATH, "//select[@class='flatpickr-monthDropdown-months']")



    @allure.step("Create a new user")
    def create_user(self, user_firstname, user_lastname, user_middlename, user_email, password, year, month):
        self.send_keys(self.FIRSTNAME, user_firstname)
        self.send_keys(self.LASTNAME, user_lastname)
        self.send_keys(self.MIDDLENAME, user_middlename)
        self.send_keys(self.REGISTRATION_EMAIL, user_email)
        self.send_keys(self.REGISTRATION_PASSWORD, password)
        self.click(self.CALENDAR)
        self.clear_text(self.YEAR)
        self.send_keys(self.YEAR, year)
        self.select_month(self.MONTH, month)
        self.click(self.FIRSTNAME)
        self.click(self.CONFIRM_BUTTON)
