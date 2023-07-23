import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TopNavMenu(BasePage):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    # Locators

    CHOOSE_PSYCHOLOGIST = (By.XPATH, '//a[@href="/matching"]')
    BLOG = (By.XPATH, '//a[@href="/blog"]')
    FREE_HELP = (By.XPATH, '//a[@href="/free-help"]')
    ALL_SPECIALISTS = (By.XPATH, '//a[@href="/new-persons-list"]')

    @allure.step("Go to the Choose_psychologists page")
    def get_choose_psychologist(self):
        self.click(self.CHOOSE_PSYCHOLOGIST)

    @allure.step("Go to the Blog page")
    def get_blog(self):
        self.click(self.BLOG)

    @allure.step("Go to the Free_help page")
    def get_free_help(self):
        self.click(self.FREE_HELP)

    @allure.step("Go to the All_specialists page")
    def get_all_specialists(self):
        self.click(self.ALL_SPECIALISTS)
