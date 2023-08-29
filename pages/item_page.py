# Страница товара
import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from base.seleniumbase import SeleniumBase


@allure.epic("Item Page")
class ItemPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # item-page
        self._add_item = (By.XPATH, "(//a[@class='add-to-cart yellow-btn'])[1]")
        self._basket = (By.XPATH, "//a[@class='header-cart-link active']")
        self._pd_articul = (By.XPATH, "(//div[@class='pd-articul'])[2]")
        self._available_status = (By.XPATH, "(//div[@class='pd-ost_text'])[1]")
        self._item_amount = (By.XPATH, "//input[@class='amount']")

    def add_item_to_basket_and_go_to_basket(self):
        if self.is_element_present(self._add_item):
            if self.is_element_present(self._available_status) and self.find_element(
                    self._available_status).text == "Товара нет в наличии":
                print("Товар отсутствует в наличии")
                return None
            else:
                self.element_is_visible(self._add_item).click()
                articul = self.driver.find_element(*self._pd_articul).text
                self.element_is_visible(self._basket).click()
                return articul
        else:
            print("Не удалось добавить товар в корзину")
            return None

    @allure.step('Добавляем товар в корзину в количестве {amount}')
    def add_item_to_cart(self, amount: int):
        self.find_element(self._add_item).click()
        amount_field = self.find_element(self._item_amount)
        amount_field.clear()
        amount_field.send_keys(amount)
        time.sleep(2)
        return self

    @allure.step('Нажатие на кнопку корзины')
    def click_on_cart(self):
        self.find_element(self._basket).click()
        return self
