import logging
from traceback import print_stack

import utilities.custom_logger as cl
from base.base_page import BasePage
from utilities.util import Util


class NotepadPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    # Plugin login page selectors
    notepad_text_field_name = "NOTEAPD TEXT FIELD NAME"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def pluginLogin(self):
        utils_page = Util()
        try:
            utils_page.sleep(3, "Waiting for Notepad")
            self.wait_for_element(self.notepad_text_field_name, 'name')
            self.send_keys("some keys in text field")
        except:
            self.log.info("EXCEPTION MESSAGE")
            print_stack()
