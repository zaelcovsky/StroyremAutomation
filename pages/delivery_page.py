# Страница рассчета доставки
import allure
from selenium.webdriver.common.by import By
from base.seleniumbase import SeleniumBase


@allure.epic("Delivery Page")
class DeliveryPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # delivery-page
        self._page_title = (By.XPATH, "//h1[contains(text(),'Варианты доставки')]")

    @allure.step("Получение текста заголовка страницы")
    def get_page_title_text(self):
        return self.driver.find_element(*self._page_title).text
