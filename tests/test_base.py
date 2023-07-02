from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage


class BaseTest:
    login_page: LoginPage
    main_page: MainPage
    registration_page: RegistrationPage
