# Страница 'Корзина'
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
        self._total_weight = (By.ID, "total-weight")
        self._cart_total = (By.ID, "cart-total")
        self._go_to_checkout = (By.CSS_SELECTOR, "div.total-block a.btn.yellow-btn.show-modal")

    @allure.step("Получение кода товара в корзине")
    def get_product_code(self):
        return self.driver.find_element(*self._product_code).text

    @allure.step("Получение веса заказа")
    def get_weight(self):
        return float(''.join(filter(str.isdigit, self.find_element(self._total_weight).text)))

    @allure.step("Получение итоговой цены товаров в корзине")
    def get_cart_total_price(self):
        return float(''.join(filter(str.isdigit, self.find_element(self._cart_total).text)))

    @allure.step('Нажатие на кнопку "Перейти к оформлению"')
    def click_on_go_to_checkout(self):
        self.element_is_clickable(self._go_to_checkout).click()
        return self
