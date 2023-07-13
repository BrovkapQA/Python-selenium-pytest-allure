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

    MESSAGES = (By.XPATH, '//ul[@class="nav-menu"]/li[2]')
    NOTIFICATION = (By.XPATH, '//a[@href="/dialogs"][2]')
    MESSANGER = (By.XPATH, '//a[@href="/messenger"]')

    SESSIONS = (By.XPATH, '//ul[@class="nav-menu"]/li[3]')
    CALENDAR = (By.XPATH, '//a[@href="/new-calendar"]')
    SEANS_SUGGESTIONS = (By.XPATH, '//a[@href="/seance-suggestions"]')
    TECHNIQUES = (By.XPATH, '//a[@href="/techniques"]')
    NOTICE = (By.XPATH, '//a[@href="/cards"]')

    AKPP = (By.XPATH, '//ul[@class="nav-menu"]/li[4]')

    ASSOCIATION = (By.XPATH, '//ul[@class="nav-menu"]/li[5]')

    LEARNING = (By.XPATH, '(//ul[@class="nav-menu"]/li[6]')


    FINANCE = (By.XPATH, '//ul[@class="nav-menu"]/li[7]')


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



