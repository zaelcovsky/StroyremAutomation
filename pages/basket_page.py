# Страница  'Корзина'
import allure
from selenium.webdriver.common.by import By
from base.seleniumbase import SeleniumBase


@allure.epic("Basket Page")
class BasketPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # basket-page
        self._product_code = (By.XPATH, "//div[@class='product-code']")

    @allure.step("Получение кода товара в корзине")
    def get_product_code(self):
        return self.driver.find_element(*self._product_code).text
