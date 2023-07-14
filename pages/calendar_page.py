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
    CALENDAR_FIELD = (By.XPATH, '//input[@class="flatpickr dropdown-btn dropdown-input datepicker flatpickr-input active superMegaCalendar_date"]')
    HEADER_FIELD = (By.XPATH, '//div[@class="superMegaCalendar_popup-header"]')
    def create_session(self, date):
        self.click(self.SESSION_BUTTON)
        self.click(self.ALERT_TYPE_SESSION_FILD)
        self.click(self.INDIVIDUAL_SESSION)
        self.chose_date(self.CALENDAR_FIELD, date)
        self.click(self.HEADER_FIELD)




