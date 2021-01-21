from suite.library.pages.BasePage import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    # End Of Definition

    def check_enable(self, locator):
        self.is_enabled(locator)
    # End Of Definition

    def navigate_page_and_check(self, locator):
        self.click(locator)
        self.check_enable(locator)
    # End Of Definition
# End Of Class
