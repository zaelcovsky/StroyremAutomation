import time

import pytest
import allure

from pages.basket_page import BasketPage
from pages.item_page import ItemPage
from pages.main_page import MainPage
from constants import MAIN_PAGE_STAGE_URL, MAIN_PAGE_TITLE


@allure.epic("Main Page")
class TestMainPage:

    # @allure.title("TC 001 - проверка логотипа Stroyrem в хедере на главной странице")
    # @pytest.mark.smoke_test
    # def test_001_visibility_of_header_logo(self, driver, open_and_load_main_page):
    #     main_page = MainPage(driver)
    #     main_page.check_that_image_is_present_and_visible_on_the_page(BasePageLocators.HEADER_LOGO)

    @allure.title("TC 002 - проверка title на главной странице")
    @pytest.mark.regression_test
    def test_002_visibility_of_page_title(self, driver):
        main_page = MainPage(driver)
        driver.get(MAIN_PAGE_STAGE_URL) #нужно поправить 
        assert main_page.get_stroimaterialy_section().text == MAIN_PAGE_TITLE

    @allure.title("TC 003 - Функционал кнопоки 'Корзина' в шапке главной страницы")
    @pytest.mark.smoke_test
    @pytest.mark.xfail(reason="Если выбранного товара нет в наличии, то селектор _pd_articul все равно активен, \
                            соответственно тест падает")
    def test_positive_header_basket1_smoke(self, driver, setup):
        main_page, item_page, basket_page = setup
        driver.get(MAIN_PAGE_STAGE_URL)
        main_page.go_to_random_item()
        article_text = item_page.add_item_to_basket_and_go_to_basket()
        product_code = basket_page.get_product_code()
        assert article_text == product_code, "Артикул товара не совпадает с кодом товара в корзине"
