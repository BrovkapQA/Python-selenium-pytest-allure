from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, txt):
        return self.wait.until(EC.element_to_be_clickable(locator)).send_keys(txt)

    def clear_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).clear()

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def move_to_element(self, locator):
        action = ActionChains(self.driver)
        self.wait.until(EC.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        action.move_to_element(element).perform()

    def switch_to_alert(self):
        return self.driver.switch_to.alert

    def chose_date(self, locator, date):
        datepicker_input = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].removeAttribute('readonly', '')", datepicker_input)
        datepicker_input.clear()
        date_str = date.strftime('%d.%m.%Y')
        datepicker_input.send_keys(date_str)

    def scroll_to_view_element(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
