import pytest
import allure
from pages.articles_page import ArticlesPage
from pages.delivery_page import DeliveryPage
from pages.main_page import MainPage
from constants import MAIN_PAGE_STAGE_URL, MAIN_PAGE_TITLE, ARTICLES_PAGE_URL, MAIN_PAGE_PROD_URL


# PROD_URL = "https://stroyrem-nn.ru/"
# STAGE_URL = "https://test2.stroyrem-nn.ru/"


# @pytest.mark.parametrize('url', [PROD_URL, STAGE_URL])
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
        driver.get(MAIN_PAGE_STAGE_URL)  # нужно поправить
        assert main_page.get_stroimaterialy_section().text == MAIN_PAGE_TITLE

    @allure.title("TC 003 - Функционал кнопоки 'Корзина' в шапке главной страницы")
    @pytest.mark.smoke_test
    @pytest.mark.xfail
    def test_positive_header_basket1_smoke(self, driver, setup):
        main_page, item_page, basket_page = setup
        driver.get(MAIN_PAGE_PROD_URL)
        main_page.go_to_random_item()
        article_text = item_page.add_item_to_basket_and_go_to_basket()
        product_code = basket_page.get_product_code()
        assert article_text == product_code, "Артикул товара не совпадает с кодом товара в корзине"

    @allure.title("TC 004 - Функционал блока 'Советы от профессионалов ремонта'")
    @pytest.mark.smoke_test
    def test_positive_building_advices1_smoke(self, driver):
        main_page = MainPage(driver)
        driver.get(MAIN_PAGE_PROD_URL)
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
        driver.get(MAIN_PAGE_PROD_URL)
        items = main_page.get_building_advices_section()
        urls = [item.get_attribute('href') for item in items]
        for url in urls:
            driver.get(url)
            articles = main_page.check_page_content()
            assert articles, "Articles are not present on the page"

    @allure.title("TC 006 - Проверка функциональности ссылки 'Обратный звонок' в футере")
    @pytest.mark.smoke_test
    def test_positive_footer_back_call_smoke(self, driver):
        main_page = MainPage(driver)
        driver.get(MAIN_PAGE_PROD_URL)
        result = main_page.check_call_back_link()
        assert result == "Заказать обратный звонок", f"Expected 'Заказать обратный звонок', but got '{result}'"

    @allure.title("TC 007 - Проверка функциональности ссылки 'Строительные советы' в футере")
    @pytest.mark.smoke_test
    def test_positive_footer_building_advices_smoke(self, driver):
        main_page = MainPage(driver)
        articles_page = ArticlesPage(driver)
        driver.get(MAIN_PAGE_PROD_URL)
        main_page.check_building_tips_link()
        assert driver.current_url == ARTICLES_PAGE_URL, "URL after redirect is not correct"
        assert articles_page.get_page_title_text() == "Советы", "Page title is not correct"

    @allure.title("TC 008 - Проверка функциональности ссылки 'Каталог товаров' в футере")
    @pytest.mark.smoke_test
    def test_positive_footer_catalog_smoke(self, driver):
        main_page = MainPage(driver)
        driver.get(MAIN_PAGE_PROD_URL)
        is_displayed, header_text = main_page.check_product_catalog_link()
        assert is_displayed, "Product catalog is not displayed"
        assert header_text == "Каталог", f"Expected 'Каталог', but got '{header_text}'"

    @allure.title("TC 009 - Проверка функциональности ссылки 'Доставка' в футере")
    @pytest.mark.smoke_test
    def test_positive_footer_delivery_smoke(self, driver):
        main_page = MainPage(driver)
        driver.get(MAIN_PAGE_PROD_URL)
        main_page.check_delivery_link()
        delivery_page = DeliveryPage(driver)
        result = delivery_page.get_page_title_text()
        assert result == "Варианты доставки", f"Expected 'Варианты доставки', but got '{result}'"
