from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    login_icon = (By.CLASS_NAME, "link account-user")
    login_button = (By.CLASS_NAME, "login-button")
    close_popup_button = (By.CSS_SELECTOR, '.fancybox-item.fancybox-close')
    username_textbox = (By.ID, "login-email")
    password_textbox = (By.ID, "login-password-input")
    submit_button = (By.XPATH, '//*[@id="login-register"]/div[3]/div[1]/form/button/span')
# End Of Class
