import allure
import pytest
from tests.test_base import BaseTest
from utilities.excel_utilities import ExcelReader


@allure.feature("Login")
class TestLogin(BaseTest):

    @pytest.mark.parametrize("email_address, password", ExcelReader("data.xlsx").get_data_from_excel("ValidLogin"))
    @allure.title("Login with valid credentials test")
    def test_valid_login(self, email_address, password, json_data):

        self.login_page.login(email_address, password)
        expected_message = json_data["login"]["success_login"]
        assert expected_message == self.main_page.successful_authorization(), "The user is not logged in"

    @pytest.mark.parametrize("email_address, password", ExcelReader("data.xlsx").get_data_from_excel("InvalidLogin"))
    @allure.title("Login with invalid credentials test")
    def test_invalid_login(self, email_address, password, json_data):
        self.login_page.login(email_address, password)
        expected_message = json_data["login"]["error_login"]
        assert expected_message == self.login_page.get_login_error(), "Not found error authorization"

    @allure.title("Login without login and password")
    def test_without_login_and_password(self, json_data):
        self.login_page.login("", "")
        expected_message = json_data["login"]["error_without_login_or_password"]
        assert expected_message == self.login_page.get_error_fild()
