from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import Data
import allure

class TestOrderPage():

    
    @allure.title("Проверка заказа через вверхнюю кнопку")
    @allure.description("Заходим на страницу заказа через вверхнюю кнопку и выполняем заказ")
    def test_order_scooter_header_button(self, driver):
        
        main_page = MainPage(driver)

        order_page = OrderPage(driver)
        
        main_page.click_on_header_order_button()
        
        order_page.order_scooter(Data.User_1)

        assert order_page.order_header_is_displayed()
        
    

    @allure.title("Проверка заказа через нижнюю кнопку")
    @allure.description("Заходим на страницу заказа через нижнюю кнопку и выполняем заказ")
    def test_order_scooter_lower_button(self, driver):

        main_page = MainPage(driver)

        order_page = OrderPage(driver)

        main_page.scroll_to_the_lower_button_order()

        main_page.wait_lower_button_order()

        main_page.click_on_lower_order_button()
        
        order_page.order_scooter(Data.User_2)
        
        assert order_page.order_header_is_displayed()



        
