from tests.test_base import BaseTest


class TestRegistration(BaseTest):

    def test_valid_authorization(self, login_page, registration_page, main_page):
        login_page.get_registration()
        registration_page.create_user("Ivan", "Ivanov", "Ivanovich", "IIIII@gmail.com", "Qwerty123")
        assert "Спасибо за регистрацию!" in main_page.successful_authorization(), "The user hasnt been created"

