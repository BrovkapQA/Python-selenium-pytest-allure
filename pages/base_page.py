from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver



    def click(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, txt):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).send_keys(txt)

    def clear_text(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def get_text(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text
