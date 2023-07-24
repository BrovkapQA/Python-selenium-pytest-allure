from pages.nav_menu.footer_nav_menu import FooterNavMenu
from pages.nav_menu.main_nav_menu import MainNavMenu
from pages.akpp_page import AkppPage
from pages.calendar_page import CalendarPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.nav_menu.top_nav_menu import TopNavMenu
from pages.registration_page import RegistrationPage


class BaseTest:
    login_page: LoginPage
    main_page: MainPage
    main_nav_menu: MainNavMenu
    calendar_page: CalendarPage
    forgot_password_page: ForgotPasswordPage
    registration_page: RegistrationPage
    akpp_page: AkppPage
    footer_nav_menu: FooterNavMenu
    top_nav_menu: TopNavMenu