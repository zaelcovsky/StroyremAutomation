from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
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

