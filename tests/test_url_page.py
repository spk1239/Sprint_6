from pages.main_page import MainPage
from pages.order_page import OrderPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class TestUrlPage():

    @allure.title("Проверка перехода на страницу 'ЯндексДзен'")
    @allure.description("На главной странице жмем на логотип яндекса и переходим на страницу 'ЯндексДзен'")
    def test_transition_yandex_dzen_click_to_yandex_logo(self, driver):

        main_page = MainPage(driver)

        main_page.click_yandex_logo()

        WebDriverWait(driver, 10)
        
        windows = driver.window_handles
        
        driver.switch_to.window(windows[-1])
  
        WebDriverWait(driver, 10).until(EC.url_contains('dzen'))

        assert 'dzen' in driver.current_url

    @allure.title("Проверка перехода на главную страницу")
    @allure.description("На странице заказа жмем на логотип самоката и переходим на главную страницу")
    def test_transition_scooter_main_page_click_to_scooter_logo(self, driver):

        main_page = MainPage(driver)

        order_page = OrderPage(driver)

        main_page.click_on_header_order_button()
        
        order_page.click_scooter_logo()

        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'