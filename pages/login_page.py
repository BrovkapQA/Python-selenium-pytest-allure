from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    LOGO = (By.XPATH, "//div[@class='logo__text']")
    EMAIL = (By.XPATH, "//input[@id='email']")
    PASSWORD = (By.XPATH, "//input[@id='password-field']")
    SUBMIT = (By.XPATH, "//input[@id='submit']")
    CHECKBOX = (By.XPATH, "//span[@class= 'check__box check__box_new']")
    SPECIALIST_BUTTON = (By.XPATH, "(//a[@class='btn btn-outline login-form__registration'])[2]")
    BASIC_USER_BUTTON = (By.XPATH, "(//a[@class='btn btn-outline login-form__registration'])[1]")
    LOGIN_ERROR = (By.XPATH, "//div[@class='alert alert-primary']")
    ERROR_FILD = (By.XPATH, "//span[@class='flush-form']")
    FORGOT_PASSWORD = (By.XPATH, '//a[@class="login-screen__bottom-link"]')

    @allure.step("Log in with username and password")
    def login(self, login_email, login_password):
        with allure.step("Send login email"):
            self.send_keys(self.EMAIL, login_email)
            with allure.step("Send login password"):
                self.send_keys(self.PASSWORD, login_password)
                self.click(self.SUBMIT)

    @allure.step("Get authorization error message")
    def get_login_error(self):
        return self.get_text(self.LOGIN_ERROR)

    @allure.step("Get fild error message")
    def get_error_fild(self):
        return self.get_text(self.ERROR_FILD)

    @allure.step("Go to the registration page")
    def get_registration(self):
        return self.click(self.SPECIALIST_BUTTON)

    @allure.step("Go to the forgot_password page")
    def click_forgot_password(self):
        return self.click(self.FORGOT_PASSWORD)
