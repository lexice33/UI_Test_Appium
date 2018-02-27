import os

from pages.intro import IntroPage
from pages.main import MainPage
from tools.drivers import Drivers

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestWebViewAndroid(IntroPage, MainPage, Drivers):
    driver = Drivers.driver
    c_driver = Drivers.c_driver
    xiaomi_c_driver = Drivers.xiaomi_c_driver
    #
    # def test_info_page_opened(self, xiaomi_c_driver):
    #     MainPage.clickInfoButton(self, xiaomi_c_driver)
    #     assert MainPage.getDeliveryTitle(self, xiaomi_c_driver) == 'Доставка'
    #     print('Test OK')


    def test_cities_page_opened(self, xiaomi_c_driver):
        MainPage.clickListRegion(self, xiaomi_c_driver)
        assert MainPage.getRegionName(self, xiaomi_c_driver) == 'Москва и область'
        print('Москва ОК')

        MainPage.clickBackButton(self, xiaomi_c_driver)
        # assert MainPage.getMyRegion(self, xiaomi_c_driver) == 'Мой регион:'

        # assert MainPage.getRegionName(self, xiaomi_c_driver) == 'Самара'
        # print('Самара ок OK')

