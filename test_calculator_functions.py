from .pages.main_page import MainPage


def test_initialize(driver):
    page = MainPage(driver)
    page.clear_button().click()


def test_display(driver):
    page = MainPage(driver)
    print(page.display_text())
