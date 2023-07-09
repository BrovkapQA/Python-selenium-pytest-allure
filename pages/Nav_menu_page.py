from pages.base_page import BasePage


class NavMenuPage(BasePage):

    def __init__(self):
        super().__init__(self.driver)

    #Locators

    NAV_MENU = '//ul[@class="nav-menu__inner"]'
    PROFILE = f'{NAV_MENU}/li[contains(@class, "nav-menu__inner-link--active")]'
    PERSONAL_ACCOUNT = f'{NAV_MENU}/li[1]'
    QUESTIONNAIRE = f'{NAV_MENU}/li[2]'
    FAVORITES = f'{NAV_MENU}/li[3]'
    SETTINGS = f'{NAV_MENU}/li[4]'