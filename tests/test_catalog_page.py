import time

import pytest
import allure
from pages.catalog_page import CatalogPage
from constants import MAIN_PAGE_STAGE_URL, MAIN_PAGE_PROD_URL


@allure.epic("Catalog Page")
class TestCatalogPage:

    @allure.title("001_positive_button_stroymateriali_smoke(catalog)")
    @pytest.mark.parametrize('link', [MAIN_PAGE_PROD_URL, MAIN_PAGE_STAGE_URL])
    @pytest.mark.smoke_test
    def test_001_positive_button_stroymateriali_smoke_catalog(self, driver, link):
        catalog_page = CatalogPage(driver)
        driver.get(link)
        catalog_page.get_header_catalog_menu().click()
        catalog_page.get_catalog_stroymateriali_link().click()
        text = catalog_page.get_catalog_stroymateriali_text()
        assert text == "Стройматериалы", "Меню 'Стройматериалы' не открылось"
