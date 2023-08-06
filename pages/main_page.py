# Главная страница
import random
from base.seleniumbase import SeleniumBase
from selenium.webdriver.common.by import By
import allure
from constants import DELIVERY_PAGE_URL, LIFTING_PAGE_URL, LOCATION_PAGE_URL, ARTICLES_PAGE_URL


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
        # футер "Помощь покупателю"
        self._call_back_link = (By.XPATH, "(//a[@href='#backcall-popup'])[2]")
        self._call_back_popup_title = (By.XPATH, "(//div[@class='popup-h'])[1]")
        self._location = (By.XPATH, "(//a[@href='/contact'])[3]")
        self._attach_application = (By.XPATH, "(//a[@href='#attach-application'])[2]")
        # футер "Интернет магазин"
        self._building_advices_link = (By.XPATH, "(//a[@href='/articles'])[3]")
        self._product_catalog_link = (By.XPATH, "(//div[@class='footer-col']/ul/li/a)[1]")
        self._product_catalog = (By.XPATH, "//div[@id='mcm-screen-0']")
        self._product_catalog_header = (By.XPATH, "(//div[@class='mcm-h'])[1]")
        self._new_products_link = (By.XPATH, "(//a[@href='/catalog/new'])[3]")
        self._new_products_title = (By.XPATH, "//h1[contains(text(),'Новинки')]")
        self._price_link = (By.XPATH, "//a[@href='/price']")
        self._reviews_link = (By.XPATH, "(//a[contains(text(), 'Отзывы')])[3]")
        self._header = (By.XPATH, "//h1")
        self._shares_link = (By.XPATH, "(//a[contains(text(), 'Акции')])[2]")
        # футер "Доставка и оплата"
        self._delivery_link = (By.XPATH, "(//a[@href='/dostavka'])[3]")
        self._floor_climb_link = (By.XPATH, "(//a[@href='/podem-strojmaterialov-v-kvartiru'])[3]")
        self._payment_order_link = (By.XPATH, "(//a[@href='#order-pay'])[3]")
        self._payment_order_title = (By.XPATH, "(//div[@class='screen-h'])[1]")
        # футер top-right
        self._email_link = (By.XPATH, "//a[@class='footer-email']")
        self._telephone_number_link = (By.XPATH, "//a[@class='footer-phone']")

    # находим element, но не проводим тесты над ним
    @allure.step("Проверяем что элемент _stroimaterialy_section виден на странице")
    def get_stroimaterialy_section(self):
        return self.element_is_visible(self._stroimaterialy_section)

    @allure.step("Клик по случайному элементу")
    def go_to_random_item(self):
        """Выбирает случайный элемент из списка и кликает на него"""
        all_items = self.find_elements(self._random_item)
        if all_items:
            random_item = random.choice(all_items)
            self.go_to_element(random_item)
            random_item.click()
        else:
            raise ValueError("No items found for the _random_item locator")

    @allure.step("Проверка функциональности блока 'Советы от профессионалов ремонта'")
    def get_building_advices_section(self):
        """Проверяет и возвращает элементы блока 'Советы от профессионалов ремонта'"""
        section = self.driver.find_element(*self._building_advices_section)
        self.go_to_element(section)
        return self.driver.find_elements(*self._cart_items)

    @allure.step("Проверка селекторов на странице статьи")
    def check_selectors_article_page(self):
        """Проверяет доступность селекторов на странице статьи и возвращает их статус"""
        selectors_status = {}
        selectors_status['comment_button'] = self.driver.find_element(*self._comment_button).is_enabled()
        selectors_status['input_name'] = self.driver.find_element(*self._input_name).is_enabled()
        selectors_status['input_comment'] = self.driver.find_element(*self._input_comment).is_enabled()
        selectors_status['send_button'] = self.driver.find_element(*self._send_button).is_enabled()
        return selectors_status

    @allure.step("Проверка наличия статей на странице с советами (т.к. видео есть не на всех страницах)")
    def check_page_content(self):
        """Проверяет и возвращает статьи на странице с советами"""
        articles = self.find_elements(self._article_items)
        if not articles:
            raise ValueError("No articles found on the page")
        return articles

    @allure.step("Проверка функциональности ссылки 'Обратный звонок'")
    def check_call_back_link(self):
        """Проверяет работоспособность ссылки 'Обратный звонок' и возвращает текст заголовка"""
        self.driver.find_element(*self._call_back_link).click()
        title = self.driver.find_element(*self._call_back_popup_title).text
        return title

    @allure.step("Проверка функциональности ссылки 'Строительные советы'")
    def check_building_tips_link(self):
        """Проверяет работоспособность ссылки 'Строительные советы' и возвращает URL страницы"""
        self.driver.find_element(*self._building_advices_link).click()
        return ARTICLES_PAGE_URL

    @allure.step("Проверка функциональности ссылки 'Доставка'")
    def check_delivery_link(self):
        """Проверяет работоспособность ссылки 'Доставка' и возвращает результат проверки URL страницы"""
        self.driver.find_element(*self._delivery_link).click()
        return self.driver.current_url == DELIVERY_PAGE_URL

    @allure.step("Проверка функциональности ссылки 'Каталог товаров'")
    def check_product_catalog_link(self):
        """Проверяет работоспособность ссылки 'Каталог товаров' и возвращает статус видимости и текст заголовка"""
        self.driver.find_element(*self._product_catalog_link).click()
        product_catalog = self.driver.find_element(*self._product_catalog)
        title = self.driver.find_element(*self._product_catalog_header)
        return product_catalog.is_displayed(), title.text

    @allure.step("Проверка функциональности ссылки 'Доставка'")
    def check_delivery_link(self):
        """Проверяет работоспособность ссылки 'Доставка' и возвращает результат проверки URL страницы"""
        self.driver.find_element(*self._delivery_link).click()
        return self.driver.current_url == DELIVERY_PAGE_URL

    @allure.step("Проверка функциональности ссылки 'email'-info@stroyrem-nn.ru")
    def check_email_link(self):
        """Проверяет работоспособность ссылки 'email'-info@stroyrem-nn.ru и возвращает None, пока не реализовано"""
        self.driver.find_element(*self._email_link).click()
        return None

    @allure.step("Проверка функциональности ссылки 'Подъем на этаж'")
    def check_floor_climb_link(self):
        """Проверяет работоспособность ссылки 'Подъем на этаж' и возвращает результат проверки URL страницы"""
        self.driver.find_element(*self._floor_climb_link).click()
        return self.driver.current_url == LIFTING_PAGE_URL

    @allure.step("Проверка функциональности ссылки 'Местоположение'")
    def check_location_link(self):
        """Проверяет работоспособность ссылки 'Местоположение' и возвращает результат проверки URL страницы"""
        self.driver.find_element(*self._location).click()
        return self.driver.current_url == LOCATION_PAGE_URL

    @allure.step("Проверка функциональности ссылки 'Новинки'")
    def check_new_in_stock_link(self):
        """Проверяет работоспособность ссылки 'Новинки' и возвращает текст заголовка"""
        self.driver.find_element(*self._new_products_link).click()
        title = self.driver.find_element(*self._new_products_title).text
        return title

    @allure.step("Проверка функциональности ссылки 'Оплатить заказ'")
    def check_payment_order_link(self):
        """Проверяет работоспособность ссылки 'Оплатить заказ' и возвращает текст заголовка"""
        self.driver.find_element(*self._payment_order_link).click()
        title = self.driver.find_element(*self._payment_order_title).text
        return title

    @allure.step("Проверка функциональности ссылки 'номер телефона'-8 (831) 260-11-60")
    def check_telephone_number_link(self):
        """Проверяет работоспособность ссылки 'номер телефона'-8(831)260-11-60 и возвращает None, пока не реализовано"""
        self.driver.find_element(*self._telephone_number_link).click()
        return None

    @allure.step("Проверка функциональности ссылки 'Прайс'")
    def check_price_link(self):
        """Проверяет работоспособность ссылки 'Прайс' и возвращает None, пока не реализовано"""
        self.driver.find_element(*self._price_link).click()
        return None

    @allure.step("Проверка функциональности ссылки 'Отзывы'")
    def check_reviews_link(self):
        """Проверяет работоспособность ссылки 'Отзывы' и возвращает текст заголовка"""
        self.driver.find_element(*self._reviews_link).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        title = self.driver.find_element(*self._header).text
        return title

    @allure.step("Проверка функциональности ссылки 'Акции'")
    def check_shares_link(self):
        """Проверяет работоспособность ссылки 'Акции' и возвращает текст заголовка"""
        self.driver.find_element(*self._shares_link).click()
        title = self.driver.find_element(*self._header).text
        return title
