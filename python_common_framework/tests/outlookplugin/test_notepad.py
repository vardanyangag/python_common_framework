import logging

from pytest import mark

import utilities.custom_logger as cl
from pages.notepad_page.notepad_page import NotepadPage
from utilities.test_status import TestStatus


@mark.run(order=1)
@mark.outlook
def test_notepad(driver):
    log = cl.custom_logger(logging.DEBUG)
    tests_status = TestStatus(driver)
    notepad = NotepadPage(driver)

    log.info(f"{test_notepad} >>>>>>>>>>>>>>>>> started")
    login_plugin_page.pluginLogin()
    notepad.check_email_error_window()

    log.info(f"{test_notepad} >>>>>>>>>>>>>>>>> finished")
