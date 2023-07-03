from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage
from selenium.webdriver.common.by import By


class BaseTest:
    login_page: LoginPage
    main_page: MainPage
    registration_page: RegistrationPage
    forgot_password_page: ForgotPasswordPage
