import pytest
import allure
from selenium.common import TimeoutException
from constants import MAIN_PAGE_STAGE_URL, MAIN_PAGE_PROD_URL
from tests.catalog.catalog_constants import *
from pages.catalog_page import CatalogPage


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
        assert catalog_page_open.get_page_title().text == CATALOG_PAGE_SHOVELS_TITLE, \
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

    @allure.title("004_positive_alfabet_plaster_mixtures_smoke")
    @pytest.mark.xfail(reason='Неверная сортировка')
    @pytest.mark.parametrize('link', [SHTUKATURNYE_SMESI_PAGE_PROD_URL, SHTUKATURNYE_SMESI_PAGE_STAGE_URL])
    @pytest.mark.smoke_test
    def test_004_positive_alfabet_plaster_mixtures_smoke(self, driver, link):
        page = CatalogPage(driver)
        driver.get(link)
        page.get_sort_name_link_a_z().click()
        list_a_z = [item.text for item in page.get_list_shtukaturnye_smesi() if item.text != '']
        assert list_a_z == sorted(list_a_z), "Список не отсортирован от А до Я"
        page.get_sort_name_link_z_a().click()
        list_z_a = [item.text for item in page.get_list_shtukaturnye_smesi() if item.text != '']
        assert list_z_a == sorted(list_z_a, reverse=True), "Список не отсортирован от Я до А"

    @allure.title("007_positive_catalog_first_link_smoke")
    @pytest.mark.parametrize('link', [MAIN_PAGE_PROD_URL, MAIN_PAGE_STAGE_URL])
    @pytest.mark.smoke_test
    def test_007_positive_catalog_first_link_smoke(self, driver, link, catalog_page_open):
        catalog_page_open.get_link_drywall_systems().click()
        catalog_page_open.get_link_drywall_lists().click()
        assert driver.current_url == f"{link}{DRYWALL_LISTS_PAGE_URL}", "Неверный адрес страницы"
        assert catalog_page_open.get_page_title().text == CATALOG_PAGE_DRYWALL_LISTS_TITLE, \
            f"Заголовок '{CATALOG_PAGE_DRYWALL_LISTS_TITLE}' не отображается"