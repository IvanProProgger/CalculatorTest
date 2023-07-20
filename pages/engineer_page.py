from .base_page import BasePage
import unidecode


class EngineerPage(BasePage):
    def button_factorial(self):
        return self.driver.find_element_by_name("Факториал")



