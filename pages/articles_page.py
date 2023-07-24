# Страница 'Строительные советы'
import allure
from selenium.webdriver.common.by import By
from base.seleniumbase import SeleniumBase


@allure.epic("Articles Page")
class ArticlesPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # articles-page
        self._page_title = (By.XPATH, "//h1[@class='title']")

    @allure.step("Получение текста заголовка страницы")
    def get_page_title_text(self):
        return self.driver.find_element(*self._page_title).text
