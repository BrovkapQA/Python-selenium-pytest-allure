import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CalendarPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    SESSION_BUTTON = (By.XPATH, '//span[@class="btn-text"]')
    ALERT_TYPE_SESSION_FILD = (By.XPATH, '//div[@class="superMegaCalendar_popup-type"]')
    INDIVIDUAL_SESSION = (By.XPATH, "//button[text()='Индивидуальный сеанс']")
    GROUP_SESSION = (By.XPATH, "//button[text()='Групповой сеанс']")
    SOCIAL_SESSION = (By.XPATH, "//button[text()='Социальный сеанс']")
    LECTURE_SESSION = (By.XPATH, "//button[text()='Лекция']")
    CALENDAR_FIELD = (By.XPATH,
                      '//input[@class="flatpickr dropdown-btn dropdown-input datepicker flatpickr-input active superMegaCalendar_date"]')
    HEADER_FIELD = (By.XPATH, '//div[@class="superMegaCalendar_popup-header"]')
    CONFIRM_BUTTON = (By.XPATH, '//button[@class="superMegaCalendar_popup-btn"]')
    START_SESSION_HOURS = (By.XPATH, "(//div[@time='hour']/input)[1]")
    START_SESSION_MINUTES = (By.XPATH, "(//div[@time='minute']/input)[1]")
    FINISH_SESSION_HOURS = (By.XPATH, "(//div[@time='hour']/input)[2]")
    FINISH_SESSION_MINUTES = (By.XPATH, "(//div[@time='minute']/input)[2]")
    ACTIVE_LIST = '//ul[@class="superMegaCalendar_popup-list superMegaCalendar_popup-list--active"]/li'

    def select_time(self, value):
        chose_time = f"/button[text()={value:02}]"
        xpath_expression = (By.XPATH, f"{self.ACTIVE_LIST}{chose_time}")
        print(xpath_expression)
        self.click(xpath_expression)

    @allure.step("Create a new session")
    def create_session(self, date, st_hour, st_minutes, end_hour, end_minutes):
        with allure.step("Click button 'create session'"):
            self.click(self.SESSION_BUTTON)
            with allure.step("Click fild type_session"):
                self.click(self.ALERT_TYPE_SESSION_FILD)
                with allure.step("Chose individual session"):
                    self.click(self.INDIVIDUAL_SESSION)
                    with allure.step("Chose date of session"):
                        self.chose_date(self.CALENDAR_FIELD, date)
                        self.click(self.HEADER_FIELD)
                        with allure.step("Choosing the start and end time of the session"):
                            self.click(self.START_SESSION_HOURS)
                            self.select_time(st_hour)
                            self.click(self.START_SESSION_MINUTES)
                            self.select_time(st_minutes)
                            self.click(self.FINISH_SESSION_HOURS)
                            self.select_time(end_hour)
                            self.click(self.FINISH_SESSION_MINUTES)
                            self.select_time(end_minutes)
                            self.click(self.CONFIRM_BUTTON)
