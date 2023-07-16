from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AkppPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    POPUP_CLOSE = (By.XPATH, '//button[@class="btn btn-second btn-second-middle"]')
    GO_TO_PROFILE = (By.XPATH, '//span[@class="btn-text"]')
    MEMBERSHIP_AKPP = (By.XPATH, '//h3[text()="Членство АКПП"]')

    def go_to_profile(self):
        self.click(self.GO_TO_PROFILE)

    def close_popup(self):
        self.click(self.POPUP_CLOSE)

    def get_text_akkp(self):
        return self.get_text(self.MEMBERSHIP_AKPP)
