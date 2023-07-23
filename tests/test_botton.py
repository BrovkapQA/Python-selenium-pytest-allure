import time

import pytest

from tests.test_base import BaseTest
from utilities.excel_utilities import ExcelReader


class TestBottomNavMenu(BaseTest):

    @pytest.mark.parametrize("email_address, password", ExcelReader("data.xlsx").get_data_from_excel("ValidLogin"))
    def test_check_calendar(self, email_address, password):
        self.login_page.login(email_address, password)
        self.bottom_nav_menu.get_main_page()

