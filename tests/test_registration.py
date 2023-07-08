import allure
import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage


@pytest.mark.usefixtures("setup_and_teardown")
@allure.severity("Blocker")
@allure.feature("Registration user features")
class TestRegistration():

    @pytest.mark.xfail("it is necessary to update the user, I will automate this process a little later")
    @allure.description("Valid registration")
    @allure.title("Registration a new user with valid date")
    def test_valid_authorization(self):
        login_page = LoginPage(self.driver)
        main_page = MainPage(self.driver)
        registration_page = RegistrationPage(self.driver)

        login_page.get_registration()
        registration_page.create_user("Ivan", "Ivanov", "Ivanovich", "IIIII@gmail.com", "Qwerty123")
        assert "Спасибо за регистрацию!" in main_page.successful_authorization(), "The user hasn't been created"
#
