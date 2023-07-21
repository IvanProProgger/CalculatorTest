import unidecode


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def number_zero(self):
        return self.driver.find_element_by_name("Ноль")

    def number_one(self):
        return self.driver.find_element_by_name("Один")

    def number_two(self):
        return self.driver.find_element_by_name("Два")

    def number_three(self):
        return self.driver.find_element_by_name("Три")

    def number_four(self):
        return self.driver.find_element_by_name("Четыре")

    def number_five(self):
        return self.driver.find_element_by_name("Пять")

    def number_six(self):
        return self.driver.find_element_by_name("Шесть")

    def number_seven(self):
        return self.driver.find_element_by_name("Семь")

    def number_eight(self):
        return self.driver.find_element_by_name("Восемь")

    def number_nine(self):
        return self.driver.find_element_by_name("Девять")

    def clear_button_empty(self):
        return self.driver.find_element_by_name("Очистить")

    def clear_button_with_text(self):
        return self.driver.find_element_by_name("Очистить запись")

    def display_text(self):
        find_display_text = self.driver.find_element_by_accessibility_id("CalculatorResults").text
        displaytext = unidecode.unidecode(find_display_text.strip("Отображать как "))
        return displaytext

    def value_input(self):
        find_display_text = self.driver.find_element_by_accessibility_id("Value1").text
        num = find_display_text.split()[2]
        return num

    def value_output(self):
        find_display_text = self.driver.find_element_by_accessibility_id("Value2").text
        num = find_display_text.split()[2]
        return num

    def assert_for_default_display_text(self):
        assert self.display_text() == "0", "Ошибка, дефолтный текст на дисплее не соответствует"


