import time
import pytest
from pages.products_on_sale_page import ProductsOnSale
from tests.test_products_on_sale.constants_products_on_sale_page import USER_NAME, USER_PHONE, USER_EMAIL


@pytest.fixture(scope='function')
def product_page_open(driver, link):
    """Открывает страницу каталога по link"""
    page = ProductsOnSale(driver)
    driver.get(link)
    return page
