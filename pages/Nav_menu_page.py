from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class NavMenuPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    #Locators

    # NAV_MENU = '//ul[@class="nav-menu__inner"]'
    PROFILE = (By.XPATH, '//ul[@class="nav-menu"]/li[1]')
    PERSONAL_ACCOUNT = (By.XPATH, '//a[@href="/dashboard"]')
    QUESTIONNAIRE = (By.XPATH, '//a[@href="/new-edit-profile"]')
    FAVORITES = (By.XPATH, '//a[@href="/bookmarks"]')
    SETTINGS = (By.XPATH, '//a[@href="/presets"]')

    MESSAGES = (By.XPATH, '//ul[@class="nav-menu"]/li[2]')   # and Notification locator
    MESSANGER = (By.XPATH, '//a[@href="/messenger"]')

    SESSIONS = (By.XPATH, '//ul[@class="nav-menu"]/li[3]')   # and Calendar locator
    SEANS_SUGGESTIONS = (By.XPATH, '//a[@href="/seance-suggestions"]')
    TECHNIQUES = (By.XPATH, '//a[@href="/techniques"]')
    NOTICE = (By.XPATH, '//a[@href="/cards"]')

    AKPP = (By.XPATH, '//ul[@class="nav-menu"]/li[4]')

    ASSOCIATION = (By.XPATH, '//ul[@class="nav-menu"]/li[5]')   # and Events locator
    CERTIFICATES = (By.XPATH, '//a[@href="/person/certificates"]')


    LEARNING = (By.XPATH, '//ul[@class="nav-menu"]/li[6]')     # and Courses locator
    SUPERVISION_WITHOUT_COURSE = (By.XPATH, '//a[@href="/supervision-without-course"]')
    PERSONAL_ACCOUNT_INDIVIDUAL_THERAPIES = (By.XPATH, '//a[@href="/study/therapy/client"]')
    INDIVIDUAL_SUPERVISION = (By.XPATH, '//a[@href="/study/individual-supervision"]')
    TECHNIQUES_AND_SKILLS = (By.XPATH, '//a[@href="/study/tas"]')
    TESTING = (By.XPATH, '//a[@href="/study/tests/list"]')
    INTERSVISION = (By.XPATH, '//a[@href="/study/tests/list"]')


    FINANCE = (By.XPATH, '//ul[@class="nav-menu"]/li[7]')


    def get_messanger(self):
        self.move_to_element(self.MESSAGES)
        self.click(self.MESSANGER)

    def get_notification(self):
        self.click(self.MESSAGES)

    def get_calendar(self):
        self.click(self.SESSIONS)

    def get_seans_suggestions(self):
        self.move_to_element(self.SESSIONS)
        self.click(self.SEANS_SUGGESTIONS)

    def get_techniques(self):
        self.move_to_element(self.SESSIONS)
        self.click(self.TECHNIQUES)

    def get_notice(self):
        self.move_to_element(self.SESSIONS)
        self.click(self.NOTICE)

    def get_akpp(self):
        self.move_to_element(self.AKPP)
        self.click(self.AKPP)

    def get_events(self):
        self.click(self.ASSOCIATION)

    def get_certificates(self):
        self.move_to_element(self.ASSOCIATION)
        self.click(self.CERTIFICATES)

    def get_courses(self):
        self.click(self.LEARNING)

    def get_supervision_without_courses(self):
        self.move_to_element(self.LEARNING)
        self.click(self.SUPERVISION_WITHOUT_COURSE)

    def get_personal_account_individual_therapies(self):
        self.move_to_element(self.LEARNING)
        self.click(self.PERSONAL_ACCOUNT_INDIVIDUAL_THERAPIES)

    def get_individual_supervision(self):
        self.move_to_element(self.LEARNING)
        self.click(self.INDIVIDUAL_SUPERVISION)

    def get_techniques_and_skills(self):
        self.move_to_element(self.LEARNING)
        self.click(self.TECHNIQUES_AND_SKILLS)

    def get_testing(self):
        self.move_to_element(self.LEARNING)
        self.click(self.TESTING)

    def get_intervision(self):
        self.move_to_element(self.LEARNING)
        self.click(self.INTERSVISION)

    def get_finance(self):
        self.click(self.FINANCE)



