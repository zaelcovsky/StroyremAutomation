import time

import allure
import pytest

from constants import MAIN_PAGE_SANDBOX_TEST_URL
from .delivery_constants import (uroven_3000, bundeks_25, aksolit_30, fio, city, address_green_zone,
                                 form_phone, email, address_blue_zone, distance_km, address_red_zone, city_red_zone)
from pages.basket_page import BasketPage
from pages.item_page import ItemPage
from pages.ordering_page import OrderingPage


@allure.epic("Delivery Page - calculation")
@pytest.mark.parametrize('url', [MAIN_PAGE_SANDBOX_TEST_URL])
class TestDeliveryPageCalculation:
    @pytest.mark.parametrize('case_id, link_item, amount, weight, standard, in_time, all_time', [
        ("TD 001", uroven_3000, 1, 30, 0, 1590, 2190),
        ("TD 002", bundeks_25, 1, 30, 400, 1590, 2190),
        ("TD 003", aksolit_30, 8, 300, 400, 1590, 2190),
        ("TD 004", aksolit_30, 13, 400, 450, 1590, 2190),
        ("TD 005", aksolit_30, 16, 500, 600, 1590, 2190),
        ("TD 006", aksolit_30, 25, 1700, 990, 1990, 2480),
        ("TD 007", aksolit_30, 66, 2000, 1300, 2490, 2980),
        ("TD 008", aksolit_30, 149, 4500, 2300, 3980, 4490),
        ("TD 009", aksolit_30, 166, 5000, 2500, 4990, 5480),
        pytest.param(
            "TD 010", aksolit_30, 206, 6200, 2900, 5570, 6120,
            marks=pytest.mark.xfail(reson="Цена доставки 3600 7960 8980")
        ),
        ("TD 011", aksolit_30, 299, 9000, 3600, 7960, 8980),
        ("TD 012", aksolit_30, 333, 10000, 4450, 11990, 12500),
        pytest.param(
            "TD 013", aksolit_30, 366, 11000, 4800, 12450, 13480,
            marks=pytest.mark.xfail(reason="Цена стандартной доставки 4450")
        ),
        pytest.param(
            "TD 014", aksolit_30, 666, 20000, 5400, 15600, 17490,
            marks=pytest.mark.xfail(reason="Цена стандартной доставки 4450")
        )
    ])
    @pytest.mark.smoke
    def test_positive_delivery_green_zone_smoke(
            self, driver, url, case_id, link_item, amount, weight, standard, in_time, all_time
    ):

        driver.get(f'{url}{link_item}')
        item_page = ItemPage(driver)
        item_page.add_item_to_cart(amount).click_on_cart()

        cart_page = BasketPage(driver)
        price_items = cart_page.get_cart_total_price()
        weight_items = cart_page.get_weight()

        if price_items < 3000 and weight_items < 30:
            allure.dynamic.title(
                f"{case_id} Доставка товара весом до {weight}кг. и стоимостью до 3000р. в зеленой зоне"
            )
        elif price_items >= 3000 and weight_items < 30:
            allure.dynamic.title(
                f"{case_id} Доставка товара весом до {weight}кг. и стоимостью более 3000р. в зеленой зоне"
            )
        else:
            allure.dynamic.title(
                f"{case_id} Доставка товара весом до {weight}кг. в зеленой зоне"
            )

        cart_page.click_on_go_to_checkout()

        ordering_page = OrderingPage(driver)
        ordering_page.fill_fiz_name(fio).fill_fiz_phone(form_phone).fill_fiz_email(email).click_on_continue()
        ordering_page.fill_city(city)
        ordering_page.fill_street(address_green_zone)
        ordering_page.select_delivery('standard')
        time.sleep(2)

        standard_delivery_price = ordering_page.get_delivery_price('standard')
        standard_delivery_value = int(''.join(filter(str.isdigit, standard_delivery_price)))
        assert standard_delivery_value == standard, f'Стоимость стандартной доставки не соответствует расчетной:' \
                                                    f'\nТекущая цена: {standard_delivery_value}' \
                                                    f'\nОжидаемая цена: {standard}'

        delivery_in_time_price = ordering_page.select_delivery('in_time').get_delivery_price('in_time')
        delivery_in_time_value = int(''.join(filter(str.isdigit, delivery_in_time_price)))
        assert delivery_in_time_value == in_time, f'Стоимость доставки ко времени не соответствует расчетной:' \
                                                  f'\nТекущая цена: {delivery_in_time_value}' \
                                                  f'\nОжидаемая цена: {in_time}'

        delivery_all_time_price = ordering_page.select_delivery('all_time').get_delivery_price('all_time')
        delivery_all_time_value = int(''.join(filter(str.isdigit, delivery_all_time_price)))
        assert delivery_all_time_value == all_time, f'Стоимость круглосуточной доставки не соответствует расчетной:' \
                                                    f'\nТекущая цена: {delivery_all_time_value}' \
                                                    f'\nОжидаемая цена: {all_time}'

    @pytest.mark.parametrize('case_id, link_item, amount, weight, standard, in_time, all_time', [
        ("TD 015", bundeks_25, 1, 30, 650, 2390, 3320),
        pytest.param(
            "TD 016", aksolit_30, 8, 300, 650, 2390, 3320,
            marks=pytest.mark.xfail(reson="Цена доставки: - - -")
        ),
        ("TD 017", aksolit_30, 13, 400, 650, 2390, 3320),
        ("TD 018", aksolit_30, 16, 500, 850, 2490, 3320),
        ("TD 019", aksolit_30, 25, 1700, 1150, 2490, 3320),
        ("TD 020", aksolit_30, 66, 2000, 1500, 2990, 3650),
        ("TD 021", aksolit_30, 149, 4500, 2600, 4380, 4890),
        ("TD 022", aksolit_30, 166, 5000, 2800, 5490, 5980),
        pytest.param(
            "TD 023", aksolit_30, 206, 6200, 3300, 7500, 8000,
            marks=pytest.mark.xfail(reson="Цена доставки: 4300 9900 11440")
        ),
        ("TD 024", aksolit_30, 299, 9000, 4300, 9900, 11440),
        ("TD 025", aksolit_30, 333, 10000, 7000, 13900, 15900),
        pytest.param(
            "TD 026", aksolit_30, 366, 11000, 8000, 14900, 19900,
            marks=pytest.mark.xfail(reson="Цена доставки: 7000 13900 15900")
        ),
        pytest.param(
            "TD 027", aksolit_30, 666, 20000, 14000, 16900, 23900,
            marks=pytest.mark.xfail(reson="Цена доставки: 7000 13900 15900")
        )
    ])
    @pytest.mark.smoke
    def test_positive_delivery_blue_zone_smoke(
            self, driver, url, case_id, link_item, amount, weight, standard, in_time, all_time
    ):
        allure.dynamic.title(f"{case_id} Доставка товара весом до {weight}кг. в синей зоне")

        driver.get(f'{url}{link_item}')
        item_page = ItemPage(driver)
        item_page.add_item_to_cart(amount).click_on_cart()

        cart_page = BasketPage(driver)
        cart_page.click_on_go_to_checkout()

        ordering_page = OrderingPage(driver)
        ordering_page.fill_fiz_name(fio).fill_fiz_phone(form_phone).fill_fiz_email(email).click_on_continue()
        ordering_page.fill_city(city)
        ordering_page.fill_street(address_blue_zone)
        ordering_page.select_delivery('standard')
        time.sleep(2)

        standard_delivery_price = ordering_page.get_delivery_price('standard')
        standard_delivery_value = int(''.join(filter(str.isdigit, standard_delivery_price)))
        assert standard_delivery_value == standard, f'Стоимость стандартной доставки не соответствует расчетной:' \
                                                    f'\nТекущая цена: {standard_delivery_value}' \
                                                    f'\nОжидаемая цена: {standard}'

        delivery_in_time_price = ordering_page.select_delivery('in_time').get_delivery_price('in_time')
        delivery_in_time_value = int(''.join(filter(str.isdigit, delivery_in_time_price)))
        assert delivery_in_time_value == in_time, f'Стоимость доставки ко времени не соответствует расчетной:' \
                                                  f'\nТекущая цена: {delivery_in_time_value}' \
                                                  f'\nОжидаемая цена: {in_time}'

        delivery_all_time_price = ordering_page.select_delivery('all_time').get_delivery_price('all_time')
        delivery_all_time_value = int(''.join(filter(str.isdigit, delivery_all_time_price)))
        assert delivery_all_time_value == all_time, f'Стоимость круглосуточной доставки не соответствует расчетной:' \
                                                    f'\nТекущая цена: {delivery_all_time_value}' \
                                                    f'\nОжидаемая цена: {all_time}'
