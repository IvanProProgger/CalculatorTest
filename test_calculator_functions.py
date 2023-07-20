import time
from .pages.speed_page import SpeedPage
from .pages.main_page import MainPage
from .pages.engineer_page import EngineerPage
import pytest


@pytest.fixture(autouse=True)
def test_go_to_main_page(driver):
    page = MainPage(driver)
    page.go_to_main_page()


def test_display(driver):
    page = MainPage(driver)
    assert page.display_text() == "0", "Ошибка, элемент не совпадает с выводом"


def test_initialize(driver):
    page = MainPage(driver)
    page.clear_button_empty().click()
    page.number_seven().click()
    assert page.display_text() == "7", "Ошибка, элемент не совпадает с выводом"


def test_engineer_calculator_page(driver):
    page = MainPage(driver)
    page.clear_button_empty().click()
    page.go_to_engineer_page()
    if page.display_text() != "0":
        page.clear_button_with_text().click()
    assert page.display_text() == "0", "Ошибка, элемент не совпадает с выводом"


def test_engineer_page_factorial(driver):
    page = MainPage(driver)
    page.number_five().click()
    if page.display_text() != "0":
        page.clear_button_with_text().click()
    page.go_to_engineer_page()
    engin_page = EngineerPage(driver)
    engin_page.number_seven().click()
    engin_page.button_factorial().click()
    assert engin_page.display_text() == "5 040", "Ошибка, элемент не совпадает с выводом"


def test_speed_page_convert(driver):
    page = MainPage(driver)
    page.clear_button_empty().click()
    page.go_to_speed_page()
    speed_page = SpeedPage(driver)
    speed_page.change_unit1_to_km_hour()
    speed_page.change_unit2_to_mile_hour()
    speed_page.number_seven().click()
    assert speed_page.value_output() == "4,349988"

