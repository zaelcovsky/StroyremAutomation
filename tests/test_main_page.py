import pytest
import allure
from pages.main_page import MainPage
from constants import MAIN_PAGE_STAGE_URL, MAIN_PAGE_TITLE


@allure.epic("Main Page")
class TestMainPage:

    # @allure.title("TC 001 - проверка логотипа Stroyrem в хедере на главной странице")
    # @pytest.mark.smoke_test
    # def test_001_visibility_of_header_logo(self, driver, open_and_load_main_page):
    #     main_page = MainPage(driver)
    #     main_page.check_that_image_is_present_and_visible_on_the_page(BasePageLocators.HEADER_LOGO)

    @allure.title("TC 002 - проверка title на главной странице")
    @pytest.mark.regression_test
    def test_002_visibility_of_page_title(self, driver):
        main_page = MainPage(driver)
        driver.get(MAIN_PAGE_STAGE_URL) #нужно поправить 
        assert main_page.get_stroimaterialy_section().text == MAIN_PAGE_TITLE
