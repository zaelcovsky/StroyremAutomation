import pytest
from pages.catalog_page import CatalogPage


@pytest.fixture(scope='function')
def catalog_page_open(driver, link):
    catalog_page = CatalogPage(driver)
    driver.get(link)
    catalog_page.get_header_catalog_menu().click()
    return catalog_page
