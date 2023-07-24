import pytest
import allure
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
    @pytest.mark.xfail
    def test_positive_header_basket1_smoke(self, driver, setup):
        main_page, item_page, basket_page = setup
        driver.get(MAIN_PAGE_STAGE_URL)
        main_page.go_to_random_item()
        article_text = item_page.add_item_to_basket_and_go_to_basket()
        product_code = basket_page.get_product_code()
        assert article_text == product_code, "Артикул товара не совпадает с кодом товара в корзине"

    @allure.title("TC 004 - Функционал блока 'Советы от профессионалов ремонта'")
    @pytest.mark.smoke_test
    def test_positive_building_advices1_smoke(self, driver):
        main_page = MainPage(driver)
        driver.get(MAIN_PAGE_STAGE_URL)
        items = main_page.get_building_advices_section()
        urls = [item.get_attribute('href') for item in items]
        for url in urls:
            driver.get(url)
            main_page.check_selectors_article_page()
            assert driver.current_url == url, f"Expected {url}, but got {driver.current_url}"

    @allure.title("TC 005 - Функционал блока 'Советы от профессионалов ремонта'")
    @pytest.mark.smoke_test
    def test_positive_building_advices2_smoke(self, driver):
        main_page = MainPage(driver)
        driver.get(MAIN_PAGE_STAGE_URL)
        items = main_page.get_building_advices_section()
        urls = [item.get_attribute('href') for item in items]
        for url in urls:
            driver.get(url)
            articles = main_page.check_page_content()
            assert articles, "Articles are not present on the page"
