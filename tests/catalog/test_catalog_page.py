import pytest
import allure
from selenium.common import TimeoutException
from constants import MAIN_PAGE_STAGE_URL, MAIN_PAGE_PROD_URL
from tests.catalog.catalog_constants import *


@allure.epic("Catalog Page")
class TestCatalogPage:

    @allure.title("001_positive_button_stroymateriali_smoke(catalog)")
    @pytest.mark.parametrize('link', [MAIN_PAGE_PROD_URL, MAIN_PAGE_STAGE_URL])
    @pytest.mark.smoke_test
    def test_001_positive_button_stroymateriali_smoke(self, driver, link, catalog_page_open):
        catalog_page_open.get_catalog_building_materials_link().click()
        assert catalog_page_open.get_catalog_building_materials_text().text == CATALOG_PAGE_BUILDING_MATERIALS_TITLE, \
            f"Заголовок '{CATALOG_PAGE_BUILDING_MATERIALS_TITLE}' не отображается"
        assert catalog_page_open.get_navigation_main_catalog_text()[0].text == CATALOG_PAGE_MAIN_LINK, \
            f"Меню навигации '{CATALOG_PAGE_MAIN_LINK}' не отображается"
        assert catalog_page_open.get_navigation_main_catalog_text()[1].text == CATALOG_PAGE_CATALOG_LINK, \
            f"Меню навигации '{CATALOG_PAGE_CATALOG_LINK}' не отображается"

    @allure.title("002_positive_last_link_of_catalog_smoke")
    @pytest.mark.parametrize('link', [MAIN_PAGE_PROD_URL, pytest.param(
        MAIN_PAGE_STAGE_URL, marks=pytest.mark.xfail(reason=f'Нет элемента {CATALOG_PAGE_GARDEN_TOOLS_TITLE}'))])
    @pytest.mark.smoke_test
    def test_002_positive_last_link_of_catalog_smoke(self, driver, link, catalog_page_open):
        catalog_page_open.get_link_more().click()
        assert catalog_page_open.is_not_link_more(), f"Список '{CATALOG_PAGE_MORE_LINK}' не раскрылся"
        try:
            catalog_page_open.get_link_garden_tools().click()
        except TimeoutException:
            print(f'Нет элемента {CATALOG_PAGE_GARDEN_TOOLS_TITLE}')
        assert catalog_page_open.get_title_garden_tools().text == CATALOG_PAGE_GARDEN_TOOLS_TITLE, \
            f"Заголовок '{CATALOG_PAGE_GARDEN_TOOLS_TITLE}' не отображается"
        assert catalog_page_open.get_navigation_main_catalog_tools_text()[0].text == CATALOG_PAGE_MAIN_LINK, \
            f"Меню навигации '{CATALOG_PAGE_MAIN_LINK}' не отображается"
        assert catalog_page_open.get_navigation_main_catalog_tools_text()[1].text == CATALOG_PAGE_CATALOG_LINK, \
            f"Меню навигации '{CATALOG_PAGE_CATALOG_LINK}' не отображается"
        assert catalog_page_open.get_navigation_main_catalog_tools_text()[2].text == CATALOG_PAGE_TOOLS_LINK, \
            f"Меню навигации '{CATALOG_PAGE_TOOLS_LINK}' не отображается"
        catalog_page_open.get_link_garden_tools_shovels().click()
        assert catalog_page_open.get_page_title_text() == CATALOG_PAGE_SHOVELS_TITLE, \
            f"Заголовок '{CATALOG_PAGE_SHOVELS_TITLE}' не отображается"

    @allure.title("003_positive_pic_stroymateriali_smoke(catalog)")
    @pytest.mark.parametrize('link', [MAIN_PAGE_PROD_URL, MAIN_PAGE_STAGE_URL])
    @pytest.mark.smoke_test
    def test_003_positive_pic_stroymateriali_smoke(self, driver, link, catalog_page_open):
        catalog_page_open.get_picture_building_materials().click()
        assert catalog_page_open.get_catalog_building_materials_text().text == CATALOG_PAGE_BUILDING_MATERIALS_TITLE, \
            f"Заголовок '{CATALOG_PAGE_BUILDING_MATERIALS_TITLE}' не отображается"
        assert catalog_page_open.get_navigation_main_catalog_text()[0].text == CATALOG_PAGE_MAIN_LINK, \
            f"Меню навигации '{CATALOG_PAGE_MAIN_LINK}' не отображается"
        assert catalog_page_open.get_navigation_main_catalog_text()[1].text == CATALOG_PAGE_CATALOG_LINK, \
            f"Меню навигации '{CATALOG_PAGE_CATALOG_LINK}' не отображается"
