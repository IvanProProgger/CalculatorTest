def test_display(driver):
    find_display_text = driver.find_element_by_accessibility_id("CalculatorResults").text
    displaytext = find_display_text.strip("Отображать как")
    return displaytext


def test_initialize(driver):
    driver.find_element_by_name("Очистить").click()
    driver.find_element_by_name("Семь").click()
    assert test_display(driver) == "7", "ошибка"
    driver.find_element_by_name("Очистить").click()
