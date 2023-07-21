from .base_page import BasePage
import unidecode


class EngineerPage(BasePage):
    def button_factorial(self):
        return self.driver.find_element_by_name("Факториал")

    def assert_seven_factorial(self):
        assert self.display_text() == "5 040", "Ошибка, элемент не совпадает с выводом"


