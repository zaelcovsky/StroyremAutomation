import random

from base.seleniumbase import SeleniumBase
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage(SeleniumBase):

    # в __init__ храним название локатора и его значени для необходимой страницы
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._stroimaterialy_section = (By.CSS_SELECTOR, "a[href='catalog/strojmaterialy']")
        self._header_logo = (By.XPATH, "//div[@class='header-row header-row-2']//div[@class='header-logo']//a//img")
        # page-block best-offers-block
        self._random_item = (By.XPATH, "(//div[@class='product-link-div'])")
        # self._item = (By.XPATH, "(//div[@class='product-link-div'])[1]")

    # находим element, но не проводим тесты над ним
    @allure.step("Проверяем что элемент _terrestrially_section виден на странице")
    def get_stroimaterialy_section(self):
        return self.element_is_visible(self._stroimaterialy_section)

    @allure.step("Кликаем по случайному элементу")
    def go_to_random_item(self):
        all_items = self.find_elements(self._random_item)
        random_item = random.choice(all_items)
        self.go_to_element(random_item)
        random_item.click()

