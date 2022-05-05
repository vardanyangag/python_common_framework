import time
import traceback
import random, string
import utilities.custom_logger as cl
import logging


class Util(object):
    log = cl.custom_logger(logging.INFO)

    def sleep(self, sec, info=""):
        '''
        Wait a spcified time
        :param sec:
        :param info:
        :return: None
        '''
        if info is not None:
            self.log.info(f"Wait >> {sec} seconds for {info}")
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def get_alpha_numeric(self, length, symbol_type='letters'):
        """
        Get random string of characters
        Parameters:
            length: Length of string, number of characters string should have
            symbol_type: Type of characters string should have. Default is letters
            Provide lower/upper/digits for different types
        """
        alpha_num = ''
        if symbol_type == 'lower':
            case = string.ascii_lowercase
        elif symbol_type == 'upper':
            case = string.ascii_uppercase
        elif symbol_type == 'digits':
            case = string.digits
        elif symbol_type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def get_unique_name(self, char_count=10):
        """
        Get a unique name
        """
        return self.get_alpha_numeric(char_count, 'lower')

    def get_unique_name_list(self, list_size=5, item_length=None):
        """
        Get a list of valid email ids

        Parameters:
            list_size: Number of names. Default is 5 names in a list
            item_length: It should be a list containing number of items equal to the listSize
                        This determines the length of the each item in the list -> [1, 2, 3, 4, 5]
        """
        name_list = []
        for i in range(0, list_size):
            name_list.append(self.get_unique_name(item_length[i]))
        return name_list

    def verify_text_contains(self, actual_text, expected_text):
        """
        Verify actual text contains expected text string
        Parameters:
            actual_text: Actual Text
            expected_text: Expected Text
        """
        self.log.info("Actual Text From Application Web UI --> :: " + actual_text)
        self.log.info("Expected Text From Application Web UI --> :: " + expected_text)
        if expected_text.lower() in actual_text.lower():
            self.log.info("### VERIFICATION CONTAINS !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT CONTAINS !!!")
            return False

    def verify_text_match(self, actual_text, expected_text):
        """
        Verify text match
        Parameters:
            actual_text: Actual Text
            expected_text: Expected Text
        """
        self.log.info("Actual Text From Application Web UI --> :: " + actual_text)
        self.log.info("Expected Text From Application Web UI --> :: " + expected_text)
        if actual_text.lower() == expected_text.lower():
            self.log.info("### VERIFICATION MATCHED !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT MATCHED !!!")
            return False

    def verify_list_match(self, expected_list, actual_list):
        """
        Verify two list matches

        Parameters:
            expected_list: Expected List
            actual_list: Actual List
        """
        return set(expected_list) == set(actual_list)

    def verify_list_contains(self, expected_list, actual_list):
        """
        Verify actual list contains elements of expected list
        Parameters:
            expected_list: Expected List
            actual_list: Actual List
        """
        length = len(expected_list)
        for i in range(0, length):
            if expected_list[i] not in actual_list:
                return False
        else:
            return True