import pytest
from appium import webdriver


desired_caps = {
    "app": "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App",
    "deviceName": "WindowsPC",
    "platformName": "Windows"
}


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Remote(
        command_executor='http://192.168.31.248:4723/wd/hub',
        desired_capabilities=desired_caps
    )
    yield driver
    driver.quit()