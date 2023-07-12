from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver



    def click(self, locator):
        return Wait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def send_keys(self, locator, txt):
        return Wait(self.driver, 10).until(EC.element_to_be_clickable(locator)).send_keys(txt)

    def clear_text(self, locator):
        return Wait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def get_text(self, locator):
        return Wait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text

    def move_to_element(self, locator):
        action = ActionChains(self.driver)
        Wait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        action.move_to_element(element).perform()

    def select_month(self, locator, month):
        dropdown = Select(Wait(self.driver, 10).until(EC.visibility_of_element_located(locator)))
        return dropdown.select_by_visible_text(month)



