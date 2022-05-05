import logging

import pytest
from pytest import mark

import utilities.custom_logger as cl
from pages.login_page.login_page import LoginPage
from utilities.test_status import TestStatus


@pytest.mark.order(5)
@mark.regression
@mark.smoke
def test_ivalid_login(driver):
    log = cl.custom_logger(logging.DEBUG)
    tests_status = TestStatus(driver)
    user_login_page = LoginPage(driver)
    log.info(f"{test_ivalid_login} >>>>>>>>>>>>>>>>> started")
    user_login_page.user_login(user_login_page.WRONG_USERNAME, user_login_page.WRONG_PASSWORD)
    resultLogin = user_login_page.check_error_message("Invalid email or password.")
    tests_status.mark_final("test_ivalid_login", resultLogin, "SOME MESSAGE FOR LOGGING")
    log.info(f"{test_ivalid_login} >>>>>>>>>>>>>>>>> finished")