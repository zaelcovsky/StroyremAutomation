# Страница 'Корзина'
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.seleniumbase import SeleniumBase


@allure.epic("Ordering Page")
class OrderingPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # basket-page
        self._fiz_fio = (By.XPATH, "//div[@id='fiz']//input[contains(@name, 'name')]")
        self._fiz_phone = (By.XPATH, "//div[@id='fiz']//input[contains(@name, 'phone')]")
        self._fiz_email = (By.XPATH, "//div[@id='fiz']//input[contains(@name, 'email')]")
        self._continue_btn = (By.XPATH, "//a[@class='yellow-btn checkout-to-step-2 checkout-to-step-2-fiz']")
        self._city = (By.XPATH, "//form[@class='checkout-step2-form']//input[contains(@name, 'city')]")
        self._street = (By.XPATH, "//form[@class='checkout-step2-form']//input[contains(@name, 'address')]")
        self._city_ajax = (By.CSS_SELECTOR, "form.checkout-step2-form div.ajaxed-data.ajaxed-city.active")
        self._street_ajax = (By.CSS_SELECTOR, "form.checkout-step2-form div.ajaxed-data.ajaxed-address.active")
        self._radio_items = (By.XPATH, "//div[@class='radio-items']")
        self._standard_delivery = (By.XPATH, "//label[@for='del_id_1']")
        self._standard_delivery_price = (By.XPATH, "//label[@for='del_id_1']/div[contains(@class, 'radio-del-price')]")
        self._delivery_in_time = (By.XPATH, "//label[@for='del_id_2']")
        self._delivery_in_time_price = (By.XPATH, "//label[@for='del_id_2']/div[contains(@class, 'radio-del-price')]")
        self._delivery_all_time = (By.XPATH, "//label[@for='del_id_3']")
        self._delivery_all_time_price = (By.XPATH, "//label[@for='del_id_3']/div[contains(@class, 'radio-del-price')]")

    @allure.step("Заполняем поле имя: {name}")
    def fill_fiz_name(self, name):
        self.element_is_clickable(self._fiz_fio).send_keys(name)
        return self

    @allure.step("Заполняем телефон: {phone}")
    def fill_fiz_phone(self, phone):
        self.element_is_clickable(self._fiz_phone).send_keys(phone)
        return self

    @allure.step("Заполняем email: {email}")
    def fill_fiz_email(self, email):
        self.element_is_clickable(self._fiz_email).send_keys(email)
        return self

    @allure.step('Нажатие на кнопку "Продолжить"')
    def click_on_continue(self):
        self.element_is_clickable(self._continue_btn).click()
        return self

    @allure.step("Заполняем город: {city}")
    def fill_city(self, city):
        self.find_element(self._city).send_keys(city)
        wait = WebDriverWait(self.driver, 50, 0.3)
        wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[@data-city='{city}']"))).click()
        return self

    @allure.step("Заполняем улицу: {street}")
    def fill_street(self, street):
        self.find_element(self._street).send_keys(street)
        wait = WebDriverWait(self.driver, 50, 0.3)
        wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[@data-address='{street}']"))).click()
        return self

    @allure.title("Выбираем доставку: {name}")
    def select_delivery(self, name: str):
        delivery_options = {
            "standard": self._standard_delivery,
            "in_time": self._delivery_in_time,
            "all_time": self._delivery_all_time
        }
        delivery = delivery_options.get(name.lower())
        self.element_is_clickable(delivery).click()
        return self

    @allure.step("Получаем цену {name} доставки")
    def get_delivery_price(self, name: str):
        delivery_options = {
            "standard": self._standard_delivery_price,
            "in_time": self._delivery_in_time_price,
            "all_time": self._delivery_all_time_price
        }
        delivery = delivery_options.get(name.lower())
        return self.find_element(delivery).text
