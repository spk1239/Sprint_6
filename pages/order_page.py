from Locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from Locators.base_locators import BaseLocators
import allure

class OrderPage(BasePage):
 
    def __init__(self, driver):

        super().__init__(driver)

    @allure.step("Заполняем форму заказа")
    def order_scooter(self, user):

        self.send_keys(OrderPageLocators.NAME_FIELD, user["Name"])

        self.send_keys(OrderPageLocators.SURNAME_FIELD, user["Surname"])

        self.send_keys(OrderPageLocators.ADRESS_FIELD, user["Adress"])

        self.click_to_element(OrderPageLocators.METRO_FIELD)

        self.click_to_element(OrderPageLocators.METRO_BULVAR)

        self.send_keys(OrderPageLocators.PHONE_FIELD, user["Number"])

        self.click_to_element(OrderPageLocators.BUTTON_NEXT)

        self.send_keys(OrderPageLocators.DATE_FIELD, user["Date"])

        self.wait_element(OrderPageLocators.RENTAL_PERIOD_FIELD)

        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_FIELD)

        self.wait_element(OrderPageLocators.BUTTON_DAY_OPTION)

        self.click_to_element(OrderPageLocators.BUTTON_DAY_OPTION)

        self.click_to_element(OrderPageLocators.BUTTON_ORDER)

        self.click_to_element(OrderPageLocators.BUTTON_YES)

    @allure.step("Жмем на логотип самоката")
    def click_scooter_logo(self):

        self.click_to_element(BaseLocators.SCOOTER_LOGO)

    @allure.step('Проверяем что появилось окно об успешном заказе')
    def order_header_is_displayed(self):

        return self.element_is_displayed(OrderPageLocators.ORDER_HEADER)
    
    

        



    

