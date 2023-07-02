import pytest

from tests.test_base import BaseTest


class TestLogin(BaseTest):

    def test_valid_login(self, login_page, main_page):
        login_page.login("test_user_1@gmail.com", "Qwerty123")
        assert "Вы успешно авторизовались" == main_page.successful_authorization(), "The user is not logged in"


    @pytest.mark.parametrize("user_login, user_password",
                             [("test_user_1@gmail.com", "invalid_password"),
                              (" test_user_1@gmail.com ", " Qwerty123 "),
                              ("invalid_login1@gmail.com", "invalid_password1"),
                              (" test_user_1@gmail.com ", " Qwerty123 ")])
    def test_invalid_login(self, login_page, user_login, user_password):
        login_page.login(user_login, user_password)
        assert "Неверный логин или пароль! Попробуйте снова" == login_page.get_login_error(), "Not found error authorization"

    def test_without_login_and_password(self, login_page):
        login_page.login("", "")
        assert "Это поле обязательное" == login_page.get_error_fild()
