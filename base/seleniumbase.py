from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import TimeoutException, StaleElementReferenceException


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 15, 0.3)

    def find_element(self, locator):
        """
        Находит элемент по заданному локатору.
        Локатор - используется для поиска элемента. Возвращает WebElement.
        """
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        """
        Находит элементы по заданному локатору.
        Локатор - используется для поиска элемента. Возвращает WebElement.
        """
        return self.driver.find_elements(*locator)

    def element_is_visible(self, locator):
        """
        Ожидает проверку, что элемент присутствует в DOM-дереве, виден и отображается на странице.
        Видимость означает, что элемент не только отображается,
        но также имеет высоту и ширину больше 0.
        Локатор - используется для поиска элемента. Возвращает WebElement.
        Timeout - время в течение которого он будет ожидать. По умолчанию стоит 5 секунд,
        при необходимости можно будет изменить.
        """
        self.go_to_element(self.element_is_present(locator))
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator):
        """
        Ожидает проверку, что элементы присутствуют в DOM-дереве, видны и отображаются на странице.
        Видимость означает, что элементы не только отображаются,
        но также имеет высоту и ширину больше 0.
        Локатор - используется для поиска элементов. Возвращает WebElements.
        Timeout - время в течение которого он будет ожидать. По умолчанию стоит 5 секунд,
        при необходимости можно будет изменить.
        """
        return self.__wait.until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator):
        """
        Ожидает проверку, что элемент присутствует в DOM-дереве, но не обязательно,
        что виден и отображается на странице.
        Локатор - используется для поиска элемента. Возвращает WebElement.
        Timeout - время в течение которого он будет ожидать. По умолчанию стоит 5 секунд,
        при необходимости можно будет изменить.
        """
        return self.__wait.until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator):
        """
        Ожидает проверку, что элементы присутствуют в DOM-дереве, но не обязательно,
        что видны и отображаются на странице.
        Локатор - используется для поиска элемента. Возвращает WebElement.
        Timeout - время в течение которого он будет ожидать. По умолчанию стоит 5 секунд,
        при необходимости можно будет изменить.
        """
        return self.__wait.until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator):
        """
        Ожидает проверку, является ли элемент невидимым или нет. Элемент присутствует в DOM-дереве.
        Локатор - используется для поиска элемента. Возвращает WebElement.
        Timeout - время в течение которого он будет ожидать. По умолчанию стоит 5 секунд,
        при необходимости можно будет изменить.
        """
        return self.__wait.until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator):
        """
        Ожидает проверку, что элемент виден, отображается на странице,
        а также элемент включен. Элемент присутствует в DOM-дереве.
        Локатор - используется для поиска элемента.
        Timeout - время в течение которого он будет ожидать. По умолчанию стоит 5 секунд,
        при необходимости можно будет изменить.
        """
        return self.__wait.until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        """
        Скролит страницу к выбранному элементу так, чтобы элемент стал видимым пользователю.
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # def action_move_to_element(self, element):
    #     """
    #     Двигает курсор мышки на середину выбранного элемента
    #     Имитирует hover.
    #     Можно использовать для проверки интерактивности элемента при наведении
    #     курсора мышки на элемент.
    #     """
    #     action = ActionChains(self.driver)
    #     action.move_to_element(element)
    #     action.perform()

    # def press_enter_button(self):
    #     """
    #     Нажимает клавишу Enter
    #     """
    #     actions = ActionChains(self.driver)
    #     actions.send_keys(Keys.ENTER).perform()

    # def title_check(self, text=None):
    #     """
    #     Проверяет title страницы.
    #     text - ожидаемый текст title.
    #     """
    #     assert self.driver.title == text, "Title is NOT correct"

    # def switch_to_new_window(self):
    #     """
    #     Переключается на следующую вкладку браузера.
    #     """
    #     self.driver.switch_to.window(self.driver.window_handles[1])

    # def scroll_to_the_element(self, locator):
    #     """
    #     Скроллит до указанного элемента.
    #     """
    #     element = self.driver.find_element(*locator)
    #     self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # def scroll_down_the_page(self):
    #     """
    #     Скроллит до низа страницы.
    #     """
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # def link_visible_and_clickable(self, locator):
    #     """
    #     В случае ошибки подставляет в ответ адрес несработавшей ссылки.
    #     """
    #     link = wait(self.driver, timeout=3).until(EC.visibility_of_element_located(locator))
    #     link_text = link.get_attribute('href')
    #     assert link.is_displayed() and link.is_enabled(), \
    #         f'"{link_text}" link is not visible or clickable'

    # def check_link_redirection(self, locator, link):
    #     """
    #     Проверка переадресации после нажатия на соответствующую ссылку.
    #     """
    #     self.driver.find_element(*locator).click()
    #     assert link in self.driver.current_url, \
    #         f'"{link}" link does not redirect correctly'

    # def get_text_content_of_the_element(self, locator, data):
    #     """
    #     Проверяет видимый текст в элементе.
    #     """
    #     element = self.driver.find_element(*locator).text
    #     assert element == data, f'{data} is not in the text content of the element'

    # @allure.step('Проверка что картинка видима на странице')
    # def check_that_image_is_present_and_visible_on_the_page(self, locator):
    #     """
    #     Проверяет что картинка видима на странице
    #     """
    #     image = self.element_is_visible(locator)
    #     image_height = self.driver.execute_script("return arguments[0].height;", image)
    #     image_width = self.driver.execute_script("return arguments[0].width;", image)
    #     assert image_height > 0 and image_width > 0, f"The image {image.get_attribute('src')} is not displayed"

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def check_element_is_not_visible(self, locator):
        """
        Проверка того что элемент не виден на странице
        """
        try:
            self.element_is_not_visible(locator)
            return True
        except (TimeoutException, StaleElementReferenceException):
            return False

    def check_number_of_windows_to_be_equal(self, number):
        """
        Ожидает проверку того что количество открытых окон в браузере равно заданному значению (number)
        """
        return self.__wait.until(EC.number_of_windows_to_be(number))

