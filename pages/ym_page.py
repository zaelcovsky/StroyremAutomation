from base.seleniumbase import SeleniumBase
from selenium.webdriver.common.by import By
import allure


class YmPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._ym = ("xpath", "//*[contains(text(), '40023215')]")

    @allure.step("Проверяем что метрика 40023215 представлена на странице")
    def get_ym(self):
        return self.element_is_present(self._ym)
