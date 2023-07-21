from .base_page import BasePage
import unidecode


class MainPage(BasePage):

    def display_text(self):
        find_display_text = self.driver.find_element_by_accessibility_id("CalculatorResults").text
        displaytext = "".join(unidecode.unidecode(find_display_text.strip("Отображать как")).split())
        return displaytext

    def go_to_main_page(self):
        self.driver.find_element_by_name("Открыть навигацию").click()
        self.driver.find_element_by_name("Обычный Калькулятор").click()

    def go_to_engineer_page(self):
        self.driver.find_element_by_name("Открыть навигацию").click()
        self.driver.find_element_by_name("Инженерный Калькулятор").click()

    def go_to_speed_page(self):
        self.driver.find_element_by_name("Открыть навигацию").click()
        self.driver.find_element_by_name("Скорость Преобразователь").click()
