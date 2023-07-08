import allure
import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage
from utilities import ExcelUtilities


@pytest.mark.usefixtures("setup_and_teardown")
@allure.severity("Blocker")
@allure.feature("Login")
class TestLogin():

    @pytest.mark.parametrize("email_address, password",
                             ExcelUtilities.get_data_from_excel("ExcelData/UserData.xlsx", "ValidLogin"))
    @allure.description("Valid login")
    @allure.title("Login with valid credentials test")
    def test_valid_login(self, email_address, password):
        login_page = LoginPage(self.driver)
        main_page = MainPage(self.driver)
        login_page.login(email_address, password)
        assert "Вы успешно авторизовались" == main_page.successful_authorization(), "The user is not logged in"

    @pytest.mark.parametrize("email_address, password",
                             ExcelUtilities.get_data_from_excel("ExcelData/UserData.xlsx", "InvalidLogin"))
    @allure.description("Invalid login(password or login)")
    @allure.title("Login with invalid credentials test")
    def test_invalid_login(self, email_address, password):
        login_page = LoginPage(self.driver)

        login_page.login(email_address, password)
        assert "Неверный логин или пароль! Попробуйте снова" == login_page.get_login_error(), \
            "Not found error authorization"

    # @allure.description("Login without date")
    # @allure.title("Login without login and password")
    # def test_without_login_and_password(self, login_page):
    #     login_page.login("", "")
    #     assert "Это поле обязательное" == login_page.get_error_fild()
