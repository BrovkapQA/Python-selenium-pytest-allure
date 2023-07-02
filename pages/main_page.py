import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    SUCCESS_ALERT = (By.XPATH, '//div[@class="alert alert-primary"]')
    NAVIGATION_MENU = (By.XPATH, '//a[@class="nav-menu__link nav-menu__link--active"]')

    @allure.step("Get success authorization message")
    def successful_authorization(self):
        return self.get_text(self.SUCCESS_ALERT)
