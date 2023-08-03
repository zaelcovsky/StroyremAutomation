from base.seleniumbase import SeleniumBase
from selenium.webdriver.common.by import By
import allure


class CatalogPage(SeleniumBase):
    # в __init__ храним название локатора и его значени для необходимой страницы
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._header_catalog_menu = (By.CSS_SELECTOR, "a.header-catalog-menu_link")
        self._building_materials_link = (By.XPATH, "//a[contains(text(),'Стройматериалы')]")
        self._building_materials = (By.CSS_SELECTOR, "#mcm-screen-182 span:nth-child(2)")
        self._main_catalog = (By.CSS_SELECTOR, "#mcm-screen-182 .breadcrumb span:nth-child(1)")
        self._main_catalog_tools = (By.CSS_SELECTOR, "#mcm-screen-1127 .breadcrumb span:nth-child(1)")
        self._page_title = (By.XPATH, "//h1")
        self._link_more = (By.CSS_SELECTOR, "a.mcm-more[data-id='622']")
        self._garden_tools_link = (By.CSS_SELECTOR, "[data-id='1127']")
        self._garden_tools_title = (By.CSS_SELECTOR, "#mcm-screen-1127 span:nth-child(2)")
        self._garden_tools_shovels_link = (By.CSS_SELECTOR, "[data-id='1128']")
        self._main_catalog_tools_shovels_link = (By.CSS_SELECTOR, ".block.content-container .breadcrumb a")

    @allure.step("Получение текста заголовка страницы")
    def get_page_title_text(self):
        return self.driver.find_element(*self._page_title).text

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
