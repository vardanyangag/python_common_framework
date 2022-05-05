import json
import xml.etree.ElementTree as ET
from traceback import print_stack

import psycopg2
from selenium.webdriver.support.select import Select

from base.selenium_driver import SeleniumDriver
from utilities.util import Util

from zipfile import ZipFile
from contextlib import closing


class BasePage(SeleniumDriver):
    # Base page DOM selectors
    # Here should be selector which is appropriate for your project
    admin_menuitems_css = ".ui-menu.ui-menubar li"
    error_message_css = ".ui-messages-error"
    success_message_css = ".ui-messages-info"
    message_css = 'div[class^="ui-messages-"]'
    admin_header_menu_items_css = ".ui-link.ui-widget"
    admin_page_title_css = "#headingToolbarOuter h1"

    """
    *****
    
    Put in this class common methods which can be used in all pages in project.
    
    *****
    """

    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verify_server_title(self, title_to_verify):
        """
        Verify the page Title
        :param title_to_verify: Title on the page which needs to be verified
        """
        try:
            actual_title = self.get_title()
            return self.util.verify_text_contains(actual_title, title_to_verify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False

    def find_element_by_selector_and_text(self, selector, text):
        """
        Find the page element by selector and text
        :param selector: The selectors list
        :param text: The unique text by which the method can find exact element
        :return webElement: Search element
        """
        try:
            for domElement in selector:
                if domElement.text == text:
                    return domElement
        except:
            self.log.error("Failed to get element in the page")
            print_stack()
            return None

    def find_element_by_selector_and_text_contains(self, selector, text):
        """
        Find the page element by selector and text
        :param selector: The selectors list
        :param text: The unique text by which the method can find exact element
        :return webElement: Search element
        """
        try:
            for dom_element in selector:
                if text in dom_element.text:
                    return dom_element
        except:
            self.log.error("Failed to get element in the page")
            print_stack()
            return None

    def select_item_from_drop_down_list(self, element, option, value):
        """
        Use the method to chose item from select list
        The method uses Selenium native select class
        :param element: WebElement
        :param option: Select option, Example - index, value, text
        :param value: The appropriate option value
        :return:
        """
        try:
            select = Select(element)
            if option == "index":
                select.select_by_index(value)
            if option == "value":
                select.select_by_value(value)
            if option == "text":
                select.select_by_visible_text(value)
        except:
            self.log.error("Cant select from List")
            print_stack()

    def select_item_from_drop_down_list_using_loop(self, list_selector, list_item_selector, value):
        """
        Use the method to chose item from select list
        The method uses Selenium native select class
        :param list_selector: Drop down list selector
        :param list_item_selector: Drop down list items selector
        :param value: The appropriate option value
        :return:
        """
        try:
            el = self.get_element(list_selector)
            el.click()
            items = self.get_element_list(list_item_selector)
            for item in items:
                if item.text == value:
                    item.click()
                    break
        except:
            self.log.error("Cant select from List")
            print_stack()

    def run_query_on_postgres(self, credentials, query):
        """
        The method creates connection to POSTGRES DB and runs the query on it
        :param self: DB credentials, type - Dictionary
        :param query: SQL query
        :param credentials: Postgres DB credentials dictionary
        :return:
        """
        try:
            connection = psycopg2.connect(user=credentials['DB_USER'],
                                          password=credentials['DB_PASSWORD'],
                                          host=credentials['DB_HOST'],
                                          port="5432",
                                          database=credentials['DB_NAME'])

            QUERY = query

            cursor = connection.cursor()

            cursor.execute(QUERY)
            record = cursor.fetchall()
            return record

        except (Exception, psycopg2.Error) as error:
            self.log.info(f"Error while fetching data from PostgresSQL - {error}")
            print_stack()

        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    def browser_logger(self, method_name):
        """
        The method gets the browser log from btowser console
        :param method_name: As a param set the method name to write it in log file
        :return:
        """
        log_entries = self.driver.get_log("browser")
        logFile = open("browserConsoleLog.log", "a")
        for log_entry in log_entries:
            logFile.write(f"\n {method_name}<<<<<<< " +
                          "\n Log Level = " + log_entry['level'] +
                          "\n Log TimeStamp = " + str(log_entry["timestamp"]) +
                          "\n Log Message = " + log_entry['message'] +
                          "\n >>>>>>>")
        logFile.close()

    def replace_value_in_XML_file(self, file_path, tag, attribute, value):
        """
        Use the method to parse an XML find the tag value and change it
        :param file_path: The xml file path
        :param tag: XML tag
        :param attribute: XML tag attribute
        :param value: XML tag value which should be set
        :return:
        """
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            for transaction_set in root.iter(tag):
                transaction_set.set(attribute, value)
                tree.write(file_path)
        except:
            self.log.info(f"Unable to Change the XML tag value")
            print_stack()

    def get_value_from_XML_file(self, file_path, tag, attribute):
        """
        Use the method to parse an XML find the tag value and return it
        :param file_path: The xml file path
        :param tag: XML tag
        :param attribute: XML tag attribute
        :return tag value:
        """
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            for transaction_set in root.iter(tag):
                value = transaction_set.get(attribute)
                return value
        except:
            self.log.info(f"Unable to find the XML tag value")
            print_stack()

    def get_files_count_in_zip(self, file_path):
        """
        Use the method to get the files count from ZIP archive
        :param file_path: The ZIP file path
        :return: Count of files
        """
        try:
            with closing(ZipFile(file_path)) as archive:
                count = len(archive.infolist())
                return count
        except:
            self.log.info(f"Unable to get the archive or get files count")
            print_stack()

    def navigate_to_the_given_menu_item(self, menu_item, submenu_item=None, nested_submenu=None):
        """
        This method is designed to navigate to the given page
        :param menu_item: Menu item name
        :param submenu_item: Submenu item name
        :param nested_submenu: Nested submenu item
        :return:
        """
        admin_menu_items = self.get_element_list(self.admin_menuitems_css, "css")
        if admin_menu_items is not None:
            self.find_element_by_selector_and_text(admin_menu_items, menu_item).click()
            if submenu_item is not None:
                self.find_element_by_selector_and_text(admin_menu_items, submenu_item).click()
            if nested_submenu is not None:
                self.find_element_by_selector_and_text(admin_menu_items, nested_submenu).click()
        else:
            assert False

    def read_json(self, file_path):
        """
        This method is designed to read given json file
        :param file_path: The json file path to be read
        :return json_data: Json file data
        """
        with open(file_path) as json_file:
            json_data = json.load(json_file)
            return json_data