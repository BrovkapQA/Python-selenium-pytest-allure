# import allure
# import pytest
# from tests.test_base import BaseTest
# from utilities.excel_utilities import ExcelReader
#
#
# @allure.feature("Registration user features")
# class TestRegistration(BaseTest):
#
#     @pytest.mark.parametrize("name, middle_name, last_name, email, password, birthday",
#                              ExcelReader("data.xlsx").get_data_from_excel("ValidUserRegistration"))
#     @allure.title("Registration a new user with valid date")
#     def test_valid_authorization(self, json_data, name, middle_name, last_name, email, password, birthday):
#         self.login_page.get_registration()
#         self.registration_page.create_user(name, middle_name, last_name, email, password, birthday)
#         expected_message = json_data["registration"]["success_registration"]
#         assert expected_message in self.main_page.successful_authorization(), "The user hasn't been created"
