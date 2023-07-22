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
        self._glavnaya = (By.XPATH, "//a[contains(text(),'Главная')]")
        self._catalog = (By.XPATH, "//a[contains(text(),'Каталог')]")

    @allure.step("Проверяем что элемент _header_catalog_menu виден на странице")
    def get_header_catalog_menu(self):
        self.element_is_visible(self._header_catalog_menu).click()
        self.element_is_visible(self._stroymateriali_link).click()
        stroymateriali = self.element_is_visible(self._stroymateriali)
        return stroymateriali.text
