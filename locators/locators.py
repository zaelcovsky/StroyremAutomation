from selenium.webdriver.common.by import By


class BasePageLocators:
    HEADER_LOGO = (By.XPATH, "//div[@class='header-row header-row-2']//div[@class='header-logo']//a//img")


class MainPageLocators:
    STROJMATERIALY_SECTION = (By.CSS_SELECTOR, "a[href='catalog/strojmaterialy']")
