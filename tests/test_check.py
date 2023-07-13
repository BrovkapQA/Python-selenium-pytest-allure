import time

import pytest

from pages.Nav_menu_page import NavMenuPage
from pages.login_page import LoginPage



@pytest.mark.usefixtures("setup_and_teardown")
class TestCheck:

    def test_check_calendar(self):
        login_page = LoginPage(self.driver)
        nav_menu_page = NavMenuPage(self.driver)

        login_page.login("", "")
        nav_menu_page.get_messanger()
        nav_menu_page.get_notification()
        nav_menu_page.get_calendar()
        nav_menu_page.get_seans_suggestions()
        nav_menu_page.get_techniques()
        nav_menu_page.get_notice()
        nav_menu_page.get_akpp()
        nav_menu_page.get_events()
        nav_menu_page.get_certificates()
        nav_menu_page.get_courses()
        nav_menu_page.get_supervision_without_courses()
        nav_menu_page.get_personal_account_individual_therapies()
        nav_menu_page.get_individual_supervision()
        nav_menu_page.get_techniques_and_skills()
        nav_menu_page.get_testing()
        nav_menu_page.get_intervision()
        nav_menu_page.get_finance()
        time.sleep(5)




