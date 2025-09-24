from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrderPage():
    name_field = [By.XPATH, "//input[@placeholder='* Имя']"]
    surname_field = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    adress_field = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    metro_field = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    phone_field = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    button_next = [By.XPATH, "//button[text()='Далее']"]
    date_field = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    rental_period_field = [By.XPATH, "//div[text()='* Срок аренды']"]
    button_day_option = [By.XPATH, "//div[text()='сутки']"]
    button_order = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    button_yes = [By.XPATH, "//button[text()='Да'"]
    order_header = [By.CLASS_NAME, 'Order_ModalHeader__3FDaJ']

    def __init__(self, driver):
        self.driver = driver