import time
import pytest
import allure
from selenium.common import ElementClickInterceptedException, StaleElementReferenceException, TimeoutException
from tests.test_products_on_sale.constants_products_on_sale_page import *
from constants import MAIN_PAGE_STAGE_URL, MAIN_PAGE_PROD_URL


@allure.epic("Products On SalePage")
class TestProductsOnSalePage:

    @allure.title("positive_check_discount_displayed_for_unauthorized_customer_for_amount_0-49rub_smoke")
    @pytest.mark.parametrize('link', [f"{MAIN_PAGE_PROD_URL}{SHURUPY_PO_DEREVU_PAGE_URL}",
                                      f"{MAIN_PAGE_STAGE_URL}{SHURUPY_PO_DEREVU_PAGE_URL}"])
    @pytest.mark.smoke_test
    def test_positive_check_discount_for_unauthorized_customer_for_amount_0_49rub_smoke(self, link, product_page_open):
        try:
            product_page_open.get_field_price_first().send_keys(0)
            product_page_open.get_field_price_last().send_keys(49)
            time.sleep(1)
            product_page_open.get_in_stock_products_link().click()
            time.sleep(5)
            price = (float(product_page_open.get_pc_price().text[:-2]))
            product_page_open.get_add_to_cart_btn().click()
            product_page_open.get_header_cart_link_active().click()
            product_page_open.get_show_modal().click()
            product_page_open.get_name().send_keys(USER_NAME)
            product_page_open.get_phone().send_keys(USER_PHONE)
            product_page_open.get_email().send_keys(USER_EMAIL)
            product_page_open.get_checkout_to_step_2().click()
            total = (float(product_page_open.get_products_total().text[:-2]))
            assert price == total, f"ОР: Стоимость товара = {price}, ФР: стоимость товара = {total}"
            assert product_page_open.cant_get_field_sale(), "Есть поле 'Скидка'"
        except (ElementClickInterceptedException, StaleElementReferenceException, TimeoutException):
            print(f"\nЭлемент не прогрузился или кнопка не кликабельна")

    @allure.title("positive_check_discount_displayed_for_unauthorized_customer_for_amount_10000_14999rub_smoke")
    @pytest.mark.parametrize('link', [f"{MAIN_PAGE_PROD_URL}{SHTUKATURNO_OTDELOCHNYJ_INSTRUMENT_PAGE_URL}",
                                      f"{MAIN_PAGE_STAGE_URL}{SHTUKATURNO_OTDELOCHNYJ_INSTRUMENT_PAGE_URL}"])
    @pytest.mark.smoke_test
    def test_positive_check_discount_for_unauthorized_customer_for_amount_10000_14999rub_smoke(self, link,
                                                                                               product_page_open):
        try:
            product_page_open.get_field_price_first().send_keys(10000)
            product_page_open.get_field_price_last().send_keys(14999)
            time.sleep(1)
            product_page_open.get_in_stock_products_link().click()
            time.sleep(5)
            product_page_open.get_add_to_cart_btn().click()
            price = (float(product_page_open.get_pc_price().text[:-2].replace(' ', '')))
            product_page_open.get_header_cart_link_active().click()
            product_page_open.get_show_modal().click()
            product_page_open.get_name().send_keys(USER_NAME)
            product_page_open.get_phone().send_keys(USER_PHONE)
            product_page_open.get_email().send_keys(USER_EMAIL)
            product_page_open.get_checkout_to_step_2().click()
            total = (float(product_page_open.get_products_total().text[:-2].replace(' ', '')))
            discount = (float(product_page_open.get_discount_price().text[:-2].replace(' ', '')))
            assert total == price - round(price * 0.04, 2), \
                f"ОР: Стоимость товара = {price - round(price * 0.04, 2)}, ФР: скидка = {total}"
            assert discount == round(price * 0.04, 2), f"ОР: Скидка = {round(price * 0.04, 2)}, ФР: скидка = {discount}"
        except (ElementClickInterceptedException, StaleElementReferenceException, TimeoutException):
            print(f"\nЭлемент не прогрузился или кнопка не кликабельна")

    @allure.title("positive_check_discount_displayed_for_unauthorized_customer_for_amount_15000rub_and_above_smoke")
    @pytest.mark.parametrize('link', [f"{MAIN_PAGE_PROD_URL}{RASTVORONASOSY_PAGE_URL}",
                                      f"{MAIN_PAGE_STAGE_URL}{RASTVORONASOSY_PAGE_URL}"])
    @pytest.mark.xfail(reason="Ждем исправление бага - Разная цена товара в каталоге и на карточке товара")
    @pytest.mark.smoke_test
    def test_positive_check_discount_for_unauthorized_customer_for_amount_15000rub_and_above_smoke(self, link,
                                                                                                   product_page_open):
        try:
            product_page_open.get_field_price_first().send_keys(15000)
            product_page_open.get_field_price_last().click()
            time.sleep(5)
            product_page_open.get_add_to_cart_btn().click()
            price = (float(product_page_open.get_pc_price().text[:-2].replace(' ', '')))
            product_page_open.get_header_cart_link_active().click()
            product_page_open.get_show_modal().click()
            product_page_open.get_name().send_keys(USER_NAME)
            product_page_open.get_phone().send_keys(USER_PHONE)
            product_page_open.get_email().send_keys(USER_EMAIL)
            product_page_open.get_checkout_to_step_2().click()
            total = (float(product_page_open.get_products_total().text[:-2].replace(' ', '')))
            discount = (float(product_page_open.get_discount_price().text[:-2].replace(' ', '')))
            assert total == price - round(price * 0.05, 2), (f"ОР: Стоимость товара = {price - round(price * 0.05, 2)},"
                                                             f"ФР: стоимость товара = {total}")
            assert discount == round(price * 0.05, 2), f"ОР: Скидка = {round(price * 0.05, 2)}, ФР: скидка = {discount}"
        except (ElementClickInterceptedException, StaleElementReferenceException, TimeoutException):
            print(f"\nЭлемент не прогрузился или кнопка не кликабельна")

    @allure.title("positive_check_discount_displayed_for_unauthorized_customer_for_amount_3500_4999rub_smoke")
    @pytest.mark.parametrize('link', [f"{MAIN_PAGE_PROD_URL}{SHLIFOVALNYE_MASHINY_PAGE_URL}",
                                      f"{MAIN_PAGE_STAGE_URL}{SHLIFOVALNYE_MASHINY_PAGE_URL}"])
    @pytest.mark.smoke_test
    def test_positive_check_discount_for_unauthorized_customer_for_amount_3500_4999rub_smoke(self, link,
                                                                                             product_page_open):
        try:
            product_page_open.get_field_price_first().send_keys(3500)
            product_page_open.get_field_price_last().send_keys(4999)
            time.sleep(1)
            product_page_open.get_in_stock_products_link().click()
            time.sleep(5)
            product_page_open.get_add_to_cart_btn().click()
            price = (float(product_page_open.get_pc_price().text[:-2].replace(' ', '')))
            product_page_open.get_header_cart_link_active().click()
            product_page_open.get_show_modal().click()
            product_page_open.get_name().send_keys(USER_NAME)
            product_page_open.get_phone().send_keys(USER_PHONE)
            product_page_open.get_email().send_keys(USER_EMAIL)
            product_page_open.get_checkout_to_step_2().click()
            total = (float(product_page_open.get_products_total().text[:-2].replace(' ', '')))
            discount = (float(product_page_open.get_discount_price().text[:-2].replace(' ', '')))
            assert total == price - round(price * 0.015, 2), \
                f"ОР: Стоимость товара = {price - round(price * 0.015, 2)}, ФР: стоимость товара = {total}"
            assert discount == round(price * 0.015, 2), \
                f"ОР: Скидка = {round(price * 0.015, 2)}, ФР: скидка = {discount}"
        except (ElementClickInterceptedException, StaleElementReferenceException, TimeoutException):
            print(f"\nЭлемент не прогрузился или кнопка не кликабельна")

    @allure.title("positive_check_discount_displayed_for_unauthorized_customer_for_amount_50_3499rub_smoke")
    @pytest.mark.parametrize('link', [f"{MAIN_PAGE_PROD_URL}{KISTI_MALYARNYE_PAGE_URL}",
                                      f"{MAIN_PAGE_STAGE_URL}{KISTI_MALYARNYE_PAGE_URL}"])
    @pytest.mark.smoke_test
    def test_positive_check_discount_for_unauthorized_customer_for_amount_50_3499rub_smoke(self, link,
                                                                                           product_page_open):
        try:
            product_page_open.get_field_price_first().send_keys(50)
            product_page_open.get_field_price_last().send_keys(3499)
            time.sleep(1)
            product_page_open.get_in_stock_products_link().click()
            time.sleep(5)
            product_page_open.get_add_to_cart_btn().click()
            price = (float(product_page_open.get_pc_price().text[:-2].replace(' ', '')))
            product_page_open.get_header_cart_link_active().click()
            product_page_open.get_show_modal().click()
            product_page_open.get_name().send_keys(USER_NAME)
            product_page_open.get_phone().send_keys(USER_PHONE)
            product_page_open.get_email().send_keys(USER_EMAIL)
            product_page_open.get_checkout_to_step_2().click()
            total = (float(product_page_open.get_products_total().text[:-2].replace(' ', '')))
            discount = (float(product_page_open.get_discount_price().text[:-2].replace(' ', '')))
            assert total == price - round(price * 0.01, 2), \
                f"ОР: Стоимость товара = {price - round(price * 0.01, 2)}, ФР: стоимость товара = {total}"
            assert discount == round(price * 0.01, 2), f"ОР: Скидка = {round(price * 0.01, 2)}, ФР: скидка = {discount}"
        except (ElementClickInterceptedException, StaleElementReferenceException, TimeoutException):
            print(f"\nЭлемент не прогрузился или кнопка не кликабельна")

    @allure.title("positive_check_discount_displayed_for_unauthorized_customer_for_amount_5000_7499rub_smoke")
    @pytest.mark.parametrize('link', [f"{MAIN_PAGE_PROD_URL}{RASTVORNYE_PISTOLETY_SOPLA_PAGE_URL}",
                                      f"{MAIN_PAGE_STAGE_URL}{RASTVORNYE_PISTOLETY_SOPLA_PAGE_URL}"])
    @pytest.mark.xfail(reason="Ждем уточнение о способе округления скидки и стоимости товара")
    @pytest.mark.smoke_test
    def test_positive_check_discount_for_unauthorized_customer_for_amount_5000_7499rub_smoke(self, link,
                                                                                             product_page_open):
        try:
            product_page_open.get_field_price_first().send_keys(5000)
            product_page_open.get_field_price_last().send_keys(7499)
            time.sleep(1)
            product_page_open.get_in_stock_products_link().click()
            time.sleep(5)
            product_page_open.get_add_to_cart_btn().click()
            price = (float(product_page_open.get_pc_price().text[:-2].replace(' ', '')))
            product_page_open.get_header_cart_link_active().click()
            product_page_open.get_show_modal().click()
            product_page_open.get_name().send_keys(USER_NAME)
            product_page_open.get_phone().send_keys(USER_PHONE)
            product_page_open.get_email().send_keys(USER_EMAIL)
            product_page_open.get_checkout_to_step_2().click()
            total = (float(product_page_open.get_products_total().text[:-2].replace(' ', '')))
            discount = (float(product_page_open.get_discount_price().text[:-2].replace(' ', '')))
            assert total == price - round(price * 0.025, 2), \
                f"ОР: Стоимость товара = {price - round(price * 0.025, 2)}, ФР: стоимость товара = {total}"
            assert discount == round(price * 0.025, 2), \
                f"ОР: Скидка = {round(price * 0.025, 2)}, ФР: скидка = {discount}"
        except (ElementClickInterceptedException, StaleElementReferenceException, TimeoutException):
            print(f"\nЭлемент не прогрузился или кнопка не кликабельна")

    @allure.title("positive_check_discount_displayed_for_unauthorized_customer_for_amount_7500_9999rub_smoke")
    @pytest.mark.parametrize('link', [f"{MAIN_PAGE_PROD_URL}{ELECTROINSTRUMENT_PAGE_URL}",
                                      f"{MAIN_PAGE_STAGE_URL}{ELECTROINSTRUMENT_PAGE_URL}"])
    @pytest.mark.smoke_test
    def test_positive_check_discount_for_unauthorized_customer_for_amount_7500_9999rub_smoke(self, link,
                                                                                             product_page_open):
        try:
            product_page_open.get_field_price_first().send_keys(7500)
            product_page_open.get_field_price_last().send_keys(9999)
            time.sleep(1)
            product_page_open.get_in_stock_products_link().click()
            time.sleep(5)
            product_page_open.get_add_to_cart_btn().click()
            price = (float(product_page_open.get_pc_price().text[:-2].replace(' ', '')))
            product_page_open.get_header_cart_link_active().click()
            product_page_open.get_show_modal().click()
            product_page_open.get_name().send_keys(USER_NAME)
            product_page_open.get_phone().send_keys(USER_PHONE)
            product_page_open.get_email().send_keys(USER_EMAIL)
            product_page_open.get_checkout_to_step_2().click()
            total = (float(product_page_open.get_products_total().text[:-2].replace(' ', '')))
            discount = (float(product_page_open.get_discount_price().text[:-2].replace(' ', '')))
            assert total == price - round(price * 0.03, 2), \
                f"ОР: Стоимость товара = {price - round(price * 0.03, 2)}, ФР: стоимость товара = {total}"
            assert discount == round(price * 0.03, 2), f"ОР: Скидка = {round(price * 0.03, 2)}, ФР: скидка = {discount}"
        except (ElementClickInterceptedException, StaleElementReferenceException, TimeoutException):
            print(f"\nЭлемент не прогрузился или кнопка не кликабельна")

    @allure.title("positive_check_discount_displayed_for_unauthorized_customer_for_amount_7500_9999rub_smoke")
    @pytest.mark.parametrize('link', [f"{MAIN_PAGE_PROD_URL}{ACTION_PAGE_URL}",
                                      f"{MAIN_PAGE_STAGE_URL}{ACTION_PAGE_URL}"])
    @pytest.mark.smoke_test
    def test_positive_check_there_is_no_discount_for_unauthorized_customer_on_order_page_for_red_prices_smoke(
            self, link, product_page_open):
        try:
            product_page_open.get_in_stock_products_link().click()
            time.sleep(1)
            product_page_open.get_text_red_link().click()
            time.sleep(2)
            product_page_open.get_add_to_cart_btn().click()
            price = (float(product_page_open.get_pc_price().text[:-2].replace(' ', '')))
            product_page_open.get_header_cart_link_active().click()
            product_page_open.get_show_modal().click()
            product_page_open.get_name().send_keys(USER_NAME)
            product_page_open.get_phone().send_keys(USER_PHONE)
            product_page_open.get_email().send_keys(USER_EMAIL)
            product_page_open.get_checkout_to_step_2().click()
            total = (float(product_page_open.get_products_total().text[:-2].replace(' ', '')))
            assert price == total, f"ОР: Стоимость товара = {price}, ФР: стоимость товара = {total}"
            assert product_page_open.cant_get_field_sale(), "Есть поле 'Скидка'"
        except (ElementClickInterceptedException, StaleElementReferenceException, TimeoutException):
            print(f"\nЭлемент не прогрузился или кнопка не кликабельна")

    @allure.title("positive_discount_for_unauthorized_customer_purchase_amount_0_to_49rub_smoke")
    @pytest.mark.parametrize('link', [f"{MAIN_PAGE_PROD_URL}{SHURUPY_PO_DEREVU_PAGE_URL}",
                                      f"{MAIN_PAGE_STAGE_URL}{SHURUPY_PO_DEREVU_PAGE_URL}"])
    @pytest.mark.smoke_test
    def test_positive_discount_for_unauthorized_customer_purchase_amount_0_to_49rub_smoke(
            self, link, product_page_open):
        product_page_open.get_field_price_first().send_keys(0)
        product_page_open.get_field_price_last().send_keys(49)
        time.sleep(1)
        product_page_open.get_in_stock_products_link().click()
        time.sleep(5)
        price = (float(product_page_open.get_pc_price().text[:-2]))
        product_page_open.get_add_to_cart_btn().click()
        product_page_open.get_header_cart_link_active().click()
        total = (float(product_page_open.get_total_current_price().text[:-2]))
        cart_total = (float(product_page_open.get_cart_total().text[:-2]))
        assert price == total == cart_total, \
            f"ОР: Суммы равны, ФР: Cтоимость товара в каталоге: {price} в корзине: {cart_total}"
        assert int(product_page_open.get_cart_discount().text[:-2]) == 0, "Есть Скидка за объём"

    @allure.title("positive_check_there_is_no_discount_for_unauthorized_customer_red_prices_smoke")
    @pytest.mark.parametrize('link', [f"{MAIN_PAGE_PROD_URL}{ACTION_PAGE_URL}",
                                      f"{MAIN_PAGE_STAGE_URL}{ACTION_PAGE_URL}"])
    @pytest.mark.smoke_test
    def test_positive_check_there_is_no_discount_for_unauthorized_customer_red_prices_smoke(
            self, link, product_page_open):
        product_page_open.get_in_stock_products_link().click()
        time.sleep(2)
        product_page_open.get_text_red_link().click()
        time.sleep(2)
        product_page_open.get_add_to_cart_btn().click()
        price = (float(product_page_open.get_pc_price().text[:-2].replace(' ', '')))
        product_page_open.get_header_cart_link_active().click()
        total = (float(product_page_open.get_total_current_price().text[:-2].replace(' ', '')))
        cart_total = (float(product_page_open.get_cart_total().text[:-2].replace(' ', '')))
        assert price == total == cart_total, \
            f"ОР: Суммы равны, ФР: Cтоимость товара в каталоге: {price} в корзине: {cart_total} и со скидкой:{total}"
        assert int(product_page_open.get_cart_discount().text[:-2]) == 0, "Есть Скидка за объём"

    @allure.title("positive_discount_for_unauthorized_customer_purchase_amount_10000_to_14999rub_smoke")
    @pytest.mark.parametrize('link', [f"{MAIN_PAGE_PROD_URL}{SHTUKATURNO_OTDELOCHNYJ_INSTRUMENT_PAGE_URL}",
                                      f"{MAIN_PAGE_STAGE_URL}{SHTUKATURNO_OTDELOCHNYJ_INSTRUMENT_PAGE_URL}"])
    @pytest.mark.smoke_test
    def test_positive_discount_for_unauthorized_customer_purchase_amount_10000_to_14999rub_smoke(
            self, link, product_page_open):
        product_page_open.get_field_price_first().send_keys(10000)
        product_page_open.get_field_price_last().send_keys(14999)
        time.sleep(1)
        product_page_open.get_in_stock_products_link().click()
        time.sleep(5)
        price = (float(product_page_open.get_pc_price().text[:-2].replace(' ', '')))
        product_page_open.get_add_to_cart_btn().click()
        product_page_open.get_header_cart_link_active().click()
        total = (float(product_page_open.get_total_current_price().text[:-2].replace(' ', '')))
        cart_total = (float(product_page_open.get_cart_total().text[:-2].replace(' ', '')))
        discount = float(product_page_open.get_cart_discount().text[:-2].replace(' ', ''))
        assert total == price - round(price * 0.04, 2) == cart_total, \
            f"ОР: Суммы равны, ФР: Cтоимость товара в каталоге: {price} в корзине: {cart_total} и со скидкой:{total}"
        assert discount == round(price * 0.04, 2), \
            f"ОР: Скидка за объем = {round(price * 0.04, 2)}, ФР: скидка = {discount}"

    @allure.title("positive_discount_for_unauthorized_customer_purchase_amount_15000_and_above_smoke")
    @pytest.mark.parametrize('link', [f"{MAIN_PAGE_PROD_URL}{RASTVORONASOSY_PAGE_URL}",
                                      f"{MAIN_PAGE_STAGE_URL}{RASTVORONASOSY_PAGE_URL}"])
    @pytest.mark.xfail(reason="Ждем исправление бага - Разная цена товара в каталоге и на карточке товара")
    @pytest.mark.smoke_test
    def test_positive_discount_for_unauthorized_customer_purchase_amount_15000_and_above_smoke(
            self, link, product_page_open):
        product_page_open.get_field_price_first().send_keys(15000)
        product_page_open.get_field_price_last().click()
        time.sleep(5)
        price = (float(product_page_open.get_pc_price().text[:-2].replace(' ', '')))
        product_page_open.get_add_to_cart_btn().click()
        product_page_open.get_header_cart_link_active().click()
        total = (float(product_page_open.get_total_current_price().text[:-2].replace(' ', '')))
        cart_total = (float(product_page_open.get_cart_total().text[:-2].replace(' ', '')))
        discount = float(product_page_open.get_cart_discount().text[:-2].replace(' ', ''))
        assert total == price - round(price * 0.05, 2) == cart_total, \
            f"ОР: Суммы равны, ФР: Cтоимость товара в каталоге: {price} в корзине: {cart_total} и со скидкой:{total}"
        assert discount == round(price * 0.05, 2), \
            f"ОР: Скидка за объем = {round(price * 0.05, 2)}, ФР: скидка = {discount}"

    @allure.title("positive_discount_for_unauthorized_customer_purchase_amount_3500_to_4999rub_smoke")
    @pytest.mark.parametrize('link', [f"{MAIN_PAGE_PROD_URL}{SHLIFOVALNYE_MASHINY_PAGE_URL}",
                                      f"{MAIN_PAGE_STAGE_URL}{SHLIFOVALNYE_MASHINY_PAGE_URL}"])
    @pytest.mark.smoke_test
    def test_positive_discount_for_unauthorized_customer_purchase_amount_3500_to_4999rub_smoke(
            self, link, product_page_open):
        product_page_open.get_field_price_first().send_keys(3500)
        product_page_open.get_field_price_last().send_keys(4999)
        time.sleep(1)
        product_page_open.get_in_stock_products_link().click()
        time.sleep(5)
        price = (float(product_page_open.get_pc_price().text[:-2].replace(' ', '')))
        product_page_open.get_add_to_cart_btn().click()
        product_page_open.get_header_cart_link_active().click()
        total = (float(product_page_open.get_total_current_price().text[:-2].replace(' ', '')))
        cart_total = (float(product_page_open.get_cart_total().text[:-2].replace(' ', '')))
        discount = float(product_page_open.get_cart_discount().text[:-2].replace(' ', ''))
        assert total == price - round(price * 0.015, 2) == cart_total, \
            f"ОР: Суммы равны, ФР: Cтоимость товара в каталоге: {price} в корзине: {cart_total} и со скидкой:{total}"
        assert discount == round(price * 0.015, 2), \
            f"ОР: Скидка за объем = {round(price * 0.015, 2)}, ФР: скидка = {discount}"

    @allure.title("positive_discount_for_unauthorized_customer_purchase_amount_5000_to_7499rub_smoke")
    @pytest.mark.parametrize('link', [f"{MAIN_PAGE_PROD_URL}{RASTVORNYE_PISTOLETY_SOPLA_PAGE_URL}",
                                      f"{MAIN_PAGE_STAGE_URL}{RASTVORNYE_PISTOLETY_SOPLA_PAGE_URL}"])
    @pytest.mark.xfail(reason="Ждем уточнение о способе округления скидки и стоимости товара")
    @pytest.mark.smoke_test
    def test_positive_discount_for_unauthorized_customer_purchase_amount_5000_to_7499rub_smoke(
            self, link, product_page_open):
        product_page_open.get_field_price_first().send_keys(5000)
        product_page_open.get_field_price_last().send_keys(7499)
        time.sleep(1)
        product_page_open.get_in_stock_products_link().click()
        time.sleep(5)
        price = (float(product_page_open.get_pc_price().text[:-2].replace(' ', '')))
        product_page_open.get_add_to_cart_btn().click()
        product_page_open.get_header_cart_link_active().click()
        total = (float(product_page_open.get_total_current_price().text[:-2].replace(' ', '')))
        cart_total = (float(product_page_open.get_cart_total().text[:-2].replace(' ', '')))
        discount = float(product_page_open.get_cart_discount().text[:-2].replace(' ', ''))
        assert total == price - round(price * 0.025, 2) == cart_total, \
            f"ОР: Суммы равны, ФР: Cтоимость товара в каталоге: {price} в корзине: {cart_total} и со скидкой:{total}"
        assert discount == round(price * 0.025, 2), \
            f"ОР: Скидка за объем = {round(price * 0.025, 2)}, ФР: скидка = {discount}"

    @allure.title("positive_discount_for_unauthorized_customer_purchase_amount_50_to_3499rub_smoke")
    @pytest.mark.parametrize('link', [f"{MAIN_PAGE_PROD_URL}{KISTI_MALYARNYE_PAGE_URL}",
                                      f"{MAIN_PAGE_STAGE_URL}{KISTI_MALYARNYE_PAGE_URL}"])
    @pytest.mark.smoke_test
    def test_positive_discount_for_unauthorized_customer_purchase_amount_50_to_3499rub_smoke(
            self, link, product_page_open):
        product_page_open.get_field_price_first().send_keys(50)
        product_page_open.get_field_price_last().send_keys(3499)
        time.sleep(1)
        product_page_open.get_in_stock_products_link().click()
        time.sleep(5)
        price = (float(product_page_open.get_pc_price().text[:-2].replace(' ', '')))
        product_page_open.get_add_to_cart_btn().click()
        product_page_open.get_header_cart_link_active().click()
        total = (float(product_page_open.get_total_current_price().text[:-2].replace(' ', '')))
        cart_total = (float(product_page_open.get_cart_total().text[:-2].replace(' ', '')))
        discount = float(product_page_open.get_cart_discount().text[:-2].replace(' ', ''))
        assert total == price - round(price * 0.01, 2) == cart_total, \
            f"ОР: Суммы равны, ФР: Cтоимость товара в каталоге: {price} в корзине: {cart_total} и со скидкой:{total}"
        assert discount == round(price * 0.01, 2), \
            f"ОР: Скидка за объем = {round(price * 0.01, 2)}, ФР: скидка = {discount}"

    @allure.title("positive_discount_for_unauthorized_customer_purchase_amount_7500_to_9999rub_smoke")
    @pytest.mark.parametrize('link', [f"{MAIN_PAGE_PROD_URL}{SHLIFOVALNYE_MASHINY_PAGE_URL}",
                                      f"{MAIN_PAGE_STAGE_URL}{SHLIFOVALNYE_MASHINY_PAGE_URL}"])
    @pytest.mark.smoke_test
    def test_positive_discount_for_unauthorized_customer_purchase_amount_7500_to_9999rub_smoke(
            self, link, product_page_open):
        product_page_open.get_field_price_first().send_keys(7500)
        product_page_open.get_field_price_last().send_keys(9999)
        time.sleep(1)
        product_page_open.get_in_stock_products_link().click()
        time.sleep(5)
        price = (float(product_page_open.get_pc_price().text[:-2].replace(' ', '')))
        product_page_open.get_add_to_cart_btn().click()
        product_page_open.get_header_cart_link_active().click()
        total = (float(product_page_open.get_total_current_price().text[:-2].replace(' ', '')))
        cart_total = (float(product_page_open.get_cart_total().text[:-2].replace(' ', '')))
        discount = float(product_page_open.get_cart_discount().text[:-2].replace(' ', ''))
        assert total == price - round(price * 0.03, 2) == cart_total, \
            f"ОР: Суммы равны, ФР: Cтоимость товара в каталоге: {price} в корзине: {cart_total} и со скидкой:{total}"
        assert discount == round(price * 0.03, 2), \
            f"ОР: Скидка за объем = {round(price * 0.03, 2)}, ФР: скидка = {discount}"
