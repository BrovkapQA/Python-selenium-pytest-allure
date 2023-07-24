from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FooterNavMenu(BasePage):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    # Locators

    BOTTOM_LOCATOR = '//a[contains(@class, "footer__list_item-link")]'
    MAIN_PAGE = (By.XPATH, f'{BOTTOM_LOCATOR}[@href="/home"]')
    SPECIALISTS_PAGE = (By.XPATH, f'{BOTTOM_LOCATOR}[@href="/new-persons-list"]')
    BLOG_PAGE = (By.XPATH, f'{BOTTOM_LOCATOR}[@href="/blog"]')
    PROFILE_PAGE = (By.XPATH, f'{BOTTOM_LOCATOR}[@href="/dashboard"]')
    HOW_WE_WORK_PAGE = (By.XPATH, f'{BOTTOM_LOCATOR}[@href="/how-we-work"]')
    FOR_SPECIALIST = (By.XPATH, f'{BOTTOM_LOCATOR}[@href="/for-specialist"]')
    FOR_CLIENT = (By.XPATH, f'{BOTTOM_LOCATOR}[@href="/for-client"]')
    CONTACT_US = (By.XPATH, f'{BOTTOM_LOCATOR}[@href="/contact-us"]')
    PAYMENT = (By.XPATH, f'{BOTTOM_LOCATOR}[@href="/payment-methods"]')
    FAQ = (By.XPATH, f'{BOTTOM_LOCATOR}[@href="/faq"]')
    BUSINESS = (By.XPATH, f'{BOTTOM_LOCATOR}[@href="/business-page"]')
    FREE_HELP = (By.XPATH, f'{BOTTOM_LOCATOR}[@href="/free-help"]')
    VK = (By.XPATH, '//a[@class="social__link social-vk footer__soc_link"]')
    TELEGRAM = (By.XPATH, '//a[@class="social__link social-yt footer__soc_link"]')

    def go_to_the_main_page(self):
        self.scroll_to_bottom()
        self.click(self.MAIN_PAGE)

    def go_to_the_specialists_page(self):
        self.scroll_to_bottom()
        self.click(self.SPECIALISTS_PAGE)

    def go_to_the_blog_page(self):
        self.scroll_to_bottom()
        self.click(self.BLOG_PAGE)

    def go_to_the_profile_page(self):
        self.scroll_to_bottom()
        self.click(self.PROFILE_PAGE)

    def go_to_the_how_we_work_page(self):
        self.scroll_to_bottom()
        self.click(self.HOW_WE_WORK_PAGE)

    def go_to_the_for_specialist_page(self):
        self.scroll_to_bottom()
        self.click(self.FOR_SPECIALIST)

    def go_to_the_for_client_page(self):
        self.scroll_to_bottom()
        self.click(self.FOR_CLIENT)

    def go_to_the_contact_us_page(self):
        self.scroll_to_bottom()
        self.click(self.CONTACT_US)

    def go_to_the_payment_page(self):
        self.scroll_to_bottom()
        self.click(self.PAYMENT)

    def go_to_the_faq_page(self):
        self.scroll_to_bottom()
        self.click(self.FAQ)

    def go_to_the_business_page(self):
        self.scroll_to_bottom()
        self.click(self.BUSINESS)

    def go_to_the_free_help_page(self):
        self.scroll_to_bottom()
        self.click(self.FREE_HELP)

    def go_to_the_vk(self):
        self.scroll_to_bottom()
        self.click(self.VK)

    def go_to_the_telegram(self):
        self.scroll_to_bottom()
        self.click(self.TELEGRAM)


