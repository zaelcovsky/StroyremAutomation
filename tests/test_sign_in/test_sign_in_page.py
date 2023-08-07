import pytest
import allure
from constants import *
# from data.credentials import credentials
from tests.test_sign_in.constants_sign_in_page import *
from time import sleep


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
    @pytest.mark.xfail(reason="хранение логинов/паролей не реализовано")
    @pytest.mark.smoke_test
    def test_positive_authorization_first_time_using_MAIL_smoke(self, driver, sign_in_page, open_sign_in_window):
        sign_in_page.get_mail_auth_icon().click()
        driver.switch_to.window(driver.window_handles[1])
        sign_in_page.get_mail_ru_window_email_field().send_keys(credentials['mail.ru_email'])
        sign_in_page.get_mail_ru_window_password_field().send_keys(credentials['mail.ru_password'])
        sign_in_page.get_mail_ru_window_submit_button().click()
        driver.switch_to.window(driver.window_handles[0])
        sign_in_page.check_number_of_windows_to_be_equal(1)
        sleep(4)
        assert driver.current_url == ACCOUNT_PAGE, f"Неправильный url страницы: {driver.current_url}"
        driver.get(PERSONAL_DATA_PAGE)
        sign_in_page.get_account_page_fizik_section().click()
        name = sign_in_page.get_account_page_name_field().get_attribute('value')
        email = sign_in_page.get_account_page_email_field().get_attribute('value')
        assert name == credentials['mail.ru_name'] and email == credentials['mail.ru_email'], \
            f"ФИО или email не соответствуют ожидаемым, ФИО: {name}, email: {email}"

    @allure.title("Авторизация с помощью аккаунта OK.ru")
    @pytest.mark.xfail(reason="хранение логинов/паролей не реализовано")
    @pytest.mark.smoke_test
    def test_positive_authorization_first_time_using_OK_smoke(self, driver, sign_in_page, open_sign_in_window):
        sign_in_page.get_ok_ru_auth_icon().click()
        driver.switch_to.window(driver.window_handles[1])
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
        sleep(4)
        assert driver.current_url == ACCOUNT_PAGE, f"Неправильный url страницы: {driver.current_url}"
        driver.get(PERSONAL_DATA_PAGE)
        sign_in_page.get_account_page_fizik_section().click()
        name = sign_in_page.get_account_page_name_field().get_attribute('value')
        email = sign_in_page.get_account_page_email_field().get_attribute('value')
        assert name == credentials['ok.ru_name'] and email == credentials['ok.ru_email'], \
            f"ФИО или email не соответствуют ожидаемым, ФИО: {name}, email: {email}"

    @allure.title("Авторизация с помощью аккаунта vk.ru")
    @pytest.mark.xfail(reason="хранение логинов/паролей не реализовано")
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
        sleep(4)
        assert driver.current_url == ACCOUNT_PAGE, f"Неправильный url страницы: {driver.current_url}"
        driver.get(PERSONAL_DATA_PAGE)
        sign_in_page.get_account_page_fizik_section().click()
        name = sign_in_page.get_account_page_name_field().get_attribute('value')
        email = sign_in_page.get_account_page_email_field().get_attribute('value')
        assert name == credentials['vk.ru_name'] and email == credentials['vk.ru_email'], \
            f"ФИО или email не соответствуют ожидаемым, ФИО: {name}, email: {email}"

    @allure.title("Авторизация с помощью аккаунта ya.ru")
    @pytest.mark.xfail(reason="хранение логинов/паролей не реализовано")
    @pytest.mark.smoke_test
    def test_positive_authorization_first_time_using_YA_smoke(self, driver, sign_in_page, open_sign_in_window):
        sign_in_page.get_ya_ru_auth_icon().click()
        driver.switch_to.window(driver.window_handles[1])
        sign_in_page.get_ya_ru_window_alternative_ways_to_sign_up().click()
        sign_in_page.get_ya_ru_window_email_field().send_keys(credentials['ya.ru_email'])
        sign_in_page.get_ya_ru_window_submit_button().click()
        sign_in_page.get_ya_ru_window_password_field().send_keys(credentials['ya.ru_password'])
        sign_in_page.get_ya_ru_window_submit_button().click()
        driver.switch_to.window(driver.window_handles[0])
        sign_in_page.check_number_of_windows_to_be_equal(1)
        sleep(4)
        assert driver.current_url == ACCOUNT_PAGE, f"Неправильный url страницы: {driver.current_url}"
        driver.get(PERSONAL_DATA_PAGE)
        sign_in_page.get_account_page_fizik_section().click()
        name = sign_in_page.get_account_page_name_field().get_attribute('value')
        email = sign_in_page.get_account_page_email_field().get_attribute('value')
        assert name == credentials['ya.ru_name'] and email == credentials['ya.ru_email'], \
            f"ФИО или email не соответствуют ожидаемым, ФИО: {name}, email: {email}"

    @allure.title("Авторизация с помощью формы авторизации")
    @pytest.mark.xfail(reason="хранение логинов/паролей не реализовано")
    @pytest.mark.smoke_test
    def test_positive_login_with_correct_email_and_password_smoke(self, driver, sign_in_page, open_sign_in_window):
        sign_in_page.get_email_field().send_keys(credentials['email'])
        sign_in_page.get_password_field().send_keys(credentials['password'])
        sign_in_page.get_sign_in_button().click()
        assert driver.current_url == ACCOUNT_PAGE, f"Неправильный url страницы: {driver.current_url}"
        driver.get(PERSONAL_DATA_PAGE)
        sign_in_page.get_account_page_fizik_section().click()
        name = sign_in_page.get_account_page_name_field().get_attribute('value')
        email = sign_in_page.get_account_page_email_field().get_attribute('value')
        assert name == credentials['name'] and email == credentials['email'], \
            f"ФИО или email не соответствуют ожидаемым, ФИО: {name}, email: {email}"











