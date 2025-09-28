from Locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from Locators.base_locators import BaseLocators
import allure

class MainPage(BasePage):

    def __init__(self, driver):

        super().__init__(driver)
   
    @allure.step("Жмем верхнюю кнопку заказа")
    def click_on_header_order_button(self):

        self.driver.find_element(*MainPageLocators.BUTTON_HEADER_ORDER).click()

    @allure.step("Жмем нижнюю кнопку заказа")
    def click_on_lower_order_button(self):

        self.driver.find_element(*MainPageLocators.BUTTON_LOWER_ORDER).click()

    @allure.step("Жмем на логотип Яндекса")
    def click_yandex_logo(self):

        self.driver.find_element(*BaseLocators.YANDEX_LOGO).click()
    

