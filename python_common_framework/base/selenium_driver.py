import logging
import os
import time
from traceback import print_stack

from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import utilities.custom_logger as cl


class SeleniumDriver:
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screen_shot(self, result_message):
        """
        Takes the screenshot of the current open page
        :param result_message:
        """
        fileName = result_message + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDir = "../screenshots/"
        relFilename = screenshotDir + fileName
        currentDir = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDir, relFilename)
        destinationDirectory = os.path.join(currentDir, screenshotDir)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info(f"Screenshot caved to {destinationFile}")
        except:
            self.log.error("UNABLE TO SAVE THE SCREENSHOT")
            print_stack()

    def get_title(self):
        """
        Get the current page title
        :return: pageTitle
        """
        return self.driver.title

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            self.log.info(f"Locator type {locator_type} not correct/supported")
        return False

    def get_element(self, locator, locator_type="css"):
        """
        Use the method to get the element from DOM
        :param locator: any selenium locator
        :param locator_type: locator type which are set, by default - css
        """
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info(f"Element Found with locator {locator} and locatorType {locator_type}")
        except:
            self.log.info(f"Element NOT found with locator: {locator} and locatorType: {locator_type}")
        return element

    def get_element_list(self, locator, locator_type="css"):
        """
        Use the method to get the list of elements
        :param locator: any selenium locator
        :param locator_type: locator type which are set, by default - css
        :return: elements list
        """
        element = None
        try:
            locator_type = locator_type.lower()
            byType = self.get_by_type(locator_type)
            element = self.driver.find_elements(byType, locator)
            self.log.info(f"Element list found with locator {locator} and locator type {locator_type}")
        except:
            self.log.info(f"Element list NOT found with locator {locator} and locator type {locator_type}")

        return element

    def get_elements_nested(self, parent_webElem, child_locator, locator_type="css"):
        """
        Use the method to get elements from parent webelement
        :param parent_webElem: Selenium webElement object
        :param child_locator: Any selenium locator
        :param locator_type: locator type which are set, by default - css
        :return: elements: List of WebElements
        """
        try:
            locator_type = locator_type.lower()
            byType = self.get_by_type(locator_type)
            childElems = parent_webElem.find_elements(byType, child_locator)
            self.log.info(f"Element list found with locator {childElems} and locator type {locator_type}")
        except:
            self.log.info(f"Element list NOT found with locator {childElems} and locator type {locator_type}")

        return childElems

    def get_element_nested(self, parent_webElem, child_locator, locator_type="css"):
        """
        Use the method to get element from parent webelement
        :param parent_webElem: Selenium webElement object
        :param child_locator: Any selenium locator
        :param locator_type: locator type which are set, by default - css
        :return: element: WebElement
        """
        try:
            locator_type = locator_type.lower()
            byType = self.get_by_type(locator_type)
            child_elem = parent_webElem.find_element(byType, child_locator)

            self.log.info(f"Element list found with locator {child_elem} and locator type {locator_type}")
        except:
            self.log.info(f"Element list NOT found with locator {child_elem} and locator type {locator_type}")

        return child_elem

    def element_click(self, locator="", locator_type="css", element=None):
        """
        Click on an element
        Either provide element or a combination of locator and locatorType
        :param locator: Any selenium locator, By default - ""
        :param locator_type: locator type which are set, by default - css
        :param element: WebElement object
        :return:
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            element.click()
            self.log.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locator_type)
        except:
            self.log.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locator_type)
            print_stack()

    def element_double_click(self, element):
        """
        double Click on an element
        Either provide element
        :param element: WebElement object
        :return:
        """
        try:
            action = ActionChains(self.driver)
            action.double_click(element).perform()
        except:
            self.log.info("Cannot Doubleclick on the element")
            print_stack()

    def clear_input_fields(self, locator, locator_type="css"):
        try:
            element = self.get_element(locator, locator_type)
            element.clear()
            self.log.info(f"The field cleaned by locator: {locator} and locatorType: {locator_type}")
        except:
            self.log.info(f"Cannot find the element to clean by locator: {locator} and locatorType: {locator_type}")
            print_stack()

    def send_keys(self, data, locator="", locator_type="css", element=None):
        """
        Send keys to an element
        Either provide element or a combination of locator and locatorType
        :param data: data which should input in the field
        :param locator: Any selenium locator, By default - ""
        :param locator_type: locator type which are set, by default - css
        :param element: WebElement object
        :return:
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locator_type)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                          " locatorType: " + locator_type)
            print_stack()

    def get_text(self, locator="", locator_type="css", element=None, info=""):
        """
        Get 'Text' on an element
        :param locator: Any selenium locator, By default - ""
        :param locator_type: locator type which are set, by default - css
        :param element: WebElement object
        :param info: Info about text which should get. Default param - ""
        :return: text
        """
        try:
            if locator:  # This means if locator is not empty
                self.log.debug("In locator condition")
                element = self.get_element(locator, locator_type)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def is_element_present(self, locator="", locator_type="css", element=None):
        """
        Check if element is present
        Either provide element or a combination of locator and locatorType
        :param locator: Any selenium locator, By default - ""
        :param locator_type: locator type which are set, by default - css
        :param element: WebElement object
        :return:
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locator_type)
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locator_type)
                return False
        except:
            print("Element not found")
            return False

    def is_element_displayed(self, locator="", locator_type="css", element=None):
        """
        Check if element is displayed
        :param locator: Any selenium locator, By default - ""
        :param locator_type: locator type which are set, by default - css
        :param element: WebElement object
        :return: Boolean
        """
        is_displayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            if element is not None:
                is_displayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locatorType: " + locator_type)
            else:
                self.log.info("Element not displayed with locator: " + locator +
                              " locatorType: " + locator_type)
            return is_displayed
        except:
            print("Element not found")
            return False

    def element_presence_check(self, locator, locator_type="css"):
        """
        Check if element present in the page - Alternate solution
        :param locator: Any selenium locator, By default - ""
        :param locator_type: locator type which are set, by default - css
        :return: Boolean
        """
        try:
            elementList = self.driver.find_elements(locator_type, locator)
            if len(elementList) > 0:
                self.log.info(f"Element Found by {locator} and  {locator_type}")
                return True
            else:
                self.log.info(f"Element not found by {locator} and {locator_type}")
                return False
        except:
            self.log.info(f"Element not found by {locator} and {locator_type}")
            return False

    def wait_for_element(self, locator, locator_type="css", timeout=10, poll_frequency=0.5):
        """
        Check if element present in the page - Alternate solution
        :param locator: Any selenium locator, By default - ""
        :param locator_type: locator type which are set, by default - css
        :param timeout: maximum time of waiting, default value 10 sec
        :param poll_frequency: checking attempt frequency, default value 0.5 sec
        :return: WebElement
        """
        element = None
        try:
            byType = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info(f"Element appeared on the web page by {locator_type}")
        except:
            self.log.info(f"Element not appeared on the web page by {locator_type}")
            print_stack()
        return element

    def web_scroll(self, direction="up"):
        """
        Scroll the web page
        :param direction: direction to scroll, default - up
        :return: None
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def get_element_parent(self, locator="", locator_type="xpath"):
        """
        This method is designed to get the parent of a given element
        :param locator: The element selector the parent of which should be found. Selector type must be xpath
        :param locator_type: locator type which are set, by default - xpath
        """
        locator_type = locator_type.lower()
        byType = self.get_by_type(locator_type)
        element = self.driver.find_element(byType, locator)
        parent = element.find_element_by_xpath("..")
        return parent

    def verify_element_attribute(self, element, attr_type, attr_value):
        """
        This method is designed to verify given attribute value
        :param element: The element selector
        :param attr_type: Attribute type that should be verified
        :param attr_value: Expected attribute value
        """
        classValue = element.get_attribute(attr_type)
        assert attr_value in classValue

    def click_on_element_by_xpathtext(self, element, text, locator_type="xpath"):
        """
        This method is designed to verify given attribute value
        :param element: The element selector
        :param text: Attribute type that should be verified
        :param locator_type: locator type which are set, by default - xpath
        """
        self.element_click("//" + element + "[text()='" + text + "']", locator_type)

    def scroll_into_view(self, element, type='css'):
        """
        This method is designed to scroll the given element into the view
        :param element: The element selector that should be scrolled into the view
        :param type: selector type, Default value css
        """
        self.driver.execute_script('arguments[0].scrollIntoView(true);', self.get_element(element, type))
