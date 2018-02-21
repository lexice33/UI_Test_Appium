import pytest

from appium import webdriver


class Drivers:
    @pytest.fixture(scope="function")
    def driver(self, request):
        desired_caps = {
            'automationName': 'Appium',
            'appActivity': 'ru.leroymerlin.mobile.presentation.MainActivity',
            'platformName': 'Android',
            'platformVersion': '8.0.0',
            'deviceName': 'c39bb44d',
            # 'deviceName': 'emulator-5554',  # Emulator
            'appPackage': 'ru.leroymerlin.mobile'
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        def fin():
            driver.quit()

        request.addfinalizer(fin)
        return driver  # provide the fixture value

    @pytest.fixture(scope="function")
    def c_driver(self, request):
        desired_caps = {
            'automationName': 'Appium',
            'appActivity': 'ru.leroymerlin.mobile.presentation.MainActivity',
            'platformName': 'Android',
            'platformVersion': '8.0.0',
            'deviceName': 'c39bb44d',
            # 'deviceName': 'emulator-5554',  # Emulator
            'appPackage': 'ru.leroymerlin.mobile',
            'noReset': 'true'
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        def fin():
            driver.quit()

        request.addfinalizer(fin)
        return driver  # provide the fixture value
