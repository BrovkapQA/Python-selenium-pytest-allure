from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait


    def click(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, txt):
        return self.wait.until(EC.element_to_be_clickable(locator)).send_keys(txt)

    def clear_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    # def go_to_element(self, element):
    #     return self.driver.execute_script("argument[0].scrollIntoView({ behavior: 'smooth', block: 'center' });",
    #                                       element)
    #


