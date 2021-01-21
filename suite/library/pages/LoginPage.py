from suite.library.locators.login.LoginPage import LoginPageLocators
from suite.library.pages.BasePage import BasePage
from suite.library.testData.testData import DataGenerator


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.data_generator = DataGenerator()
    # End Of Definition

    def navigate_to_login_page(self):
        self.click(LoginPageLocators.close_popup_button)
        # self.hover_to(LoginPageLocators.login_icon)
        self.click(LoginPageLocators.login_button)
    # End Of  Definition

    def perform_login(self):
        self.enter_text(LoginPageLocators.username_textbox, self.data_generator.get_username())
        self.enter_text(LoginPageLocators.password_textbox, self.data_generator.get_password())
        self.click(LoginPageLocators.submit_button)
    # End Of Definition
