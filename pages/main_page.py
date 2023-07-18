from .base_page import BasePage


class MainPage(BasePage):
    def clear_button(self):
        return self.driver.find_element_by_name("Очистить")

    def display_text(self):
        find_display_text = self.driver.find_element_by_accessibility_id("CalculatorResults").text
        displaytext = find_display_text.strip("Отображать как")
        return displaytext
