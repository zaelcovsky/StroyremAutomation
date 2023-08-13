from base.seleniumbase import SeleniumBase
import allure
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver import Keys
from constants import PERSONAL_DATA_PAGE


class SignInPage(SeleniumBase):

    # в __init__ храним название локатора и его значение для необходимой страницы
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # главная страница
        self._main_page_header = (By.XPATH, "//header[@class='header']")
        self._main_page_profile_icon = (By.CSS_SELECTOR, ".header-profile-link.auth-tooltip-show")
        # self._main_page_sign_in_button = (By.XPATH, "//div[@class='auth-tooltip active']/div/a[1]")
        self._main_page_sign_in_button = (By.CSS_SELECTOR, "a[class='show-auth-modal']")
        self._main_page_sign_up_button = (By.CSS_SELECTOR, "a.register-link")
        self._main_page_header_logo_zzz = (By.CSS_SELECTOR,
                                           "div[class='header-row header-row-2'] div[class='header-logo'] img")
        # окно авторизации
        self._authorization_window_heading = (By.CSS_SELECTOR, "div.auth-h1")
        self._vk_auth_icon = (By.CSS_SELECTOR, ".vk-auth")
        self._ya_auth_icon = (By.CSS_SELECTOR, ".ya-auth")
        self._ok_auth_icon = (By.CSS_SELECTOR, ".ok-auth")
        self._mail_auth_icon = (By.CSS_SELECTOR, ".mail-auth")
        self._email_field = (By.CSS_SELECTOR, "input[placeholder='example@gmail.com']")
        self._password_field = (By.CSS_SELECTOR, "input[placeholder='Пароль']")
        self._remember_me_checkbox = (By.XPATH, "//div[@class='flex-column-block']//span")
        self._forgot_password_link = (By.CSS_SELECTOR, "div.link-row a")
        self._sign_in_button = (By.CSS_SELECTOR, "input[value='Войти']")
        self._sign_up_button = (By.CSS_SELECTOR, ".btn.yellow-btn-invert")
        self._authorization_window_logo = (By.CSS_SELECTOR, "div[id='login-modal'] div[class='header-logo'] a")
        # окно mail.ru
        self._mail_ru_window_email_field = (By.CSS_SELECTOR, "#login")
        self._mail_ru_window_password_field = (By.CSS_SELECTOR, "#password")
        self._mail_ru_window_submit_button = (By.CSS_SELECTOR, "button[type='submit']")
        # страница аккаунта
        self._account_page_fizik_section = (By.XPATH, "//div[@class='person-type active set-fiz-entity']")
        self._account_page_name_field = (By.CSS_SELECTOR, ".form-block>input[name='name']")
        self._account_page_email_field = (By.CSS_SELECTOR, "div.form-block>input[name='email']")
        # окно OK.ru
        self._ok_ru_window_email_field = (By.CSS_SELECTOR, "#field_email")
        self._ok_ru_window_password_field = (By.CSS_SELECTOR, "#field_password")
        self._ok_ru_window_submit_button = (By.CSS_SELECTOR, "input[type='submit']")
        self._ok_ru_window_accept_button = (By.CSS_SELECTOR, "button[name='button_accept_request']")
        # окно ulogin
        self._ulogin_window_email_field = (By.CSS_SELECTOR, "input[id='email']")
        self._ulogin_window_submit_button = (By.CSS_SELECTOR, "div[id='submit']")
        # окно vk.ru
        self._vk_ru_window_email_field = (By.CSS_SELECTOR, "input[name='login']")
        self._vk_ru_window_proceed_button = (By.CSS_SELECTOR, "button[type='submit']")
        self._vk_ru_window_password_field = (By.CSS_SELECTOR, "input[name='password']")
        self._vk_ru_window_submit_button = (By.CSS_SELECTOR, "button[type='submit']")
        self._vk_ru_window_continue_as_button = (By.CSS_SELECTOR, "div.vkc__ButtonOneTap__buttonText")
        # окно ya.ru
        self._ya_ru_window_alternative_ways_to_sign_up = (By.CSS_SELECTOR, "button[data-t='button:clear']")
        self._ya_ru_window_email_field = (By.CSS_SELECTOR, "input[data-t='field:input-login']")
        self._ya_ru_window_password_field = (By.CSS_SELECTOR, "input[data-t='field:input-passwd']")
        self._ya_ru_window_submit_button = (By.CSS_SELECTOR, "button[id='passp:sign-in']")
        self._ya_ru_window_control_question_field = (By.CSS_SELECTOR, "input[data-t='field:input-question']")
        self._ya_ru_window_proceed_button = (By.CSS_SELECTOR, "button[data-t='button:action']")
        self._ya_ru_window_authorize_button = (By.CSS_SELECTOR, "div.Authorize-button")
        # страница восстановления пароля
        self._restore_password_page_heading = (By.CSS_SELECTOR, "h1.reg-h1")

    @allure.step("Нахождение элемента: иконка профиля в хедере")
    def get_main_page_profile_icon(self):
        return self.find_element(self._main_page_profile_icon)

    @allure.step("Проверка кликабельности элемента: кнопка 'Войти' в хедере")
    def get_main_page_sign_in_button(self):
        return self.element_is_clickable(self._main_page_sign_in_button)

    @allure.step("Нахождение элемента: кнопка 'Регистрация' в хедере")
    def get_main_page_sign_up_button(self):
        return self.find_element(self._main_page_sign_up_button)

    @allure.step("Нахождение элемента: заголовок окна авторизации")
    def get_authorization_window_heading(self):
        return self.find_element(self._authorization_window_heading)

    @allure.step("Нахождение элемента: поле ввода Email окна авторизации")
    def get_email_field(self):
        return self.find_element(self._email_field)

    @allure.step("Нахождение элемента: поле ввода пароля окна авторизации")
    def get_password_field(self):
        return self.find_element(self._password_field)

    @allure.step("Нахождение элемента: кнопка 'Войти' окна авторизации")
    def get_sign_in_button(self):
        return self.find_element(self._sign_in_button)

    @allure.step("Нахождение элемента: иконка 'mail.ru' окна авторизации")
    def get_mail_auth_icon(self):
        return self.find_element(self._mail_auth_icon)

    @allure.step("Нахождение элемента: поле 'Email' окна авторизации через 'mail.ru'")
    def get_mail_ru_window_email_field(self):
        return self.find_element(self._mail_ru_window_email_field)

    @allure.step("Нахождение элемента: поле 'Пароль' окна авторизации через 'mail.ru'")
    def get_mail_ru_window_password_field(self):
        return self.find_element(self._mail_ru_window_password_field)

    @allure.step("Нахождение элемента: кнопка 'Войти' окна авторизации через 'mail.ru'")
    def get_mail_ru_window_submit_button(self):
        return self.find_element(self._mail_ru_window_submit_button)

    @allure.step("Нахождение элемента: ссылка на секцию 'Физическое лицо' в личном кабинете")
    def get_account_page_fizik_section(self):
        return self.find_element(self._account_page_fizik_section)

    @allure.step("Нахождение элемента: поле 'ФИО' в секции 'Физическое лицо' в личном кабинете")
    def get_account_page_name_field(self):
        return self.find_element(self._account_page_name_field)

    @allure.step("Нахождение элемента: поле 'E-mail' в секции 'Физическое лицо' в личном кабинете")
    def get_account_page_email_field(self):
        return self.find_element(self._account_page_email_field)

    @allure.step("Нахождение элемента: логотип 'Стройрем' окна авторизации")
    def get_authorization_window_logo(self):
        return self.find_element(self._authorization_window_logo)

    @allure.step("Проверка невидимости элемента: логотип 'Стройрем' окна авторизации")
    def check_authorization_window_logo_is_not_visible(self):
        return self.check_element_is_not_visible(self._authorization_window_logo)

    @allure.step("Нахождение элемента: ссылка 'Забыли пароль?' окна авторизации")
    def get_forgot_password_link(self):
        return self.find_element(self._forgot_password_link)

    @allure.step("Нахождение элемента: заголовок страницы восстановления пароля")
    def get_restore_password_page_heading(self):
        return self.find_element(self._restore_password_page_heading)

    @allure.step("Нахождение элемента: иконка 'OK.ru' окна авторизации")
    def get_ok_ru_auth_icon(self):
        return self.find_element(self._ok_auth_icon)

    @allure.step("Нахождение элемента: поле 'Email' окна авторизации через 'OK.ru'")
    def get_ok_ru_window_email_field(self):
        return self.find_element(self._ok_ru_window_email_field)

    @allure.step("Нахождение элемента: поле 'Пароль' окна авторизации через 'OK.ru'")
    def get_ok_ru_window_password_field(self):
        return self.find_element(self._ok_ru_window_password_field)

    @allure.step("Нахождение элемента: кнопка 'Войти' окна авторизации через 'OK.ru'")
    def get_ok_ru_window_submit_button(self):
        return self.find_element(self._ok_ru_window_submit_button)

    @allure.step("Нахождение элемента: иконка 'vk.ru' окна авторизации")
    def get_vk_ru_auth_icon(self):
        return self.find_element(self._vk_auth_icon)

    @allure.step("Проверка кликабельности элемента: поле 'Email' окна авторизации через 'vk.ru'")
    def get_vk_ru_window_email_field(self):
        return self.element_is_clickable(self._vk_ru_window_email_field)

    @allure.step("Проверка кликабельности элемента: поле 'Пароль' окна авторизации через 'vk.ru'")
    def get_vk_ru_window_password_field(self):
        return self.element_is_clickable(self._vk_ru_window_password_field)

    @allure.step("Проверка кликабельности элемента: кнопка 'Войти' окна авторизации через 'vk.ru'")
    def get_vk_ru_window_submit_button(self):
        return self.element_is_clickable(self._vk_ru_window_submit_button)

    @allure.step("Нахождение элемента: кнопка 'Продолжить' окна авторизации через 'vk.ru'")
    def get_vk_ru_window_proceed_button(self):
        return self.find_element(self._vk_ru_window_proceed_button)

    @allure.step("Проверка кликабельности элемента: кнопка 'Продолжить как' окна авторизации через 'vk.ru'")
    def get_vk_ru_window_continue_as_button(self):
        return self.element_is_clickable(self._vk_ru_window_continue_as_button)

    @allure.step("Нахождение элемента: иконка 'ya.ru' окна авторизации")
    def get_ya_ru_auth_icon(self):
        return self.find_element(self._ya_auth_icon)

    @allure.step("Проверка кликабельности элемента: кнопка 'Другие способы входа' окна авторизации через 'ya.ru'")
    def get_ya_ru_window_alternative_ways_to_sign_up(self):
        return self.find_element(self._ya_ru_window_alternative_ways_to_sign_up)

    @allure.step("Проверка кликабельности элемента: поле 'Email' окна авторизации через 'ya.ru'")
    def get_ya_ru_window_email_field(self):
        return self.element_is_clickable(self._ya_ru_window_email_field)

    @allure.step("Проверка кликабельности элемента: поле 'Пароль' окна авторизации через 'ya.ru'")
    def get_ya_ru_window_password_field(self):
        return self.element_is_clickable(self._ya_ru_window_password_field)

    @allure.step("Нахождение элемента: кнопка 'Войти' окна авторизации через 'ya.ru'")
    def get_ya_ru_window_submit_button(self):
        return self.find_element(self._ya_ru_window_submit_button)

    @allure.step("Нахождение элемента: поле 'Ответ на контрольный вопрос' окна авторизации через 'ya.ru'")
    def get_ya_ru_window_control_question_field(self):
        return self.find_element(self._ya_ru_window_control_question_field)

    @allure.step("Нахождение элемента: кнопка 'Продолжить' окна авторизации через 'ya.ru'")
    def get_ya_ru_window_proceed_button(self):
        return self.find_element(self._ya_ru_window_proceed_button)
