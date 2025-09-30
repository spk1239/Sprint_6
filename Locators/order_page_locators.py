from selenium.webdriver.common.by import By



class OrderPageLocators():
    NAME_FIELD = [By.XPATH, "//input[@placeholder='* Имя']"]

    SURNAME_FIELD = [By.XPATH, "//input[@placeholder='* Фамилия']"]

    ADRESS_FIELD = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]

    METRO_FIELD = [By.XPATH, "//input[@placeholder='* Станция метро']"]

    PHONE_FIELD = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]

    BUTTON_NEXT = [By.XPATH, "//button[text()='Далее']"]

    DATE_FIELD = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]

    RENTAL_PERIOD_FIELD = [By.XPATH, "//span[@class='Dropdown-arrow']"]

    BUTTON_DAY_OPTION = [By.XPATH, "//div[text()='сутки']"]

    BUTTON_ORDER = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]

    BUTTON_YES = [By.XPATH, "//button[text()='Да']"]

    ORDER_HEADER = [By.CLASS_NAME, 'Order_ModalHeader__3FDaJ']
    
    METRO_BULVAR = [By.XPATH, "//button[@value='1']"]