import pytest
from appium import webdriver


desired_caps = {}
desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723',
        desired_capabilities=desired_caps
    )
    yield driver
    driver.quit()




