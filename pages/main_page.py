from Locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from Locators.base_locators import BaseLocators
import allure

class MainPage(BasePage):

    def __init__(self, driver):

        super().__init__(driver)
   
    @allure.step("Жмем верхнюю кнопку заказа")
    def click_on_header_order_button(self):

        self.click_to_element(MainPageLocators.BUTTON_HEADER_ORDER)

    @allure.step("Жмем нижнюю кнопку заказа")
    def click_on_lower_order_button(self):

        self.click_to_element(MainPageLocators.BUTTON_LOWER_ORDER)

    @allure.step("Жмем на логотип Яндекса")
    def click_yandex_logo(self):

        self.click_to_element(BaseLocators.YANDEX_LOGO)
    
    @allure.step('Скролим до нижней кнопки заказа')
    def scroll_to_the_lower_button_order(self):
        return self.scroll_to_the_element(MainPageLocators.BUTTON_LOWER_ORDER)

    @allure.step("Ждем появления нижней кнопки заказа")
    def wait_lower_button_order(self):
        return self.wait_element(MainPageLocators.BUTTON_LOWER_ORDER)