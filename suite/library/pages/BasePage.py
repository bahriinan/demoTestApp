import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        self.driver.implicitly_wait(self.timeout)
    # End Of Definition

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
    # End Of Definition

    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text
    # End Of Definition

    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
    # End Of Definition

    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
    # End Of Definition

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)
    # End Of Definition

    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()
    # End Of Definition

    def find_element(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return self.driver.find_element(*by_locator)
    # End Of Definition

    def get_text_of_element(self, by_locator):
        return self.find_element(by_locator).text
    # End Of Definition

    def hit_enter_button(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.ENTER)
    # End Of Definition

    def switch_frame(self, by_locator):
        self.driver.switch_to.frame(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)))
    # End Of Definition

    def switch_default(self):
        self.driver.switch_to.default_content()
    # End Of Definition

    def find_elements(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located)
        return self.driver.find_elements(*by_locator)
    # End Of Definition
# End Of Class
