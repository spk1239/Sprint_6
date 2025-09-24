from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MainPage():
    dropdown_list_1 =[By.ID, 'accordion__heading-40']
    dropdown_list_2 =[By.ID, 'accordion__heading-41']
    dropdown_list_3 =[By.ID, 'accordion__heading-42']
    dropdown_list_4 =[By.ID, 'accordion__heading-43']
    dropdown_list_5 =[By.ID, 'accordion__heading-44']
    dropdown_list_6 =[By.ID, 'accordion__heading-45']
    dropdown_list_7 =[By.ID, 'accordion__heading-46']
    dropdown_list_8 =[By.ID, 'accordion__heading-47']
    text_in_dropdown_list_1 = [By.XPATH, '//p[text()="Сутки — 400 рублей. Оплата курьеру — наличными или картой."]']
    text_in_dropdown_list_2 = [By.XPATH, '//p[text()="Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."]']
    text_in_dropdown_list_3 = [By.XPATH, '//p[text()="Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."]']
    text_in_dropdown_list_4 = [By.XPATH, '//p[text()="Только начиная с завтрашнего дня. Но скоро станем расторопнее."]']
    text_in_dropdown_list_5 = [By.XPATH, '//p[text()="Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."]']
    text_in_dropdown_list_6 = [By.XPATH, '//p[text()="Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."]']
    text_in_dropdown_list_7 = [By.XPATH, '//p[text()="Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."]']
    text_in_dropdown_list_8 = [By.XPATH, '//p[text()="Да, обязательно. Всем самокатов! И Москве, и Московской области."]']

    def __init__(self, driver):
        self.driver = driver