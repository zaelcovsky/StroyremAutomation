import pytest
import allure
from constants import MAIN_PAGE_STAGE_URL, ACCOUNT_PAGE, MAIN_PAGE_PROD_URL, RESTORE_PASSWORD_PAGE
from data.credentials import credentials
from tests.test_sign_in.constants_sign_in_page import *


@allure.epic("Sign In Page")
class TestSignInPage:

    @allure.title("Проверка открытия тултипа с кнопками 'Войти' и 'Регистрация' и открытия окна авторизации")
    @pytest.mark.smoke_test
    def test_positive_Open_authorization_form_smoke(self, driver, sign_in_page):
        sign_in_page.get_main_page_profile_icon().click()
        sign_in_button_text = sign_in_page.get_main_page_sign_in_button().text
        sign_up_button_text = sign_in_page.get_main_page_sign_up_button().text
        assert sign_in_button_text == SIGN_IN_BUTTON_TEXT and sign_up_button_text == SIGN_UP_BUTTON_TEXT, \
            f"Текст кнопок {SIGN_IN_BUTTON_TEXT} и {SIGN_UP_BUTTON_TEXT} не соответствует ожидаемым, " \
            f"получили '{sign_in_button_text}' и '{sign_up_button_text}'"
        sign_in_page.get_main_page_sign_in_button().click()
        authorization_window_heading_text = sign_in_page.get_authorization_window_heading().text
        assert authorization_window_heading_text == AUTHORIZATION_WINDOW_HEADING_TEXT, f"Текст заголовка окна " \
            f"авторизации не соответствует ожидаемому, получили {authorization_window_heading_text}"

    @allure.title("Переход с окна авторизации на страницу восстановления пароля")
    @pytest.mark.smoke_test
    def test_positive_Click_Forgot_your_password_smoke(self, driver, sign_in_page, open_sign_in_window):
        sign_in_page.get_forgot_password_link().click()
        assert driver.current_url == RESTORE_PASSWORD_PAGE, f"Неправильный url страницы: {driver.current_url}"
        restore_password_page_heading_text = sign_in_page.get_restore_password_page_heading().text
        assert restore_password_page_heading_text == RESTORE_PASSWORD_PAGE_HEADING_TEXT, f"Текст заголовка страницы" \
            f" восстановления пароля не соответствует ожидаемому, получили {restore_password_page_heading_text}"

    @allure.title("Переход со окна авторизации на главную страницу по клику на логотипе Стройрем")
    @pytest.mark.regression_test
    def test_positive_Go_main_page_clicking_logo_button_on_authorization_form_regress(self, driver, sign_in_page,
                                                                                      open_sign_in_window):
        sign_in_page.get_authorization_window_logo().click()
        assert sign_in_page.check_authorization_window_logo_is_not_visible() is True, \
            "Главная страница не отображается"



