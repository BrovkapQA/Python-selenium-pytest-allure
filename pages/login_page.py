from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)


    #Locators

    LOGO = (By.XPATH, "//div[@class='logo__text']")
    EMAIL = (By.XPATH, "//input[@id='email']")
    PASSWORD = (By.XPATH, "//input[@id='password-field']")
    SUBMIT = (By.XPATH, "//input[@id='submit']")
    CHECKBOX = (By.XPATH, "//span[@class= 'check__box check__box_new']")
    SPECIALIST_BUTTON = (By.XPATH, "(//a[@class='btn btn-outline login-form__registration'])[2]")
    BASIC_USER_BUTTON = (By.XPATH, "(//a[@class='btn btn-outline login-form__registration'])[1]")
    LOGIN_ERROR = (By.XPATH, "//div[@class='alert alert-primary']")
    ERROR_FILD = (By.XPATH, "//span[@class='flush-form']")


    def login(self, login_email, login_password):
        self.send_keys(self.EMAIL, login_email)
        self.send_keys(self.PASSWORD, login_password)
        self.click(self.SUBMIT)

    def get_login_error(self):
        return self.get_text(self.LOGIN_ERROR)

    def get_error_fild(self):
        return self.get_text(self.ERROR_FILD)

    def get_registration(self):
        return self.click(self.SPECIALIST_BUTTON)


