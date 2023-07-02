import allure

from tests.test_base import BaseTest

@allure.severity("Blocker")
@allure.feature("Registration user features")
class TestRegistration(BaseTest):

    @allure.description("Valid registration")
    @allure.title("Registration a new user with valid date")
    def test_valid_authorization(self, login_page, registration_page, main_page):
        login_page.get_registration()
        registration_page.create_user("Ivan", "Ivanov", "Ivanovich", "IIIII@gmail.com", "Qwerty123")
        assert "Спасибо за регистрацию!" in main_page.successful_authorization(), "The user hasn't been created"

