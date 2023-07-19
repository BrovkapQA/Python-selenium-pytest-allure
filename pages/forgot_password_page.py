import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    FILD_EMAIL = (By.XPATH, '//input[@class="input-form__input"]')
    CONFIRM_BUTTON = (By.XPATH, '//input[@id="submit"]')
    SUCCESS_MESSAGE = (By.XPATH, '//div[@class="alert alert-primary"]')
    INVALID_EMAIL_MESSAGE = (By.XPATH, '//span[@class="flush-form"]')
    NOT_REGISTERED_USER_MESSAGE = (By.XPATH, '//div[@class="alert alert-primary"]')

    @allure.step("Sending a link to restore the password")
    def send_password_reset_link(self, email):
        with allure.step("send email for restore the password"):
            self.send_keys(self.FILD_EMAIL, email)
            with allure.step("Confirm sending"):
                self.click(self.CONFIRM_BUTTON)

    @allure.step("Get message about successful password reset")
    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)

    @allure.step("Get message about a non-correct email")
    def get_invalid_email_message(self):
        return self.get_text(self.INVALID_EMAIL_MESSAGE)

    @allure.step("Get message about an unregistered email")
    def get_not_registered_user_message(self):
        return self.get_text(self.NOT_REGISTERED_USER_MESSAGE)