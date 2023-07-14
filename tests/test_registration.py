import allure
import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage
from utilities import ExcelUtilities


@pytest.mark.usefixtures("setup_and_teardown")
@allure.feature("Registration user features")
class TestRegistration:

    @pytest.mark.parametrize("name, middle_name, last_name, email, password, year, month",
                             ExcelUtilities.get_data_from_excel("ExcelData/UserData.xlsx", "ValidUserRegistration"))
    @allure.description("Valid registration")
    @allure.title("Registration a new user with valid date")
    def test_valid_authorization(self, name, middle_name, last_name, email, password, date):
        login_page = LoginPage(self.driver)
        main_page = MainPage(self.driver)
        registration_page = RegistrationPage(self.driver)

        login_page.get_registration()
        registration_page.create_user(name, middle_name, last_name, email, password, date)
        assert "Спасибо за регистрацию!" in main_page.successful_authorization(), "The user hasn't been created"
