import allure
from selenium.webdriver.common.by import By
from base.seleniumbase import SeleniumBase


@allure.epic("Login Account Page")
class BasketPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._email_input = (By.XPATH, "//input[@placeholder='example@gmail.com']")
        self._password_input = (By.XPATH, "//input[@placeholder='Пароль']")
        self._enter_button = (By.XPATH, "//input[@value='Войти']")
        self._register_button = (By.XPATH, "//a[@class='btn yellow-btn-invert']")

    @allure.step("Авторизация пользователя в системе")
    def login(self, email, password):
        self.driver.find_element(self._email_input).send_keys(email)
        self.driver.find_element(self._password_input).send_keys(password)
        self.driver.find_element(self._enter_button).click()

