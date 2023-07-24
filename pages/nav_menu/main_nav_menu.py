import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainNavMenu(BasePage):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    # Locators

    # NAV_MENU = '//ul[@class="nav-menu__inner"]'
    PROFILE = (By.XPATH, '//ul[@class="nav-menu"]/li[1]')
    PERSONAL_ACCOUNT = (By.XPATH, '//a[@href="/dashboard"]')
    QUESTIONNAIRE = (By.XPATH, '//a[@href="/new-edit-profile"]')
    FAVORITES = (By.XPATH, '//a[@href="/bookmarks"]')
    SETTINGS = (By.XPATH, '//a[@href="/presets"]')
    MESSAGES = (By.XPATH, '//ul[@class="nav-menu"]/li[2]')  # and Notification locator
    MESSANGER = (By.XPATH, '//a[@href="/messenger"]')
    SESSIONS = (By.XPATH, '//ul[@class="nav-menu"]/li[3]')  # and Calendar locator
    SESSION_SUGGESTIONS = (By.XPATH, '//a[@href="/seance-suggestions"]')
    TECHNIQUES = (By.XPATH, '//a[@href="/techniques"]')
    NOTICE = (By.XPATH, '//a[@href="/cards"]')
    AKPP = (By.XPATH, '//ul[@class="nav-menu"]/li[4]')
    ASSOCIATION = (By.XPATH, '//ul[@class="nav-menu"]/li[5]')  # and Events locator
    CERTIFICATES = (By.XPATH, '//a[@href="/person/certificates"]')
    LEARNING = (By.XPATH, '//ul[@class="nav-menu"]/li[6]')  # and Courses locator
    SUPERVISION_WITHOUT_COURSE = (By.XPATH, '//a[@href="/supervision-without-course"]')
    PERSONAL_ACCOUNT_INDIVIDUAL_THERAPIES = (By.XPATH, '//a[@href="/study/therapy/client"]')
    INDIVIDUAL_SUPERVISION = (By.XPATH, '//a[@href="/study/individual-supervision"]')
    TECHNIQUES_AND_SKILLS = (By.XPATH, '//a[@href="/study/tas"]')
    TESTING = (By.XPATH, '//a[@href="/study/tests/list"]')
    INTERSVISION = (By.XPATH, '//a[@href="/study/tests/list"]')
    FINANCE = (By.XPATH, '//ul[@class="nav-menu"]/li[7]')

    @allure.step("Go to the messanger page")
    def get_messanger(self):
        self.move_to_element(self.MESSAGES)
        self.click(self.MESSANGER)

    @allure.step("Go to the notification page")
    def get_notification(self):
        self.click(self.MESSAGES)

    @allure.step("Go to the calendar page")
    def get_calendar(self):
        self.click(self.SESSIONS)

    @allure.step("Go to the session_suggestions page")
    def get_session_suggestions(self):
        self.move_to_element(self.SESSIONS)
        self.click(self.SESSION_SUGGESTIONS)

    @allure.step("Go to the techniques page")
    def get_techniques(self):
        self.move_to_element(self.SESSIONS)
        self.click(self.TECHNIQUES)

    @allure.step("Go to the notice page")
    def get_notice(self):
        self.move_to_element(self.SESSIONS)
        self.click(self.NOTICE)

    @allure.step("Go to the akpp page")
    def get_akpp(self):
        self.move_to_element(self.AKPP)
        self.click(self.AKPP)

    @allure.step("Go to the events page")
    def get_events(self):
        self.click(self.ASSOCIATION)

    @allure.step("Go to the certificates page")
    def get_certificates(self):
        self.move_to_element(self.ASSOCIATION)
        self.click(self.CERTIFICATES)

    @allure.step("Go to the courses page")
    def get_courses(self):
        self.click(self.LEARNING)

    @allure.step("Go to the supervision_without_courses page")
    def get_supervision_without_courses(self):
        self.move_to_element(self.LEARNING)
        self.click(self.SUPERVISION_WITHOUT_COURSE)

    @allure.step("Go to the personal_account_individual_therapies page")
    def get_personal_account_individual_therapies(self):
        self.move_to_element(self.LEARNING)
        self.click(self.PERSONAL_ACCOUNT_INDIVIDUAL_THERAPIES)

    @allure.step("Go to the individual_supervision page")
    def get_individual_supervision(self):
        self.move_to_element(self.LEARNING)
        self.click(self.INDIVIDUAL_SUPERVISION)

    @allure.step("Go to the techniques_and_skills page")
    def get_techniques_and_skills(self):
        self.move_to_element(self.LEARNING)
        self.click(self.TECHNIQUES_AND_SKILLS)

    @allure.step("Go to the testing page")
    def get_testing(self):
        self.move_to_element(self.LEARNING)
        self.click(self.TESTING)

    @allure.step("Go to the intervision page")
    def get_intervision(self):
        self.move_to_element(self.LEARNING)
        self.click(self.INTERSVISION)

    @allure.step("Go to the finance page")
    def get_finance(self):
        self.click(self.FINANCE)
