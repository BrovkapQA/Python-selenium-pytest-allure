import time

import pytest

from pages.Nav_menu_page import NavMenuPage
from pages.login_page import LoginPage



@pytest.mark.usefixtures("setup_and_teardown")
class TestCheck:

    def test_check_calendar(self):
        login_page = LoginPage(self.driver)
        nav_menu_page = NavMenuPage(self.driver)

        login_page.login("Visoveny@gmail.com", "Asd123df")
        nav_menu_page.get_messanger()
        nav_menu_page.get_calendar()



