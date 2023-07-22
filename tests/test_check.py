import pytest
from tests.test_base import BaseTest
from utilities.excel_utilities import ExcelReader


class TestCheck(BaseTest):

    @pytest.mark.parametrize("email_address, password", ExcelReader("data.xlsx").get_data_from_excel("ValidLogin"))
    def test_check_calendar(self, email_address, password):
        self.login_page.login(email_address, password)
        self.nav_menu_page.get_akpp()
        self.akpp_page.go_to_profile()
        assert "Членство АКПП" == self.akpp_page.get_text_akkp()
