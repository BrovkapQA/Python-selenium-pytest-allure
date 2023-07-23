# import allure
# import pytest
# from tests.test_base import BaseTest
# from utilities.excel_utilities import ExcelReader
#
#
# @allure.feature("Forgot password")
# class TestForgotPassword(BaseTest):
#
#     @pytest.mark.parametrize("email", ExcelReader("data.xlsx").get_data_from_excel("ValidForgotPassword"))
#     @allure.title("Forgot Password with valid email test")
#     def test_valid_email(self, email, json_data):
#         self.login_page.click_forgot_password()
#         self.forgot_password_page.send_password_reset_link(email)
#         expected_message = json_data["forgot_password"]["success_message"]
#         assert expected_message == self.forgot_password_page.get_success_message()
#
#     @pytest.mark.parametrize("email", ExcelReader("data.xlsx").get_data_from_excel("NotRegisteredForgotPassword"))
#     @allure.title("Forgot Password with an email that does not exist in the system")
#     def test_not_a_registered_user(self, email, json_data):
#         self.login_page.click_forgot_password()
#         self.forgot_password_page.send_password_reset_link(email)
#         expected_message = json_data["forgot_password"]["error_message_unregistered_user"]
#         assert expected_message == self.forgot_password_page.get_not_registered_user_message()
#
#     @pytest.mark.parametrize("email", ExcelReader("data.xlsx").get_data_from_excel("InvalidEmailForgotPassword"))
#     @allure.title("Forgot Password with an invalid email address")
#     def test_invalid_email(self, email, json_data):
#         self.login_page.click_forgot_password()
#         self.forgot_password_page.send_password_reset_link(email)
#         expected_message = json_data["forgot_password"]["uncorrected_email"]
#         assert expected_message == self.forgot_password_page.get_invalid_email_message()
