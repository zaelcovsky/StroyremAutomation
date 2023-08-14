import pytest
from pages.sign_in_page import SignInPage
from constants import *
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture(scope='function')
def sign_in_page(driver):
    sign_in_page = SignInPage(driver)
    driver.get(MAIN_PAGE_PROD_URL)
    return sign_in_page


@pytest.fixture(scope='function')
def open_sign_in_window(driver, sign_in_page):
    """
    Осуществляет переход с главной страницы на окно авторизации
    """
    sign_in_page.get_main_page_profile_icon().click()
    action = ActionChains(driver)
    sign_in_button = sign_in_page.element_is_clickable(sign_in_page._main_page_sign_in_button)
    action.move_to_element(sign_in_button).click().perform()


def get_name_and_email_in_account(driver, sign_in_page):
    """
    Получает ФИО и email созданного аккаунта
    """
    driver.get(PERSONAL_DATA_PAGE)
    sign_in_page.get_account_page_fizik_section().click()
    name = sign_in_page.get_account_page_name_field().get_attribute('value')
    email = sign_in_page.get_account_page_email_field().get_attribute('value')
    return name, email
