import os
import shutil
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.basket_page import BasketPage
from pages.item_page import ItemPage
from pages.main_page import MainPage


@pytest.fixture(scope='function')
def driver():
    print('\nstart browser...')
    chrome_options = Options()
    # print()
    if 'CI' in os.environ:
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=Service(), options=chrome_options)
        driver.set_window_size(1382, 754)
    elif 'DOCKERRUN' in os.environ:
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=Service(), options=chrome_options)
        driver.set_window_size(1382, 754)
    else:
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service())
        driver.maximize_window()
        driver.implicitly_wait(10)
    yield driver
    print('\nquit browser...')
    driver.quit()


# скриншот
@allure.feature("Make a Screenshot")
def pytest_runtest_makereport(item, call):
    if call.when == 'call':
        # test_name = item.name
        if call.excinfo is not None:
            # status = 'failed'
            # logger.error(f'{status} - {test_name}. Reason: {str(call.excinfo)}')
            try:
                driver = item.funcargs['driver']
                driver.save_screenshot('allure_result/screenshot.png')
                allure.attach.file('allure_result/screenshot.png', name='Screenshot',
                                   attachment_type=allure.attachment_type.PNG)
                allure.attach(driver.page_source, name="HTML source", attachment_type=allure.attachment_type.HTML)
            except Exception as e:
                print(f"Failed to take screenshot: {e}")


@pytest.fixture(scope="session", autouse=True)
def clear_allure_results_folder():
    allure_report_dir = "allure_result"
    if os.path.exists(allure_report_dir):
        for file_name in os.listdir(allure_report_dir):
            file_path = os.path.join(allure_report_dir, file_name)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")


@pytest.fixture(scope='function', autouse=True)
def setup(driver):
    main_page = MainPage(driver)
    item_page = ItemPage(driver)
    basket_page = BasketPage(driver)
    yield main_page, item_page, basket_page


@pytest.fixture
def main_page(driver, url):
    page = MainPage(driver)
    driver.get(url)
    return page
