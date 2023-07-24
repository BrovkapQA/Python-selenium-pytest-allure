import pytest
from tests.test_base import BaseTest
from utilities.excel_utilities import ExcelReader


class TestCreateSession(BaseTest):

    @pytest.mark.parametrize("email_address, password, date, st_hour, st_minutes, end_hour, end_minutes",
                             ExcelReader("data.xlsx").get_data_from_excel("CreateSessionValidDate"))
    def test_create_session_valid_date(self, email_address, password, date, st_hour, st_minutes, end_hour, end_minutes):
        self.login_page.login(email_address, password)
        self.main_nav_menu.get_calendar()
        self.calendar_page.create_individual_session(date, st_hour, st_minutes, end_hour, end_minutes)
