from pages.Nav_menu_page import NavMenuPage
from pages.akpp_page import AkppPage
from pages.calendar_page import CalendarPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage


class BaseTest:
    login_page: LoginPage
    main_page: MainPage
    nav_menu_page: NavMenuPage
    calendar_page: CalendarPage
    forgot_password_page: ForgotPasswordPage
    registration_page: RegistrationPage
    akpp_page: AkppPage
