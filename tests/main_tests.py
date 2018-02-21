import os
import pytest

from appium import webdriver
from pages.intro import IntroPage
from pages.main import MainPage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestWebViewAndroid(IntroPage, MainPage):
    driver = IntroPage.driver
    c_driver = IntroPage.c_driver



    def test_info_page_opened(self, onetimedriver):
        MainPage.clickInfoButton(self, onetimedriver)
        assert MainPage.getDeliveryTitle(self, onetimedriver) == 'Доставка'
        print('Test OK')

    # def test_skip_introduction(self, driver):
    #     # first page of introduction
    #     assert IntroPage.isPicturePresent(self, driver) == True
    #     assert IntroPage.getTitleText(self, driver) == 'Приветствуем!'
    #     assert IntroPage.getDescriptionText(self, driver) == 'Познакомьтесь с возможностями нового приложения'
    #
    #     IntroPage.clickSkipButton(self, driver)
    #
    #     # select region page
    #     assert IntroPage.getTitleText(self, driver) == 'Выберите свой регион'
    #     assert IntroPage.getDescriptionText(self,
    #                                         driver) == 'Для отображения актуальной информации о наличии товаров специально для Вас!'
    #     assert IntroPage.getDescriptionChangeText(self, driver) == 'Вы можете изменить это позже'
    #
    #     IntroPage.selectRegion(self, driver)
    #     IntroPage.clickStartButton(self, driver)
    #
    #     # check that actual region equals region we select on previous page
    #     assert IntroPage.getActualRegion(self, driver) == 'Санкт-Петербург'
    #
    #     print('Test Passed')
    #
    # def test_pass_introduction(self, driver):
    #     # first page of introduction
    #     assert IntroPage.isPicturePresent(self, driver) == True
    #     assert IntroPage.getTitleText(self, driver) == 'Приветствуем!'
    #     assert IntroPage.getDescriptionText(self, driver) == 'Познакомьтесь с возможностями нового приложения'
    #
    #     IntroPage.clickShowButton(self, driver)
    #
    #     # second page of introduction
    #     assert IntroPage.isPicturePresent(self, driver) == True
    #     assert IntroPage.getTitleText(self, driver) == 'Онлайн покупки!'
    #     assert IntroPage.getDescriptionText(self, driver) == 'С мобильным приложением покупки стали еще проще'
    #
    #     IntroPage.swipeToLeft(self, driver)
    #
    #     # third page of introduction
    #     assert IntroPage.isPicturePresent(self, driver) == True
    #     assert IntroPage.getTitleText(self, driver) == 'Список покупок'
    #     assert IntroPage.getDescriptionText(self,
    #                                         driver) == 'Вы можете отложить понравившиеся товары и позже легко их найти'
    #
    #     IntroPage.swipeToLeft(self, driver)
    #     IntroPage.clickSkipButton(self, driver)
    #
    #     # select region page
    #     assert IntroPage.getTitleText(self, driver) == 'Выберите свой регион'
    #     assert IntroPage.getDescriptionText(self,
    #                                         driver) == 'Для отображения актуальной информации о наличии товаров специально для Вас!'
    #     assert IntroPage.getDescriptionChangeText(self, driver) == 'Вы можете изменить это позже'
    #
    #     IntroPage.selectRegion(self, driver)
    #     IntroPage.clickStartButton(self, driver)
    #
    #     # check that actual region equals region we select on previous page
    #     assert IntroPage.getActualRegion(self, driver) == 'Санкт-Петербург'
    #
    #     print('Test Passed')

    # def test_enable_geolocation(self, driver):
    #     IntroPage.pass_introduction(self, driver)
    #
    #     IntroPage.enable_geolocation_button(self, driver)
    #
    #     assert IntroPage.getActualRegion(self, driver) == 'Курск'
    # @pytest.fixture()
    # def resource_setup(self, request):
    #     desired_caps = {
    #         'automationName': 'Appium',
    #         'appActivity': 'ru.leroymerlin.mobile.presentation.MainActivity',
    #         'platformName': 'Android',
    #         # 'platformVersion': '8.0.0',
    #         'platformVersion': '7.1.1',
    #         'deviceName': 'c39bb44d',
    #         # 'deviceName': '4df797a95741317b',
    #         'appPackage': 'ru.leroymerlin.mobile',
    #         'fullReset': 'false',
    #
    #     }
    #     driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    #
    #     def fin():
    #         driver.quit()
    #
    #     request.addfinalizer(fin)
    #     return driver  # provide the fixture value
    #
    # @pytest.mark.usefixtures("resource_setup")
    # def test_map(self, driver):
    #     # first page of introduction
    #     assert IntroPage.isPicturePresent(self, driver) == True
    #     assert IntroPage.getTitleText(self, driver) == 'Приветствуем!'
    #     assert IntroPage.getDescriptionText(self, driver) == 'Познакомьтесь с возможностями нового приложения'
    #
    #     IntroPage.clickSkipButton(self, driver)
    #
    #     # select region page
    #     assert IntroPage.getTitleText(self, driver) == 'Выберите свой регион'
    #     assert IntroPage.getDescriptionText(self,
    #                                         driver) == 'Для отображения актуальной информации о наличии товаров специально для Вас!'
    #     assert IntroPage.getDescriptionChangeText(self, driver) == 'Вы можете изменить это позже'
    #
    #     IntroPage.selectRegion(self, driver)
    #     IntroPage.clickStartButton(self, driver)
    #
    #     # check that actual region equals region we select on previous page
    #     assert IntroPage.getActualRegion(self, driver) == 'Санкт-Петербург'
    #
    #     print('Test Passed')