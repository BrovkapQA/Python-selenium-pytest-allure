from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class NavMenuPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    #Locators

    # NAV_MENU = '//ul[@class="nav-menu__inner"]'
    PROFILE = (By.XPATH, '//a[@href="/dashboard"]')
    PERSONAL_ACCOUNT = (By.XPATH, '//a[@href="/dashboard"]')
    QUESTIONNAIRE = (By.XPATH, '//a[@href="/new-edit-profile"]')
    FAVORITES = (By.XPATH, '//a[@href="/bookmarks"]')
    SETTINGS = (By.XPATH, '//a[@href="/presets"]')

    MESSAGES = (By.XPATH, '(//li[@class="nav-menu__list nav-menu__list--absolute"])[1]')
    NOTIFICATION = (By.XPATH, '//a[href="/dialogs"]')
    MESSANGER = (By.XPATH, '//a[@href="/messenger"]')

    SESSIONS = (By.XPATH, '(//li[@class="nav-menu__list nav-menu__list--absolute"])[2]')
    CALENDAR = (By.XPATH, '//li[@href="/new-calendar"]')
    SEANS_SUGGESTIONS = (By.XPATH, '//li[@href="/seance-suggestions"]')
    TECHNIQUES = (By.XPATH, '//li[@href="/techniques"]')
    NOTICE = (By.XPATH, '//li[@href="/cards"]')

    AKPP = (By.XPATH, '(//li[@class="nav-menu__list nav-menu__list--absolute"])[3]')

    ASSOCIATION = (By.XPATH, '(//li[@class="nav-menu__list nav-menu__list--absolute"])[4]')

    LEARNING = (By.XPATH, '(//li[@class="nav-menu__list nav-menu__list--absolute"])[5]')


    FINANCE = (By.XPATH, '(//li[@class="nav-menu__list nav-menu__list--absolute"])[6]')


    def get_messanger(self):
        self.move_to_element(self.MESSAGES)
        self.click(self.MESSANGER)

    def get_notification(self):
        self.move_to_element(self.MESSAGES)
        self.click(self.NOTIFICATION)

    def get_calendar(self):
        self.move_to_element(self.SESSIONS)
        self.click(self.CALENDAR)

    def get_seans_suggestions(self):
        self.move_to_element(self.SESSIONS)
        self.click(self.SEANS_SUGGESTIONS)

    def get_techniques(self):
        self.move_to_element(self.SESSIONS)
        self.click(self.TECHNIQUES)

    def get_notice(self):
        self.move_to_element(self.SESSIONS)
        self.click(self.NOTICE)



