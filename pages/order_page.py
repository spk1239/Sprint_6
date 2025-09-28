from Locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from Locators.base_locators import BaseLocators
import allure

class OrderPage(BasePage):
 
    def __init__(self, driver):

        super().__init__(driver)

    @allure.step("Заполняем форму заказа")
    def order_scooter(self, user):

        self.driver.find_element(*OrderPageLocators.NAME_FIELD).send_keys(user["Name"])

        self.driver.find_element(*OrderPageLocators.SURNAME_FIELD).send_keys(user["Surname"])

        self.driver.find_element(*OrderPageLocators.ADRESS_FIELD).send_keys(user["Adress"])

        self.driver.find_element(*OrderPageLocators.METRO_FIELD).click()

        self.driver.find_element(*OrderPageLocators.METRO_BULVAR).click()

        self.driver.find_element(*OrderPageLocators.PHONE_FIELD).send_keys(user["Number"])

        self.driver.find_element(*OrderPageLocators.BUTTON_NEXT).click()

        self.driver.find_element(*OrderPageLocators.DATE_FIELD).send_keys(user["Date"])

        self.wait_element(OrderPageLocators.RENTAL_PERIOD_FIELD)

        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_FIELD).click()

        self.wait_element(OrderPageLocators.BUTTON_DAY_OPTION)

        self.driver.find_element(*OrderPageLocators.BUTTON_DAY_OPTION).click()

        self.driver.find_element(*OrderPageLocators.BUTTON_ORDER).click()

        self.driver.find_element(*OrderPageLocators.BUTTON_YES).click()

    @allure.step("Жмем на логотип самоката")
    def click_scooter_logo(self):

        self.driver.find_element(*BaseLocators.SCOOTER_LOGO).click()

        



    

