import pytest
import allure
from constants import *
from data.credentials import credentials
from tests.test_sign_in.conftest import get_name_and_email_in_account
from tests.test_sign_in.constants_sign_in_page import *
from time import sleep
from selenium.common import NoSuchElementException, NoSuchWindowException


@allure.epic("Sign In Page")
class TestSignInPage:

    @allure.title("Переход со окна авторизации на главную страницу по клику на логотипе Стройрем")
    @pytest.mark.regression_test
    def test_positive_Go_main_page_clicking_logo_button_on_authorization_form_regress(self, driver, sign_in_page,
                                                                                      open_sign_in_window):
        sign_in_page.get_authorization_window_logo().click()
        assert sign_in_page.check_authorization_window_logo_is_not_visible() is True, \
            "Главная страница не отображается"

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

    @allure.title("Авторизация с помощью аккаунта mail.ru")
    @pytest.mark.smoke_test
    def test_positive_authorization_first_time_using_MAIL_smoke(self, driver, sign_in_page, open_sign_in_window):
        sign_in_page.get_mail_auth_icon().click()
        driver.switch_to.window(driver.window_handles[1])
        sign_in_page.get_mail_ru_window_email_field().send_keys(credentials['mail.ru_email'])
        sign_in_page.get_mail_ru_window_password_field().send_keys(credentials['mail.ru_password'])
        sign_in_page.get_mail_ru_window_submit_button().click()
        driver.switch_to.window(driver.window_handles[0])
        sign_in_page.check_number_of_windows_to_be_equal(1)
        sleep(10)
        assert driver.current_url == ACCOUNT_PAGE, f"Неправильный url страницы: {driver.current_url}"
        name, email = get_name_and_email_in_account(driver, sign_in_page)
        assert name == credentials['mail.ru_name'] and email == credentials['mail.ru_email'], \
            f"ФИО или email не соответствуют ожидаемым, ФИО: {name}, email: {email}"

    @allure.title("Авторизация с помощью аккаунта OK.ru")
    # @pytest.mark.xfail(reason="хранение логинов/паролей не реализовано")
    @pytest.mark.smoke_test
    def test_positive_authorization_first_time_using_OK_smoke(self, driver, sign_in_page, open_sign_in_window):
        sign_in_page.get_ok_ru_auth_icon().click()
        driver.switch_to.window(driver.window_handles[1])
        driver.add_cookie({'name': 'bci',
                           'value': '232693873704985418',
                           'domain': '.ok.ru',
                           'httpOnly': True,
                           'path': '/',
                           'expiry': 1726518377,
                           'secure': True})
        driver.add_cookie({'name': '_statid',
                           'value': '2ee9fe98-ab2c-4d1f-9c04-30b8090d3f61',
                           'domain': '.ok.ru',
                           'httpOnly': True,
                           'path': '/',
                           'expiry': 1726518377,
                           'secure': True})
        driver.add_cookie({'name': 'landref',
                           'value': 'stroyrem-nn.ru',
                           'domain': '.ok.ru',
                           'httpOnly': False,
                           'path': '/',
                           'expiry': 1726518377,
                           'secure': True})
        driver.add_cookie({'name': '__last_online',
                           'value': '1691958637776',
                           'domain': 'connect.ok.ru',
                           'httpOnly': False,
                           'path': '/',
                           'expiry': 1726518638,
                           'secure': True})
        sign_in_page.get_ok_ru_window_email_field().send_keys(credentials['ok.ru_email'])
        sign_in_page.get_ok_ru_window_password_field().send_keys(credentials['ok.ru_password'])
        sign_in_page.get_ok_ru_window_submit_button().click()
        # на новых аккаунтах нужно еще кликнуть акцепт
        # self.driver.find_element(*self._ok_ru_window_accept_button).click()
        driver.switch_to.window(driver.window_handles[0])
        sign_in_page.check_number_of_windows_to_be_equal(1)
        # c OK.ru не подтягивается email, нужно вводить вручную https://trello.com/c/D1M0KnkP
        # self.driver.find_element(*self._ulogin_window_email_field).send_keys(email)
        # self.driver.find_element(*self._ulogin_window_submit_button).click()
        sleep(10)
        assert driver.current_url == ACCOUNT_PAGE, f"Неправильный url страницы: {driver.current_url}"
        name, email = get_name_and_email_in_account(driver, sign_in_page)
        assert name == credentials['ok.ru_name'] and email == credentials['ok.ru_email'], \
            f"ФИО или email не соответствуют ожидаемым, ФИО: {name}, email: {email}"

    @allure.title("Авторизация с помощью аккаунта vk.ru")
    @pytest.mark.smoke_test
    def test_positive_authorization_first_time_using_VK_smoke(self, driver, sign_in_page, open_sign_in_window):
        sign_in_page.get_vk_ru_auth_icon().click()
        driver.switch_to.window(driver.window_handles[1])
        sign_in_page.get_vk_ru_window_email_field().send_keys(credentials['vk.ru_email'])
        sign_in_page.get_vk_ru_window_proceed_button().click()
        sign_in_page.get_vk_ru_window_password_field().send_keys(credentials['vk.ru_password'])
        sign_in_page.get_vk_ru_window_submit_button().click()
        sign_in_page.get_vk_ru_window_continue_as_button().click()
        driver.switch_to.window(driver.window_handles[0])
        sign_in_page.check_number_of_windows_to_be_equal(1)
        sleep(10)
        assert driver.current_url == ACCOUNT_PAGE, f"Неправильный url страницы: {driver.current_url}"
        name, email = get_name_and_email_in_account(driver, sign_in_page)
        assert name == credentials['vk.ru_name'] and email == credentials['vk.ru_email'], \
            f"ФИО или email не соответствуют ожидаемым, ФИО: {name}, email: {email}"

    @allure.title("Авторизация с помощью аккаунта ya.ru")
    @pytest.mark.xfail(reason="Появляется капча Яндекса при запуске теста на Github")
    @pytest.mark.smoke_test
    def test_positive_authorization_first_time_using_YA_smoke(self, driver, sign_in_page, open_sign_in_window):
        sign_in_page.get_ya_ru_auth_icon().click()
        driver.switch_to.window(driver.window_handles[1])
        # driver.delete_all_cookies()
        driver.add_cookie({'name': 'uniqueuid',
                           'value': '384528911692006899',
                           'domain': 'passport.yandex.ru',
                           'httpOnly': True,
                           'path': '/',
                           'expiry': 1723499808,
                           'sameSite': 'Lax',
                           'secure': True})
        driver.add_cookie({'name': 'ymex',
                           'value': '2007366920.yrts.1692006920#2007366900.yrtsi.1692006900',
                           'domain': '.yandex.ru',
                           'httpOnly': False,
                           'path': '/',
                           'expiry': 1723499808,
                           'secure': True})
        driver.add_cookie({'name': 'i',
                           'value': 'rpEp6ASpcmkXAketS0UdMiVBT6ovBbPtyYRYZIsRWdkwRjrAU27Q2rmgTx58XJTCF6sreSZhfheTbJeEsS',
                           'domain': '.yandex.ru',
                           'httpOnly': True,
                           'path': '/',
                           'expiry': 1723499808,
                           'secure': True})
        driver.add_cookie({'name': 'yandexuid',
                           'value': '5114601221692006901',
                           'domain': '.yandex.ru',
                           'httpOnly': False,
                           'path': '/',
                           'expiry': 1723499808,
                           'secure': True})
        driver.add_cookie({'name': 'yuidss',
                           'value': '7640250911692006900',
                           'domain': '.yandex.ru',
                           'httpOnly': False,
                           'path': '/',
                           'expiry': 1723499808,
                           'secure': True})
        driver.add_cookie({'name': 'gdpr',
                           'value': '0',
                           'domain': '.yandex.ru',
                           'httpOnly': False,
                           'path': '/',
                           'expiry': 1723499808,
                           'secure': True})
        driver.add_cookie({'name': '_ym_uid',
                           'value': '169200690291832112',
                           'domain': '.yandex.ru',
                           'httpOnly': False,
                           'path': '/',
                           'expiry': 1723499808,
                           'secure': True})
        driver.add_cookie({'name': '_ym_d',
                           'value': '1692006902',
                           'domain': '.yandex.ru',
                           'httpOnly': False,
                           'path': '/',
                           'expiry': 1723499808,
                           'secure': True})
        driver.add_cookie({'name': 'bh',
                           'value': 'Ej8iTm90L0EpQnJhbmQiO3Y9Ijk5IiwiR29vZ2xlIENocm9tZSI7dj0iMTE1IiwiQ2hyb21pdW0iO3Y9IjExNSIaBSJ4ODYiIhAiMTE1LjAuNTc5MC4xMTAiKgI',
                           'domain': 'yandex.ru',
                           'httpOnly': False,
                           'path': '/',
                           'expiry': 1723499808,
                           'secure': False})
        driver.add_cookie({'name': '_ym_visorc',
                           'value': 'b',
                           'domain': '.yandex.ru',
                           'httpOnly': False,
                           'path': '/',
                           'expiry': 1723499808,
                           'secure': True})
        driver.execute_script("arguments[0].scrollIntoView();",
                              sign_in_page.get_ya_ru_window_alternative_ways_to_sign_up())
        driver.execute_script("arguments[0].click();", sign_in_page.get_ya_ru_window_alternative_ways_to_sign_up())
        sign_in_page.get_ya_ru_window_email_field().send_keys(credentials['ya.ru_email'])
        sign_in_page.get_ya_ru_window_submit_button().click()
        sign_in_page.get_ya_ru_window_password_field().send_keys(credentials['ya.ru_password'])
        sign_in_page.get_ya_ru_window_submit_button().click()
        sleep(5)
        try:
            sign_in_page.get_ya_ru_window_control_question_field()
            sign_in_page.get_ya_ru_window_control_question_field().send_keys(credentials['ya.ru_question'])
            sign_in_page.get_ya_ru_window_proceed_button().click()
            print(f"\nПоявилось окно контрольного вопроса")
        except (NoSuchWindowException, NoSuchElementException):
            print(f"\nНе появилось окно контрольного вопроса")
        driver.switch_to.window(driver.window_handles[0])
        sign_in_page.check_number_of_windows_to_be_equal(1)
        sleep(10)
        assert driver.current_url == ACCOUNT_PAGE, f"Неправильный url страницы: {driver.current_url}"
        name, email = get_name_and_email_in_account(driver, sign_in_page)
        assert name == credentials['ya.ru_name'] and email == credentials['ya.ru_email'], \
            f"ФИО или email не соответствуют ожидаемым, ФИО: {name}, email: {email}"

    @allure.title("Авторизация с помощью формы авторизации")
    @pytest.mark.smoke_test
    def test_positive_login_with_correct_email_and_password_smoke(self, driver, sign_in_page, open_sign_in_window):
        sign_in_page.get_email_field().send_keys(credentials['email'])
        sign_in_page.get_password_field().send_keys(credentials['password'])
        sign_in_page.get_sign_in_button().click()
        assert driver.current_url == ACCOUNT_PAGE, f"Неправильный url страницы: {driver.current_url}"
        name, email = get_name_and_email_in_account(driver, sign_in_page)
        assert name == credentials['name'] and email == credentials['email'], \
            f"ФИО или email не соответствуют ожидаемым, ФИО: {name}, email: {email}"

