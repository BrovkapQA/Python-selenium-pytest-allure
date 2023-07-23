import time

import pytest

from tests.test_base import BaseTest
from utilities.excel_utilities import ExcelReader


class TestBottomNavMenu(BaseTest):

    @pytest.mark.parametrize("email_address, password", ExcelReader("data.xlsx").get_data_from_excel("ValidLogin"))
    def test_check_calendar(self, email_address, password):
        self.login_page.login(email_address, password)
        self.bottom_nav_menu.go_to_the_main_page()
        self.bottom_nav_menu.go_to_the_blog_page()
        self.bottom_nav_menu.go_to_the_faq_page()
        self.bottom_nav_menu.go_to_the_payment_page()
        self.bottom_nav_menu.go_to_the_profile_page()
        self.bottom_nav_menu.go_to_the_specialists_page()
        self.bottom_nav_menu.go_to_the_how_we_work_page()
        self.bottom_nav_menu.go_to_the_contact_us_page()
        self.bottom_nav_menu.go_to_the_for_client_page()
        self.bottom_nav_menu.go_to_the_business_page()
        self.bottom_nav_menu.go_to_the_free_help_page()
        self.bottom_nav_menu.go_to_the_vk()



