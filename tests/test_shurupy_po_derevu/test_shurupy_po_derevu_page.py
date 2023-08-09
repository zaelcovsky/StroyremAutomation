import pytest
import allure
from tests.test_shurupy_po_derevu.constants_shurupy_po_derevu_page import *
from pages.shurupy_po_derevu_page import ShurupyPoDerevuPage
from constants import MAIN_PAGE_STAGE_URL, MAIN_PAGE_PROD_URL


@allure.epic("Shurupy Po Derevu Page")
class TestShurupyPoDerevuPage:

    @allure.title("positive_check_discount_displayed_on_Order_page_for_unauthorized_customer_for_amount_0-49rub_smoke")
    @pytest.mark.parametrize('link', [f"{MAIN_PAGE_PROD_URL}{SHURUPY_PO_DEREVU_PAGE_URL}",
                                      f"{MAIN_PAGE_STAGE_URL}{SHURUPY_PO_DEREVU_PAGE_URL}"])
    @pytest.mark.smoke_test
    def test_positive_check_discount_for_unauthorized_customer_for_amount_0_49rub_smoke(self, driver, link):
        page = ShurupyPoDerevuPage(driver)
        driver.get(link)
        price = (float(page.get_pc_price_list()[0].text[:-2]))
        page.get_add_to_cart_btn().click()
        page.get_header_cart_link_active().click()
        page.get_show_modal().click()
        page.get_name().send_keys('Тест')
        page.get_phone().send_keys('9999999999')
        page.get_email().send_keys('teststroy1@mail.ru')
        page.get_checkout_to_step_2().click()
        total = (float(page.get_products_total().text[:-2]))
        assert price == total, "Поле 'Товары на сумму' не совпадает с ценой из первого шага"
        assert page.cant_get_field_sale(), "Есть поле 'Скидка"
