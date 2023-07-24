from .base_page import BasePage
from helper.constans import AssertConstant


class SpeedPage(BasePage):

    def change_unit1_to_km_hour(self):
        self.driver.find_element_by_accessibility_id("Units1").click()
        self.driver.find_element_by_name("километров в час").click()

    def change_unit2_to_mile_hour(self):
        self.driver.find_element_by_accessibility_id("Units2").click()
        self.driver.find_element_by_name("миль в час").click()

    def assert_for_correct_output(self):
        assert self.value_output() == AssertConstant.seven_km_hour_into_mile_hour
