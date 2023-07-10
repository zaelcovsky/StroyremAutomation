import pytest
import allure
from pages.base_page import BasePage
from pages.main_page import MainPage
from locators.locators import MainPageLocators, BasePageLocators


@allure.epic("Main Page")
class TestMainPage:

    @allure.title("TC 001 - проверка логотипа Stroyrem в хедере на главной странице")
    @pytest.mark.smoke_test
    def test_001_visibility_of_header_logo(self, driver, open_and_load_main_page):
        main_page = MainPage(driver)
        main_page.check_that_image_is_present_and_visible_on_the_page(BasePageLocators.HEADER_LOGO)

    @allure.title("TC 002 - проверка title на главной странице")
    @pytest.mark.regression_test
    def test_002_visibility_of_page_title(self, driver):
        main_page = MainPage(driver)
        page_url = "https://test2.stroyrem-nn.ru/"
        page_title = 'СТРОЙРЕМ — магазин строительных и отделочных материалов в Н. Новгороде.'
        main_page.check_page_title(page_title, page_url)
