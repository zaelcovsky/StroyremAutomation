from base.seleniumbase import SeleniumBase
from selenium.webdriver.common.by import By
import allure


class ProductsOnSale(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._price_first = (By.NAME, "price_first")
        self._price_last = (By.NAME, "price_last")
        self._in_stock_products = (By.CSS_SELECTOR, "[for='in_stock_products'] span")
        self._reset_filter = (By.CLASS_NAME, "reset-filter")
        self._pc_price = (By.XPATH, "(//div[contains(text(), 'p')])[1]")
        self._add_to_cart_btn = (By.XPATH, "(//a[contains(@class, 'add-to-cart')])[1]")
        self._header_cart_link_active = (By.CSS_SELECTOR, "a.header-cart-link.active")
        self._show_modal = (By.CSS_SELECTOR, ".total-block .show-modal")
        self._name = (By.CSS_SELECTOR, "#fiz [name='name']")
        self._phone = (By.CSS_SELECTOR, "#fiz [name='phone']")
        self._email = (By.CSS_SELECTOR, "#fiz [name='email']")
        self._checkout_to_step_2 = (By.CSS_SELECTOR, "#fiz .checkout-to-step-2")
        self._products_total = (By.CSS_SELECTOR, "#delivery-service .modal-products-total")
        self._products_sale = (By.XPATH, "//span[text()='Скидка']")
        self._discount_price = (By.CSS_SELECTOR, "#delivery-service .modal-discount-price")
        self._text_red_link = (By.CLASS_NAME, "text-red")
        self._cart_total = (By.ID, "cart-total")
        self._cart_discount = (By.CSS_SELECTOR, ".strong div")
        self._total_current_price = (By.CSS_SELECTOR, ".cell-total .cell-value")

    @allure.step("Проверяем видимость поля 'ЦЕНА от'")
    def get_field_price_first(self):
        return self.element_is_visible(self._price_first)

    @allure.step("Проверяем видимость поля 'ЦЕНА до'")
    def get_field_price_last(self):
        return self.element_is_visible(self._price_last)

    @allure.step("Проверяем кликабельность кнопки 'На складе'")
    def get_in_stock_products_link(self):
        self.element_is_visible(self._in_stock_products)
        return self.element_is_clickable(self._in_stock_products)

    @allure.step("Проверяем кликабельность кнопки 'Красная цена!'")
    def get_text_red_link(self):
        self.element_is_visible(self._text_red_link)
        return self.element_is_clickable(self._text_red_link)

    @allure.step("Проверяем видимость кнопки 'Сбросить фильтр'")
    def get_reset_filter_link(self):
        return self.element_is_visible(self._reset_filter)

    @allure.step("Проверяем видимость цены товара")
    def get_pc_price(self):
        self.is_element_present(self._pc_price)
        return self.element_is_visible(self._pc_price)

    @allure.step("Проверяем кликабельность кнопки 'В корзину'")
    def get_add_to_cart_btn(self):
        self.element_is_visible(self._add_to_cart_btn)
        return self.element_is_clickable(self._add_to_cart_btn)

    @allure.step("Проверяем кликабельность кнопки 'Корзина'")
    def get_header_cart_link_active(self):
        self.is_element_present(self._header_cart_link_active)
        return self.element_is_clickable(self._header_cart_link_active)

    @allure.step("Проверяем кликабельность кнопки 'Перейти к оформлению'")
    def get_show_modal(self):
        self.element_is_visible(self._show_modal)
        return self.element_is_clickable(self._show_modal)

    @allure.step("Проверяем видимость поля 'ФИО'")
    def get_name(self):
        return self.element_is_visible(self._name)

    @allure.step("Проверяем видимость поля 'Номер телефона'")
    def get_phone(self):
        return self.element_is_visible(self._phone)

    @allure.step("Проверяем видимость поля 'E-mail'")
    def get_email(self):
        return self.element_is_visible(self._email)

    @allure.step("Проверяем видимость кнопки 'Продолжить'")
    def get_checkout_to_step_2(self):
        return self.element_is_visible(self._checkout_to_step_2)

    @allure.step("Проверяем видимость поля 'Товары на сумму'")
    def get_products_total(self):
        return self.element_is_visible(self._products_total)

    @allure.step("Проверяем что нет поля 'Скидка'")
    def cant_get_field_sale(self):
        return self.element_is_not_visible(self._products_sale)

    @allure.step("Проверяем наличие поля 'Скидка'")
    def get_field_sale(self):
        return self.element_is_visible(self._products_sale)

    @allure.step("Проверяем видимость значения поля 'Скидка'")
    def get_discount_price(self):
        return self.element_is_visible(self._discount_price)

    @allure.step("Проверяем видимость значения поля 'Товары на сумму'")
    def get_cart_total(self):
        return self.element_is_present(self._cart_total)

    @allure.step("Проверяем видимость суммы Товара в корзине ")
    def get_total_current_price(self):
        return self.element_is_present(self._total_current_price)

    @allure.step("Проверяем видимость значения поля 'Скидка за объём'")
    def get_cart_discount(self):
        return self.element_is_present(self._cart_discount)
