# import pytest
# from tests.test_base import BaseTest
# from utilities import ExcelUtilities
#
#
# class TestCreateSession(BaseTest):
#
#     @pytest.mark.parametrize("email_address, password, date, st_hour, st_minutes, end_hour, end_minutes",
#                              ExcelUtilities.get_data_from_excel("configurations/data.xlsx", "CreateSessionValidDate"))
#     def test_create_session_valid_date(self, email_address, password, date, st_hour, st_minutes, end_hour, end_minutes):
#         self.login_page.login(email_address, password)
#         self.nav_menu_page.get_calendar()
#         self.calendar_page.create_individual_session(date, st_hour, st_minutes, end_hour, end_minutes)
