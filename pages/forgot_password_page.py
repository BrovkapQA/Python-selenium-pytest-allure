from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    # Locators

    FILD_EMAIL = (By.XPATH, '//input[@class="input-form__input"]')
    CONFIRM_BUTTON = (By.XPATH, '//input[@id="submit"]')
    SUCCESS_MESSAGE = (By.XPATH, '//div[@id="submit"]')
    INVALID_EMAIL_MESSAGE = (By.XPATH, '//span[@class="flush-form"')
    NOT_REGISTERED_USER_MESSAGE = (By.XPATH, '//div[@class="alert alert-primary"]')

    def send_password_reset_link(self, email):
        self.send_keys(self.FILD_EMAIL, email)
        self.click(self.CONFIRM_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)

    def get_invalid_email_message(self):
        return self.get_text(self.INVALID_EMAIL_MESSAGE)

    def get_not_registered_user_message(self):
        return self.get_text(self.NOT_REGISTERED_USER_MESSAGE)