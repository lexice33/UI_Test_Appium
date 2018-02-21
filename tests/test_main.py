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

    def test_info_page_opened(self, c_driver):
        MainPage.clickInfoButton(self, c_driver)
        assert MainPage.getDeliveryTitle(self, c_driver) == 'Доставка'
        print('Test OK')
