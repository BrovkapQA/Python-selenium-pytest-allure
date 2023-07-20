import allure
import pytest
from tests.test_base import BaseTest
from utilities import ExcelUtilities


@allure.feature("Registration user features")
class TestRegistration(BaseTest):

    @pytest.mark.parametrize("name, middle_name, last_name, email, password, birthday",
                             ExcelUtilities.get_data_from_excel("ExcelData/UserData.xlsx", "ValidUserRegistration"))
    @allure.title("Registration a new user with valid date")
    def test_valid_authorization(self, name, middle_name, last_name, email, password, birthday):
        self.login_page.get_registration()
        self.registration_page.create_user(name, middle_name, last_name, email, password, birthday)
        assert "Спасибо за регистрацию!" in self.main_page.successful_authorization(), "The user hasn't been created"
