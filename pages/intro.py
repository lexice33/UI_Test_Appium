import pytest
import time

from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from locators.intro_locators import Locators
from locators.main_locators import Locators as MainLocators


class IntroPage:
    @pytest.fixture(scope="function")
    def driver(self, request):
        desired_caps = {
            'automationName': 'Appium',
            'appActivity': 'ru.leroymerlin.mobile.presentation.MainActivity',
            'platformName': 'Android',
            'platformVersion': '8.0.0',
            # 'platformVersion': '7.1.1',
            'deviceName': 'c39bb44d',
            # 'deviceName': '4df797a95741317b',
            'appPackage': 'ru.leroymerlin.mobile',
            # not to clear app data
            # 'fullReset': 'false',
            # 'noReset': 'true'
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
            'appPackage': 'ru.leroymerlin.mobile',
            'noReset': 'true'
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        def fin():
            driver.quit()

        request.addfinalizer(fin)
        return driver  # provide the fixture value


    def isPicturePresent(self, driver):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Locators.PAGE_IMAGE)))
        picture = driver.find_element_by_id(Locators.PAGE_IMAGE)

        if picture.is_displayed():
            return True
        else:
            return False

    def getTitleText(self, driver):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Locators.PAGE_TITLE)))
        title_text = driver.find_element_by_id(Locators.PAGE_TITLE).text

        return title_text

    def getDescriptionText(self, driver):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Locators.PAGE_DESCRIPTION)))
        description_text = driver.find_element_by_id(Locators.PAGE_DESCRIPTION).text

        return description_text

    def getDescriptionChangeText(self, driver):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Locators.PAGE_DESCRIPTION_CHANGE)))
        description_text = driver.find_element_by_id(Locators.PAGE_DESCRIPTION_CHANGE).text

        return description_text

    def clickShowButton(self, driver):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Locators.SHOW_BUTTON)))
        show_button = driver.find_element_by_id(Locators.SHOW_BUTTON)
        show_button.click()

    def clickSkipButton(self, driver):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Locators.SKIP_BUTTON)))
        skip_button = driver.find_element_by_id(Locators.SKIP_BUTTON)
        skip_button.click()

    def clickStartButton(self, driver):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Locators.START_BUTTON)))
        start_button = driver.find_element_by_id(Locators.START_BUTTON)
        start_button.click()

    def selectRegion(self, driver):
        driver.swipe(540, 960, 10, 500, 1500)

    def getActualRegion(self, driver):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, MainLocators.ACTUAL_REGION)))
        actual_region = driver.find_element_by_id(MainLocators.ACTUAL_REGION)
        actual_region_text = actual_region.text

        return actual_region_text

    def swipeToLeft(self, driver):
        driver.swipe(700, 500, 10, 10, 700)

    def pass_introduction(self, driver):
        self.clickShowButton(driver)
        time.sleep(1)
        self.swipeToLeft(driver)
        time.sleep(1)
        self.swipeToLeft(driver)
        time.sleep(1)
        self.swipeToLeft(driver)

    def enable_geolocation_button(self, driver):
        self.clickStartButton(driver)

        if WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Locators.ALLOW_PERMISSIONS))):
            allow_permissions = driver.find_element_by_id(Locators.ALLOW_PERMISSIONS)

            if allow_permissions.is_displayed():
                allow_permissions.click()

                confirm_allow_permissions = driver.find_elements_by_id(Locators.CONFIRM_ALLOW_PERMISSIONS)

                if len(confirm_allow_permissions) != 0:
                    confirm_allow_permissions[0].click()
                else:
                     print('Test OK')
            else:
                print('Test OK')