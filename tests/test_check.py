# import time
#
# import pytest
#
# from pages.Nav_menu_page import NavMenuPage
# from pages.akpp_page import AkppPage
# from pages.login_page import LoginPage
# from utilities import ExcelUtilities
#
#
# @pytest.mark.usefixtures("setup_and_teardown")
# class TestCheck:
#
#     @pytest.mark.parametrize("email_address, password",
#                              ExcelUtilities.get_data_from_excel("ExcelData/UserData.xlsx", "ValidLogin"))
#     def test_check_calendar(self, email_address, password):
#         login_page = LoginPage(self.driver)
#         nav_menu_page = NavMenuPage(self.driver)
#         akpp_page = AkppPage(self.driver)
#
#         login_page.login(email_address, password)
#         nav_menu_page.get_akpp()
#         akpp_page.go_to_profile()
#         assert "Членство АКПП" == akpp_page.get_text_akkp()
#
