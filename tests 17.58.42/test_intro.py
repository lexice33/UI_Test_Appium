import os

from pages.intro import IntroPage
from pages.main import MainPage
from tools.drivers import Drivers

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestWebViewAndroid(IntroPage, MainPage, Drivers):
    driver = Drivers.xiaomi_driver
    c_driver = Drivers.xiaomi_driver

    def test_skip_introduction(self, driver):
        # first page of introduction
        assert IntroPage.isPicturePresent(self, driver) == True
        assert IntroPage.getTitleText(self, driver) == 'Приветствуем!'
        assert IntroPage.getDescriptionText(self, driver) == 'Познакомьтесь с возможностями нового приложения'

        IntroPage.clickSkipButton(self, driver)

        # select region page
        assert IntroPage.getTitleText(self, driver) == 'Выберите свой регион'
        assert IntroPage.getDescriptionText(self,
                                            driver) == 'Для отображения актуальной информации о наличии товаров специально для Вас!'
        assert IntroPage.getDescriptionChangeText(self, driver) == 'Вы можете изменить это позже'

        IntroPage.selectRegion(self, driver)
        IntroPage.clickStartButton(self, driver)

        # check that actual region equals region we select on previous page
        assert IntroPage.getActualRegion(self, driver) == 'Санкт-Петербург'

        print('Test Passed')

    def test_pass_introduction(self, driver):
        # first page of introduction
        assert IntroPage.isPicturePresent(self, driver) == True
        assert IntroPage.getTitleText(self, driver) == 'Приветствуем!'
        assert IntroPage.getDescriptionText(self, driver) == 'Познакомьтесь с возможностями нового приложения'

        IntroPage.clickShowButton(self, driver)

        # second page of introduction
        assert IntroPage.isPicturePresent(self, driver) == True
        assert IntroPage.getTitleText(self, driver) == 'Онлайн покупки!'
        assert IntroPage.getDescriptionText(self, driver) == 'С мобильным приложением покупки стали еще проще'

        IntroPage.swipeToLeft(self, driver)

        # third page of introduction
        assert IntroPage.isPicturePresent(self, driver) == True
        assert IntroPage.getTitleText(self, driver) == 'Список покупок'
        assert IntroPage.getDescriptionText(self,
                                            driver) == 'Вы можете отложить понравившиеся товары и позже легко их найти'

        IntroPage.swipeToLeft(self, driver)

        # fourth page of introduction
        assert IntroPage.isPicturePresent(self, driver) == True
        assert IntroPage.getTitleText(self, driver) == 'Личный кабинет'
        assert IntroPage.getDescriptionText(self,
                                            driver) == 'Сохраняйте адреса доставки, списки покупок и следите за заказами.'

        IntroPage.swipeToLeft(self, driver)
        IntroPage.clickSkipButton(self, driver)

        # select region page
        assert IntroPage.getTitleText(self, driver) == 'Выберите свой регион'
        assert IntroPage.getDescriptionText(self,
                                            driver) == 'Для отображения актуальной информации о наличии товаров специально для Вас!'
        assert IntroPage.getDescriptionChangeText(self, driver) == 'Вы можете изменить это позже'

        IntroPage.selectRegion(self, driver)
        IntroPage.clickStartButton(self, driver)

        # check that actual region equals region we select on previous page
        assert IntroPage.getActualRegion(self, driver) == 'Санкт-Петербург'

        print('Test Passed')

    def test_enable_geolocation(self, driver):
        IntroPage.pass_introduction(self, driver)

        IntroPage.enable_geolocation_button(self, driver)

        assert IntroPage.getActualRegion(self, driver) == 'Курск'

    # TODO - need to add test for check case when gwolocation is enabled (https://jira.leroymerlin.ru/browse/MA-1010)
    # def test_enable_geolocation_two(self, driver_wo_gps):
    #     IntroPage.pass_introduction(self, driver_wo_gps)
    #
    #     IntroPage.enable_geolocation_button(self, driver_wo_gps)
    #
    #     assert IntroPage.getActualRegion(self, driver_wo_gps) == 'Курск'
