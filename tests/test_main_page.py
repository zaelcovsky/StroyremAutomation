import pytest
import allure

from pages import catalog_page
from pages.articles_page import ArticlesPage
from pages.catalog_page import CatalogPage
from pages.location_page import LocationPage
from pages.delivery_page import DeliveryPage
from pages.lifting_page import LiftingPage
from pages.main_page import MainPage
from constants import MAIN_PAGE_STAGE_URL, MAIN_PAGE_TITLE, ARTICLES_PAGE_URL, MAIN_PAGE_PROD_URL, LIFTING_PAGE_URL, \
    LOCATION_PAGE_URL, NEW_IN_STOCK_PAGE_URL, PRICE_PAGE_URL, REVIEWS_PAGE_URL, SHARES_PAGE_URL


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

    @allure.feature("Header functionality")
    @allure.title("TC 003 - Функционал кнопоки 'Корзина' в шапке главной страницы")
    @pytest.mark.smoke_test
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

    @allure.feature("Footer functionality")
    @allure.title("TC 006 - Проверка функциональности ссылки 'Обратный звонок' в футере")
    @pytest.mark.smoke_test
    def test_positive_footer_back_call_smoke(self, driver):
        main_page = MainPage(driver)
        driver.get(MAIN_PAGE_PROD_URL)
        result = main_page.check_call_back_link()
        assert result == "Заказать обратный звонок", f"Ожидалось 'Заказать обратный звонок', но получено '{result}'"

    @allure.feature("Footer functionality")
    @allure.title("TC 007 - Проверка функциональности ссылки 'Строительные советы' в футере")
    @pytest.mark.smoke_test
    def test_positive_footer_building_advices_smoke(self, driver):
        main_page = MainPage(driver)
        articles_page = ArticlesPage(driver)
        driver.get(MAIN_PAGE_PROD_URL)
        main_page.check_building_tips_link()
        assert driver.current_url == ARTICLES_PAGE_URL, "URL после перенаправления некорректен"
        assert articles_page.get_page_title_text() == "Советы", "Заголовок страницы не верен"

    @allure.feature("Footer functionality")
    @allure.title("TC 008 - Проверка функциональности ссылки 'Каталог товаров' в футере")
    @pytest.mark.smoke_test
    def test_positive_footer_catalog_smoke(self, driver):
        main_page = MainPage(driver)
        driver.get(MAIN_PAGE_PROD_URL)
        is_displayed, header_text = main_page.check_product_catalog_link()
        assert is_displayed, "Каталог товаров не отображается"
        assert header_text == "Каталог", f"Ожидалось 'Каталог', но получено '{header_text}'"

    @allure.feature("Footer functionality")
    @allure.title("TC 009 - Проверка функциональности ссылки 'Доставка' в футере")
    @pytest.mark.smoke_test
    def test_positive_footer_delivery_smoke(self, driver):
        main_page = MainPage(driver)
        driver.get(MAIN_PAGE_PROD_URL)
        main_page.check_delivery_link()
        delivery_page = DeliveryPage(driver)
        result = delivery_page.get_page_title_text()
        assert result == "Варианты доставки", f"Ожидалось 'Варианты доставки', но получено '{result}'"

    @allure.feature("Footer functionality")
    @pytest.mark.xfail(reason="Попап не реализован")
    @allure.title("TC 010 - Проверка функциональности ссылки 'email' в футере")
    @pytest.mark.smoke_test
    def test_positive_footer_email_smoke(self, driver):
        main_page = MainPage(driver)
        driver.get(MAIN_PAGE_PROD_URL)
        main_page.check_email_link()

    @allure.feature("Footer functionality")
    @allure.title("TC 011 - Проверка функциональности ссылки 'Подъем на этаж'")
    @pytest.mark.smoke_test
    def test_positive_footer_lifting_smoke(self, driver):
        main_page = MainPage(driver)
        lifting_page = LiftingPage(driver)
        driver.get(MAIN_PAGE_PROD_URL)
        main_page.check_floor_climb_link()
        assert driver.current_url == LIFTING_PAGE_URL, "URL после перенаправления некорректен"
        assert lifting_page.get_page_title_text() == \
            "Расценки на подъём и разгрузку товара", "Заголовок страницы не верен"

    @allure.feature("Footer functionality")
    @allure.title("TC 012 - Проверка функциональности ссылки 'Местоположение'")
    @pytest.mark.smoke_test
    def test_positive_footer_location_smoke(self, driver):
        main_page = MainPage(driver)
        location_page = LocationPage(driver)
        driver.get(MAIN_PAGE_PROD_URL)
        main_page.check_location_link()
        assert driver.current_url == LOCATION_PAGE_URL, "URL после перенаправления некорректен"
        assert location_page.get_page_title_text() == "Адрес", "Заголовок страницы не верен"

    @allure.feature("Footer functionality")
    @allure.title("TC 013 - Проверка функциональности ссылки 'Новинки'")
    @pytest.mark.smoke_test
    def test_positive_footer_new_in_stock_smoke(self, driver):
        main_page = MainPage(driver)
        catalog_page = CatalogPage(driver)
        driver.get(MAIN_PAGE_PROD_URL)
        main_page.check_new_in_stock_link()
        assert driver.current_url == NEW_IN_STOCK_PAGE_URL, "URL после перенаправления некорректен"
        assert catalog_page.get_page_title_text() == "Новинки", "Заголовок страницы не верен"

    @allure.feature("Footer functionality")
    @allure.title("TC 014 - Проверка функциональности ссылки 'Оплатить заказ'")
    @pytest.mark.smoke_test
    def test_positive_footer_payment_order_smoke(self, driver):
        main_page = MainPage(driver)
        driver.get(MAIN_PAGE_PROD_URL)
        title = main_page.check_payment_order_link()
        assert title == 'Оплата заказа', f"Ожидалось 'Оплата заказа', но получено '{title}'"

    @allure.feature("Footer functionality")
    @pytest.mark.xfail(reason="Попап не реализован")
    @allure.title("TC 015 - Проверка функциональности ссылки 'telephone number'")
    @pytest.mark.smoke_test
    def test_positive_footer_phone_number_smoke(self, driver):
        main_page = MainPage(driver)
        driver.get(MAIN_PAGE_PROD_URL)
        main_page.check_telephone_number_link()

    @allure.feature("Footer functionality")
    @pytest.mark.xfail(reason="При переходе на страницу выдает 404 ошибку")
    @allure.title("TC 016 - Проверка функциональности ссылки 'Прайс'")
    @pytest.mark.smoke_test
    def test_positive_footer_price_smoke(self, driver):
        main_page = MainPage(driver)
        driver.get(MAIN_PAGE_PROD_URL)
        main_page.check_price_link()
        assert driver.current_url == PRICE_PAGE_URL, "URL после перенаправления некорректен"

    @allure.feature("Footer functionality")
    @allure.title("TC 017 - Проверка функциональности ссылки 'Отзывы'")
    @pytest.mark.smoke_test
    def test_positive_footer_reviews_smoke(self, driver):
        main_page = MainPage(driver)
        driver.get(MAIN_PAGE_PROD_URL)
        main_page.check_reviews_link()
        assert driver.current_url == REVIEWS_PAGE_URL, "URL после перенаправления некорректен"

    @allure.feature("Footer functionality")
    @allure.title("TC 018 - Проверка функциональности ссылки 'Отзывы'")
    @pytest.mark.smoke_test
    def test_positive_footer_sale_smoke(self, driver):
        main_page = MainPage(driver)
        driver.get(MAIN_PAGE_PROD_URL)
        main_page.check_shares_link()
        assert driver.current_url == SHARES_PAGE_URL, "URL после перенаправления некорректен"
