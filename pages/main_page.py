from pages.base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPageLocators, BasePageLocators
import allure


class MainPage(BasePage):
    locators = MainPageLocators

    @allure.step('Проверка что картинка видима на странице')
    def check_that_image_is_present_and_visible_on_the_page(self, locator):
        """
        Проверяет что картинка видима на странице
        """
        image = self.element_is_visible(locator)
        image_height = self.driver.execute_script("return arguments[0].height;", image)
        image_width = self.driver.execute_script("return arguments[0].width;", image)
        assert image_height > 0 and image_width > 0, f"The image {image.get_attribute('src')} is not displayed"

    @allure.step('Проверка title страницы')
    def check_page_title(self, page_title, page_url):
        """
        Проверяет title страницы
        """
        main_page = MainPage(self.driver, page_url)
        main_page.open_page()
        assert self.driver.title == page_title, f"The title of the page {page_url} is incorrect"
