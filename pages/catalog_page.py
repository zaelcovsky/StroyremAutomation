from base.seleniumbase import SeleniumBase
from selenium.webdriver.common.by import By
import allure


class CatalogPage(SeleniumBase):
    # в __init__ храним название локатора и его значени для необходимой страницы
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._header_catalog_menu = (By.CSS_SELECTOR, "a.header-catalog-menu_link")
        self._building_materials_link = (By.CSS_SELECTOR, ".mcm-to-screen.mcm-name[data-id='182']")
        self._building_materials = (By.CSS_SELECTOR, "#mcm-screen-182 span:nth-child(2)")
        self._main_catalog = (By.CSS_SELECTOR, "#mcm-screen-182 .breadcrumb span:nth-child(1)")
        self._main_catalog_tools = (By.CSS_SELECTOR, "#mcm-screen-1127 .breadcrumb span:nth-child(1)")
        self._page_title = (By.XPATH, "//h1")
        self._link_more = (By.CSS_SELECTOR, "a.mcm-more[data-id='622']")
        self._garden_tools_link = (By.CSS_SELECTOR, "[data-id='1127']")
        self._garden_tools_title = (By.CSS_SELECTOR, "#mcm-screen-1127 span:nth-child(2)")
        self._garden_tools_shovels_link = (By.CSS_SELECTOR, "[data-id='1128']")
        self._main_catalog_tools_shovels_link = (By.CSS_SELECTOR, ".block.content-container .breadcrumb a")
        self._picture_building_materials = (By.CSS_SELECTOR, ".mcm-img [data-id='182'] img")
        self._sort_name_link_a_z = (By.CSS_SELECTOR, ".catalog-sort.sort-desc[data-test]")
        self._sort_name_link_z_a = (By.CSS_SELECTOR, ".catalog-sort.sort-asc[data-test]")
        self._list_shtukaturnye_smesi = (By.CSS_SELECTOR, "a.pc-link")
        self._drywall_systems = (By.CSS_SELECTOR, "a.mcm-sub-name[data-id='777']")
        self._drywall_lists = (By.CSS_SELECTOR, "a.mcm-name[data-id='785']")
        self._sort_price_link = (By.XPATH, "//a[contains(text(), 'По цене')]")
        self._list_price = (By.CSS_SELECTOR, ".price-variant.active")

    @allure.step("Получение заголовка страницы")
    def get_page_title(self):
        return self.driver.find_element(*self._page_title)

    @allure.step("Проверяем что элемент 'Каталог товаров' виден в хедере")
    def get_header_catalog_menu(self):
        return self.element_is_visible(self._header_catalog_menu)

    @allure.step("Проверяем что блок 'Стройматериалы' виден на странице")
    def get_catalog_building_materials_link(self):
        return self.element_is_visible(self._building_materials_link)

    @allure.step("Проверяем что заголовок 'Стройматериалы' виден на странице")
    def get_catalog_building_materials_text(self):
        return self.element_is_visible(self._building_materials)

    @allure.step("Проверяем что навигация 'Главная - Каталог' видна на странице")
    def get_navigation_main_catalog_text(self):
        return self.elements_are_visible(self._main_catalog)

    @allure.step("Проверяем что ссылка 'Еще' видна на странице")
    def get_link_more(self):
        return self.element_is_visible(self._link_more)

    @allure.step("Проверяем что ссылка 'Еще' не видна на странице")
    def is_not_link_more(self):
        return self.element_is_not_visible(self._link_more)

    @allure.step("Проверяем что ссылка 'Садовый инструмент и инвентарь' видна на странице")
    def get_link_garden_tools(self):
        return self.element_is_visible(self._garden_tools_link)

    @allure.step("Проверяем что заголовок 'Садовый инструмент и инвентарь' виден на странице")
    def get_title_garden_tools(self):
        return self.element_is_visible(self._garden_tools_title)

    @allure.step("Проверяем что навигация 'Главная - Каталог - Ручной и электроинструмент' видна на странице")
    def get_navigation_main_catalog_tools_text(self):
        return self.elements_are_visible(self._main_catalog_tools)

    @allure.step("Проверяем что элемент 'Лопаты' виден на странице")
    def get_link_garden_tools_shovels(self):
        return self.element_is_visible(self._garden_tools_shovels_link)

    @allure.step("Проверяем что картинка 'Стройматериалы' видна на странице")
    def get_picture_building_materials(self):
        return self.element_is_visible(self._picture_building_materials)

    @allure.step("Проверяем что ссылка 'По названию А - Я' видна на странице")
    def get_sort_name_link_a_z(self):
        return self.element_is_visible(self._sort_name_link_a_z)

    @allure.step("Проверяем что ссылка 'По названию Я - А' видна на странице")
    def get_sort_name_link_z_a(self):
        return self.element_is_visible(self._sort_name_link_z_a)

    @allure.step("Проверяем что товары из раздела 'Штукатурные смеси' видны на странице")
    def get_list_shtukaturnye_smesi(self):
        return self.elements_are_present(self._list_shtukaturnye_smesi)

    @allure.step("Проверяем что ссылка 'Гипсокартонные системы' видна на странице")
    def get_link_drywall_systems(self):
        return self.element_is_visible(self._drywall_systems)

    @allure.step("Проверяем что ссылка 'ГИПСОКАРТОННЫЕ ЛИСТЫ (ГКЛ)' видна на странице")
    def get_link_drywall_lists(self):
        return self.element_is_visible(self._drywall_lists)

    @allure.step("Проверяем что ссылка 'По цене...' видна на странице")
    def get_sort_price_link(self):
        return self.element_is_visible(self._sort_price_link)

    @allure.step("Проверяем что цена товаров из раздела 'Штукатурные смеси' видна на странице")
    def get_list_price(self):
        return self.elements_are_present(self._list_price)
