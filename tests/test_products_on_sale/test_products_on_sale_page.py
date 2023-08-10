import time

import pytest
import allure
from tests.test_products_on_sale.constants_products_on_sale_page import *
from pages.products_on_sale_page import ProductsOnSale
from constants import MAIN_PAGE_STAGE_URL, MAIN_PAGE_PROD_URL


@allure.epic("Products On SalePage")
class TestProductsOnSalePage:

    @allure.title("positive_check_discount_displayed_for_unauthorized_customer_for_amount_0-49rub_smoke")
    @pytest.mark.parametrize('link', [f"{MAIN_PAGE_PROD_URL}{SHURUPY_PO_DEREVU_PAGE_URL}",
                                      f"{MAIN_PAGE_STAGE_URL}{SHURUPY_PO_DEREVU_PAGE_URL}"])
    @pytest.mark.smoke_test
    def test_positive_check_discount_for_unauthorized_customer_for_amount_0_49rub_smoke(self, driver, link):
        page = ProductsOnSale(driver)
        driver.get(link)
        page.get_field_price_first().send_keys(0)
        page.get_field_price_last().send_keys(49)
        page.get_in_stock_products_link().click()
        time.sleep(10)
        price = (float(page.get_pc_price().text[:-2]))
        page.get_add_to_cart_btn().click()
        page.get_header_cart_link_active().click()
        page.get_show_modal().click()
        page.get_name().send_keys(USER_NAME)
        page.get_phone().send_keys(USER_PHONE)
        page.get_email().send_keys(USER_EMAIL)
        page.get_checkout_to_step_2().click()
        total = (float(page.get_products_total().text[:-2]))
        assert price == total, "Поле 'Товары на сумму' не совпадает с ценой из первого шага"
        assert page.cant_get_field_sale(), "Есть поле 'Скидка'"

    @allure.title("positive_check_discount_displayed_for_unauthorized_customer_for_amount_10000_14999rub_smoke")
    @pytest.mark.parametrize('link', [f"{MAIN_PAGE_PROD_URL}{SHTUKATURNO_OTDELOCHNYJ_INSTRUMENT_PAGE_URL}",
                                      f"{MAIN_PAGE_STAGE_URL}{SHTUKATURNO_OTDELOCHNYJ_INSTRUMENT_PAGE_URL}"])
    @pytest.mark.smoke_test
    def test_positive_check_discount_for_unauthorized_customer_for_amount_10000_14999rub_smoke(self, driver, link):
        page = ProductsOnSale(driver)
        driver.get(link)
        page.get_field_price_first().send_keys(10000)
        page.get_field_price_last().send_keys(14999)
        page.get_in_stock_products_link().click()
        time.sleep(10)
        price = (float(page.get_pc_price().text[:-2].replace(' ', '')))
        page.get_add_to_cart_btn().click()
        page.get_header_cart_link_active().click()
        page.get_show_modal().click()
        page.get_name().send_keys(USER_NAME)
        page.get_phone().send_keys(USER_PHONE)
        page.get_email().send_keys(USER_EMAIL)
        page.get_checkout_to_step_2().click()
        total = (float(page.get_products_total().text[:-2].replace(' ', '')))
        discount = (float(page.get_discount_price().text[:-2].replace(' ', '')))
        assert total == round(price * 0.96, 2), "Стоимость товара не включает скидку 4%"
        assert discount == round(price * 0.04, 2), f"Скидка должна быть равна {round(price * 0.04, 2)}, а не {discount}"
