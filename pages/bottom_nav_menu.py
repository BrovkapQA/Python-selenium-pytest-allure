from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BottomNavMenu(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    MAIN_PAGE = (By.XPATH, '//a[contains(@class, "personal-footer__list_item-link")][@href="/home"]')
    SPECIALISTS_PAGE = (By.XPATH, '//a[@class="footer__list_item-link" and href="/new-persons-list"]')
    BLOG_PAGE = (By.XPATH, '//a[@class="footer__list_item-link" and href="/blog"]')
    PROFILE_PAGE = (By.XPATH, '//a[@class="footer__list_item-link" and href="/dashboard"]')
    HOW_WE_WORK_PAGE = (By.XPATH, '//a[@class="footer__list_item-link" and href="/how-we-work"]')
    FOR_SPECIALIST = (By.XPATH, '//a[@class="footer__list_item-link" and href="/for-specialist"]')
    FOR_CLIENT = (By.XPATH, '//a[@class="footer__list_item-link" and href="/for-client"]')
    CONTACT_US = (By.XPATH, '//a[@class="footer__list_item-link" and href="/contact-us"]')
    PAYMENT = (By.XPATH, '//a[@class="footer__list_item-link" and href="/payment-methods"]')
    FAQ = (By.XPATH, '//a[@class="footer__list_item-link" and href="/faq"]')
    BUSINESS = (By.XPATH, '//a[@class="footer__list_item-link" and href="/business-page"]')
    FREE_HELP = (By.XPATH, '//a[@class="footer__list_item-link" and href="/free-help"]')
    VK = (By.XPATH, '//a[@class="social__link social-vk footer__soc_link"]')
    TELEGRAM = (By.XPATH, '//a[@class="social__link social-yt footer__soc_link"]')

    def get_main_page(self):
        self.scroll_to_bottom()
        self.click(self.MAIN_PAGE)

    def get_specialists_page(self):
        self.scroll_to_bottom()
        self.click(self.SPECIALISTS_PAGE)

    def get_blog_page(self):
        self.scroll_to_bottom()
        self.click(self.BLOG_PAGE)

    def get_profile_page(self):
        self.scroll_to_bottom()
        self.click(self.PROFILE_PAGE)

    def get_how_we_work_page(self):
        self.scroll_to_bottom()
        self.click(self.HOW_WE_WORK_PAGE)


