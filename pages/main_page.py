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
        # хэдер
        self._user_profile_button = (By.XPATH, "//a[@class='header-profile-link auth-tooltip-show']")
        self._enter_button = (By.XPATH, "//a[@class='show-auth-modal']")
        self._registration_button = (By.XPATH, "//a[@class='register-link']")
        # секция лучшие предложения
        self._random_item = (By.XPATH, "(//div[@class='product-link-div'])")
        # self._item = (By.XPATH, "(//div[@class='product-link-div'])[1]")
        # секция строительные советы
        self._building_advices_section = (By.XPATH, "//div[@class='page-block articles-block']")
        self._cart_items = (By.XPATH, "//div[@class='article-link-div']/a")
        # https://stroyrem-nn.ru/article выдает 404 ошибку, поэтому пока не создавал article_page
        self._comment_button = (By.XPATH, "//p[@class='subtitle']")
        self._input_name = (By.XPATH, "//input[@placeholder='Имя']")
        self._input_comment = (By.XPATH, "//textarea[@placeholder='Комментарий']")
        self._send_button = (By.XPATH, "//input[@name='comment']")
        self._video_frame = (By.XPATH, "//div[@class='ytp-cued-thumbnail-overlay-image']")
        self._article_items = (By.XPATH, "//div[@class='article-item']")

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

    @allure.step("Проверка функциональности блока 'Советы от профессионалов ремонта'")
    def get_building_advices_section(self):
        section = self.driver.find_element(*self._building_advices_section)
        self.go_to_element(section)
        return self.driver.find_elements(*self._cart_items)

    @allure.step("Проверка селекторов на странице статьи")
    def check_selectors_article_page(self):
        selectors_status = {}
        selectors_status['comment_button'] = self.driver.find_element(*self._comment_button).is_enabled()
        selectors_status['input_name'] = self.driver.find_element(*self._input_name).is_enabled()
        selectors_status['input_comment'] = self.driver.find_element(*self._input_comment).is_enabled()
        selectors_status['send_button'] = self.driver.find_element(*self._send_button).is_enabled()
        return selectors_status

    @allure.step("Проверка наличия статей на странице c советами(т.к. видео есть не на всех страницах")
    def check_page_content(self):
        articles = self.find_elements(self._article_items)
        return articles