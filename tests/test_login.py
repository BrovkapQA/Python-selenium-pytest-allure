import allure
import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage
from tests.test_base import BaseTest
from utilities import ExcelUtilities


@allure.feature("Login")
class TestLogin(BaseTest):

    @pytest.mark.parametrize("email_address, password",
                             ExcelUtilities.get_data_from_excel("ExcelData/UserData.xlsx", "ValidLogin"))
    @allure.title("Login with valid credentials test")
    def test_valid_login(self, email_address, password):
        self.login_page.login(email_address, password)
        assert "Вы успешно авторизовались" == self.main_page.successful_authorization(), "The user is not logged in"

    @pytest.mark.parametrize("email_address, password",
                             ExcelUtilities.get_data_from_excel("ExcelData/UserData.xlsx", "InvalidLogin"))
    @allure.title("Login with invalid credentials test")
    def test_invalid_login(self, email_address, password):
        self.login_page.login(email_address, password)
        assert "Неверный логин или пароль! Попробуйте снова" == self.login_page.get_login_error(), \
            "Not found error authorization"

    @allure.title("Login without login and password")
    def test_without_login_and_password(self):
        self.login_page.login("", "")
        assert "Это поле обязательное" == self.login_page.get_error_fild()
