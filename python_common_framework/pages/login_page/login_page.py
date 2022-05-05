from traceback import print_stack

from base.base_page import BasePage
import utilities.custom_logger as cl
import logging


class LoginPage(BasePage):
    """
    *****

    Each page should have the appropriate page methods.
    In the page class you should add the appropriate methods for that page.

    *****
    """

    log = cl.custom_logger(logging.DEBUG)

    # Admin login page selectors
    username_field_selector_css = "#user_email"
    password_field_selector_css = "#user_password"
    login_button_css = "input[value = 'Log In']"
    alert_message_css = "div[class $= 'alert-danger']"
    login_link_css = "a[class ^= 'navbar-link']"

    # Admin login page constants
    WRONG_USERNAME = "sdsd@sdsdd.sd"
    WRONG_PASSWORD = "WRONG"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def user_login(self, username, password):
        try:
            self.element_click(self.login_link_css)
            self.send_keys(username, self.username_field_selector_css)
            self.send_keys(password, self.password_field_selector_css)
            self.element_click(self.login_button_css)
        except:
            self.log.info("UNABLE TO LOGIN")
            print_stack()

    def check_error_message(self, message):
        try:
            alert_element = self.get_element(self.alert_message_css)
            if alert_element.text == message:
                return True
            else:
                return False
        except:
            self.log.info("UNABLE TO CHECK ALERT MESSAGE")
            print_stack()
