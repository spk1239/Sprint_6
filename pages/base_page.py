
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure

class BasePage():

    def __init__(self, driver):

        self.driver = driver

    @allure.step("Скролим до нужного элемента")
    def scroll_to_the_element(self, locator):

        element = self.driver.find_element(*locator)

        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    @allure.step("Ждем появления элемента")
    def wait_element(self, locator):

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step("Жмем на элемент")
    def click_to_element(self, element):
          
          self.driver.find_element(*element).click()
