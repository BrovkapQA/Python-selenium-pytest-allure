import time

import pytest

from pages.Nav_menu_page import NavMenuPage
from pages.calendar_page import CalendarPage
from pages.login_page import LoginPage
from utilities import ExcelUtilities


@pytest.mark.usefixtures("setup_and_teardown")
class TestCreateSeanse:

    @pytest.mark.parametrize("email_address, password",
                                  ExcelUtilities.get_data_from_excel("ExcelData/UserData.xlsx", "CreateSession"))
    def test_create_session_valid_date(self, email_address, password, date):
        login_page = LoginPage(self.driver)
        nav_menu_page = NavMenuPage(self.driver)
        calendar_page = CalendarPage(self.driver)

        login_page.login(email_address, password)
        nav_menu_page.get_calendar()
        calendar_page.create_session(date)



