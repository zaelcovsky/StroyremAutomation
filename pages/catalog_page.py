from base.seleniumbase import SeleniumBase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import allure


class CatalogPage(SeleniumBase):
    # в __init__ храним название локатора и его значени для необходимой страницы
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._header_catalog_menu = (By.CSS_SELECTOR, "a.header-catalog-menu_link")
        self._stroymateriali_link = (By.XPATH, "//a[contains(text(),'Стройматериалы')]")
        self._stroymateriali = (By.CSS_SELECTOR, "#mcm-screen-182 span:nth-child(2)")
        self._glavnaya_catalog = (By.CSS_SELECTOR, "#mcm-screen-182 .breadcrumb span:nth-child(1)")
        self._page_title = (By.XPATH, "//h1")

    @allure.step("Получение текста заголовка страницы")
    def get_page_title_text(self):
        return self.driver.find_element(*self._page_title).text

    @allure.step("Проверяем что элемент 'Каталог' виден на странице")
    def get_header_catalog_menu(self):
        return self.element_is_visible(self._header_catalog_menu)

    @allure.step("Проверяем что элемент 'Стройматериалы' виден на странице")
    def get_catalog_stroymateriali_link(self):
        return self.element_is_visible(self._stroymateriali_link)

    @allure.step("Проверяем что текст 'Стройматериалы' виден на странице")
    def get_catalog_stroymateriali_text(self):
        return self.element_is_visible(self._stroymateriali).text

    @allure.step("Проверяем что навигация 'Главная - Каталог' видна на странице")
    def get_navigation_glavnaya_catalog_text(self):
        return self.elements_are_present(self._glavnaya_catalog)
