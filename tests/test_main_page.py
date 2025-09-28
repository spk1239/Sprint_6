from pages.main_page import MainPage
import pytest
from Locators.main_page_locators import MainPageLocators
import pytest
import allure

class TestMainPage():

    dropdown_list = [[MainPageLocators.DROPDOWN_LIST_1, MainPageLocators.TEXT_IN_DROPDOWN_LOST_1], 
                     [MainPageLocators.DROPDOWN_LIST_2, MainPageLocators.TEXT_IN_DROPDOWN_LOST_2],
                     [MainPageLocators.DROPDOWN_LIST_3, MainPageLocators.TEXT_IN_DROPDOWN_LOST_3],
                     [MainPageLocators.DROPDOWN_LIST_4, MainPageLocators.TEXT_IN_DROPDOWN_LOST_4],
                     [MainPageLocators.DROPDOWN_LIST_5, MainPageLocators.TEXT_IN_DROPDOWN_LOST_5], 
                     [MainPageLocators.DROPDOWN_LIST_6, MainPageLocators.TEXT_IN_DROPDOWN_LOST_6],
                      [MainPageLocators.DROPDOWN_LIST_7, MainPageLocators.TEXT_IN_DROPDOWN_LOST_7],
                      [MainPageLocators.DROPDOWN_LIST_8, MainPageLocators.TEXT_IN_DROPDOWN_LOST_8]]

    @allure.title("Проверка выпадающего списка на главной странице")
    @allure.description("На странице ищем выпадающих список и проверяем что он расскрывается, и текст внутри совпадает с ожидаемым")
    @pytest.mark.parametrize("element_locator,view", dropdown_list)
    def test_dropdown_list_open(self, driver, element_locator, view):
        
        main_page = MainPage(driver)

        main_page.scroll_to_the_element(element_locator)

        main_page.wait_element(element_locator)

        main_page.click_to_element(element_locator)
        
        main_page.wait_element(view)
        
        assert driver.find_element(*view).is_displayed()


        
