import pytest
from suite.library.pages.LoginPage import LoginPage
from suite.library.pages.MainPage import MainPage
from suite.library.locators.mainpage.mainpage import MainPageLocators
from suite.library.testData.testData import DataGenerator


@pytest.mark.usefixtures("test_setup")
class TestLogin():
    def test_login(self):
        driver = self.driver
        data_generator = DataGenerator()
        driver.get(data_generator.get_base_url())
        login = LoginPage(driver)
        login.navigate_to_login_page()
        login.perform_login()
        main = MainPage(driver)
        main.check_enable(MainPageLocators.first_item)
        main.navigate_page_and_check(MainPageLocators.second_item)
        main.navigate_page_and_check(MainPageLocators.third_item)
        main.navigate_page_and_check(MainPageLocators.third_item)
        main.navigate_page_and_check(MainPageLocators.fourth_item)
        main.navigate_page_and_check(MainPageLocators.fifth_item)
        main.navigate_page_and_check(MainPageLocators.sixth_item)
        main.navigate_page_and_check(MainPageLocators.seventh_item)
        main.navigate_page_and_check(MainPageLocators.eighth_item)
        main.navigate_page_and_check(MainPageLocators.ninth_item)
    # End Of Definition
# End Of Class Definition
