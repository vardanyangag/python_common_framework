import logging
import os

import pytest
from pytest import fixture
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import utilities.custom_logger as cl
from tests.config import Config
from utilities.test_status import TestStatus


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        default="qa",
        action="store",
        help="Set the environment URL's"
    )
    parser.addoption(
        "--api",
        default="api_env",
        action="store",
        help="Set the api environment"
    )
    parser.addoption(
        "--browser",
        default="chrome",
        action="store",
        help="Set the browser type"
    )


@fixture(scope='session')
def get_env_url(request):
    return request.config.getoption("--env")


@fixture(scope='session')
def get_api_env_url(request):
    return request.config.getoption("--api")

@fixture(scope='session')
def get_browser_type(request):
    return request.config.getoption("--browser")


@fixture(scope='session')
def app_config(get_env_url, get_api_env_url, get_browser_type):
    cfg = Config(get_env_url, get_api_env_url, get_browser_type)
    return cfg


@pytest.fixture
def logger_inst():
    log = cl.custom_logger(logging.DEBUG)
    return log


@pytest.fixture
def test_status_inst():
    tests_status = TestStatus(driver)
    return tests_status

@pytest.fixture(scope='session')
def config_wait_time():
    return 30


@pytest.fixture
def driver(config_wait_time, app_config):
    browser_type = app_config.browser
    if browser_type == 'chrome' or browser_type == 'api':
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options = webdriver.ChromeOptions()
        path = os.path.abspath(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)) + '\\drivers\\chromedriver.exe'
        options.add_argument('--ignore-certificate-errors')
        caps = DesiredCapabilities.CHROME
        caps['goog:loggingPrefs'] = {'browser': 'ALL'}
        driver = webdriver.Chrome(path, options=options, desired_capabilities=caps)
    elif browser_type == 'firefox':
        driver = webdriver.Firefox()
    elif browser_type == 'ie':
        driver = webdriver.Ie
    elif browser_type == 'notepad':
        notepad_url = app_config.base_url + app_config.admin_port
        driver = webdriver.Remote(
            command_executor=notepad_url,
            desired_capabilities={
                "debugConnectToRunningApp": 'false',
                "app": r"C:\\Windows\\System32\\notepad.exe"
            })
    else:
        raise Exception(f"{browser_type} is not a supported browser")
    if browser_type != 'outlook':
        driver.implicitly_wait(config_wait_time)

        driver.maximize_window()

        admin_base_url = app_config.base_url + app_config.admin_port
        driver.get(admin_base_url)

    yield driver
    if browser_type != 'outlook':
        log_entries = driver.get_log("browser")
        logFile = open("../browserConsoleLog.log", "a")
        for log_entry in log_entries:
            logFile.write(f"\n <<<<<<< " +
                          "\n Log Level = " + log_entry['level'] +
                          "\n Log TimeStamp = " + str(log_entry["timestamp"]) +
                          "\n Log Message = " + log_entry['message'] +
                          "\n >>>>>>>")
        logFile.close()

    driver.quit()


@pytest.fixture
def open_webuser_tab(driver, app_config):
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])

    user_base_url = app_config.base_url + app_config.user_port
    driver.get(user_base_url)
    driver.switch_to.window(driver.window_handles[0])