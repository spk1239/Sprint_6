from pages.main_page import MainPage
from pages.order_page import OrderPage
import allure
from data import Data

class TestUrlPage():

    @allure.title("Проверка перехода на страницу 'ЯндексДзен'")
    @allure.description("На главной странице жмем на логотип яндекса и переходим на страницу 'ЯндексДзен'")
    def test_transition_yandex_dzen_click_to_yandex_logo(self, driver):

        main_page = MainPage(driver)

        main_page.click_yandex_logo()

        main_page.wait()
        
        main_page.switch_window()
  
        main_page.wait_url(Data.YANDEX_DZEN_URL)

        assert main_page.current_url(Data.YANDEX_DZEN_URL)

    @allure.title("Проверка перехода на главную страницу")
    @allure.description("На странице заказа жмем на логотип самоката и переходим на главную страницу")
    def test_transition_scooter_main_page_click_to_scooter_logo(self, driver):

        main_page = MainPage(driver)

        order_page = OrderPage(driver)

        main_page.click_on_header_order_button()
        
        order_page.click_scooter_logo()

        assert order_page.current_url(Data.SCOOTER_URL)