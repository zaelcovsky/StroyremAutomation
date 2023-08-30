import pytest
import allure
from .ym_constants import *
from constants import MAIN_PAGE_PROD_URL


@allure.epic("YA Metric")
class TestYaMetric:

    @allure.title("ym_is_present_smoke")
    @pytest.mark.parametrize('link', [MAIN_PAGE_PROD_URL, product_cart_url, order_url, delivery])
    @pytest.mark.smoke_test
    def test_ym_is_present_smoke(self, driver, link):
        driver.get(link)
        ya_metric = driver.find_element("xpath", "//*[contains(text(), '40023215')]").is_enabled()
        assert ya_metric is True, f'Нет яндекс метрики'
