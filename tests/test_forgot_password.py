# import allure
# import pytest
#
# from pages.forgot_password_page import ForgotPasswordPage
# from pages.login_page import LoginPage
# from utilities import ExcelUtilities
#
#
# @pytest.mark.usefixtures("setup_and_teardown")
# @allure.feature("Forgot password")
# class TestForgotPassword:
#
#     @pytest.mark.parametrize("email",
#                              ExcelUtilities.get_data_from_excel("ExcelData/UserData.xlsx", "ValidForgotPassword"))
#     @allure.title("Forgot Password with valid email test")
#     def test_valid_email(self, email):
#         login_page = LoginPage(self.driver)
#         forgot_password_page = ForgotPasswordPage(self.driver)
#
#         login_page.click_forgot_password()
#         forgot_password_page.send_password_reset_link(email)
#         assert "Проверьте вашу электронную почту для дальнейших инструкций по сбросу пароля" == \
#                forgot_password_page.get_success_message()
#
#     @pytest.mark.parametrize("email",
#                              ExcelUtilities.get_data_from_excel("ExcelData/UserData.xlsx",
#                                                                 "NotRegisteredForgotPassword"))
#     @allure.title("Forgot Password with an email that does not exist in the system")
#     def test_not_a_registered_user(self, email):
#         login_page = LoginPage(self.driver)
#         forgot_password_page = ForgotPasswordPage(self.driver)
#
#         login_page.click_forgot_password()
#         forgot_password_page.send_password_reset_link(email)
#         assert "Пользователь с таким email не зарегистрирован" == \
#                forgot_password_page.get_not_registered_user_message()
#
#     @pytest.mark.parametrize("email",
#                              ExcelUtilities.get_data_from_excel("ExcelData/UserData.xlsx",
#                                                                 "InvalidEmailForgotPassword"))
#     @allure.title("Forgot Password with an invalid email address")
#     def test_invalid_email(self, email):
#         login_page = LoginPage(self.driver)
#         forgot_password_page = ForgotPasswordPage(self.driver)
#
#         login_page.click_forgot_password()
#         forgot_password_page.send_password_reset_link(email)
#         assert "Некорректный email" == forgot_password_page.get_invalid_email_message()
