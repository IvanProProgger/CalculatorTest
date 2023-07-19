from .pages.main_page import MainPage


def test_initialize(driver):
    page = MainPage(driver)
    page.clear_button().click()
    page.number_seven().click()
    assert page.display_text() == "7", "Ошибка, элемент не совпадает с выводом"
    page.clear_button().click()


def test_display(driver):
    page = MainPage(driver)
    assert page.display_text() == "0", "Ошибка, элемент не совпадает с выводом"
