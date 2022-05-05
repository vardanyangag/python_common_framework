import json
import logging
import xml.etree.ElementTree as ET
from traceback import print_stack

import jsonpath
import requests
from requests.auth import HTTPBasicAuth

import utilities.custom_logger as cl
from base.base_page import BasePage


class BaseApi(BasePage):
    """
   *****

   This class is implemented for common API methods GET PUT POST DELETE

   *****
   """

    log = cl.custom_logger(logging.DEBUG)

    # Check status code
    def check_response_status_code(self, response, status_code):
        """
        Checking the response status code
        :param response: The response object
        :param status_code: Expected status code
        """
        assert response.status_code == status_code

    # Get request JSON from file
    def get_request_json(self, file_path):
        """
        Use this method to create the request json from json file
        :param file_path: The file path in which we have added the request JSON
        :return request_json: Formatted JSON object
        """
        file = open(file_path, 'r')
        json_input = file.read()
        request_json = json.loads(json_input)
        return request_json

    # GET request
    def get_request_basic_auth(self, url, credentials, status_code=200, headers=None, params=None):
        """
        Send GET request and check the response code
        first param is the API full URL,
        credentials - the credentials map (key:value)
        status code - integer
        headers - the response headers map (key:value) OPTIONAL
        params - the response params map (key:value) OPTIONAL
        the method returns response object
        :param url: Full URL for GET request
        :param credentials: Username and Password for authentication
        :param status_code: Expected status code
        :param headers: Request header (key:value) OPTIONAL
        :param params: Request params (key:value) OPTIONAL
        :return: response
        """
        try:
            if headers is None and params is None:
                response = requests.get(url, auth=HTTPBasicAuth(credentials.get('username'),
                                                                credentials.get('password')))
                self.check_response_status_code(response, status_code)
                return response
            elif headers is not None and params is None:
                response = requests.get(url, headers=headers, auth=HTTPBasicAuth(credentials.get('username'),
                                                                                            credentials.get(
                                                                                                'password')))
                self.check_response_status_code(response, status_code)
                return response
            elif headers is None and params is not None:
                response = requests.get(url, params=params, auth=HTTPBasicAuth(credentials.get('username'),
                                                                                          credentials.get('password')))
                self.check_response_status_code(response, status_code)
                return response
            elif headers is not None and params is not None:
                response = requests.get(url, headers=headers, params=params,
                                        auth=HTTPBasicAuth(credentials.get('username'),
                                                           credentials.get('password')))
                self.check_response_status_code(response, status_code)
                return response
            else:
                self.log.error("The GET request is not sent")
                return None
        except:
            self.log.error("Error during sending GET request")
            print_stack()

    # POST request
    def post_request_basic_auth(self, url, credentials, file_path, status_code=200, headers=None, params=None):
        """
        Send POST request and check the response code
        first param is the API relative path,
        credentials - the credentials map (key:value)
        filepath - the JSON file absolute path
        status code - integer
        headers - the response headers map (key:value) OPTIONAL
        params - the response params map (key:value) OPTIONAL
        the method returns response object
        :param url: Full URL for POST request
        :param credentials: Username and Password for authentication
        :param file_path: The JSON file path for POST request body
        :param status_code: Expected status code
        :param headers: Request header (key:value) OPTIONAL
        :param params: Request params (key:value) OPTIONAL
        :return: response
        """
        request_json = self.get_request_json(file_path)
        try:
            if headers is None and params is None:
                response = requests.post(url, request_json, auth=HTTPBasicAuth(credentials.get('username'),
                                                                               credentials.get('password')))
                self.check_response_status_code(response, status_code)
                return response
            elif headers is not None and params is None:
                response = requests.post(url, request_json, headers=headers,
                                         auth=HTTPBasicAuth(credentials.get('username'),
                                                            credentials.get('password')))
                self.check_response_status_code(response, status_code)
                return response
            elif headers is None and params is not None:
                response = requests.post(url, request_json, params=params,
                                         auth=HTTPBasicAuth(credentials.get('username'),
                                                            credentials.get('password')))
                self.check_response_status_code(response, status_code)
                return response
            elif headers is not None and params is not None:
                response = requests.post(url, request_json, headers=headers, params=params,
                                         auth=HTTPBasicAuth(credentials.get('username'),
                                                            credentials.get('password')))
                self.check_response_status_code(response, status_code)
                return response
            else:
                self.log.error("The POST request is not sent")
                return None
        except:
            self.log.error("Error during sending POST request")
            print_stack()

    # PUT request
    def put_request_basic_auth(self, url, credentials, file_path, status_code=200, headers=None, params=None):
        """
        Send PUT request and check the response code
        first param is the API relative path,
        credentials - the credentials map (key:value)
        filepath - the JSON file absolute path
        status code - integer
        headers - the response headers map (key:value) OPTIONAL
        params - the response params map (key:value) OPTIONAL
        the method returns response object
        :param url: Full URL for PUT request
        :param credentials: Username and Password for authentication
        :param file_path: The JSON file path for POST request body
        :param status_code: Expected status code
        :param headers: Request header (key:value) OPTIONAL
        :param params: Request params (key:value) OPTIONAL
        :return: response
        """
        request_json = self.get_request_json(file_path)
        try:
            if headers is None and params is None:
                response = requests.put(url, request_json,
                                        auth=HTTPBasicAuth(credentials.get('username'),
                                                           credentials.get('password')))
                self.check_response_status_code(response, status_code)
                return response
            elif headers is not None and params is None:
                response = requests.put(url, request_json, headers=headers,
                                        auth=HTTPBasicAuth(credentials.get('username'),
                                                           credentials.get('password')))
                self.check_response_status_code(response, status_code)
                return response
            elif headers is None and params is not None:
                response = requests.put(url, request_json, params=params,
                                        auth=HTTPBasicAuth(credentials.get('username'),
                                                           credentials.get('password')))
                self.check_response_status_code(response, status_code)
                return response
            elif headers is not None and params is not None:
                response = requests.put(url, request_json, headers=headers, params=params,
                                        auth=HTTPBasicAuth(credentials.get('username'),
                                                           credentials.get('password')))
                self.check_response_status_code(response, status_code)
                return response
            else:
                self.log.error("The PUT request is not sent")
                return None
        except:
            self.log.error("Error during sending PUT request")
            print_stack()

    # DELETE request
    def delete_request_basic_auth(self, url, credentials, status_code=200, headers=None):
        """
        Send DELETE request and check the response code
        first param is the API relative path,
        credentials - the credentials map (key:value)
        status code - integer
        headers - the response headers map (key:value) OPTIONAL
        the method returns response object
        :param url: Full URL for DELETE request
        :param credentials: Username and Password for authentication
        :param status_code: Expected status code
        :param headers: Request header (key:value) OPTIONAL
        :return: response
        """
        try:
            if headers is None:
                response = requests.delete(url, auth=HTTPBasicAuth(credentials.get('username'),
                                                                   credentials.get('password')))
                self.check_response_status_code(response, status_code)
                return response
            elif headers is not None:
                response = requests.delete(url, headers=headers,
                                           auth=HTTPBasicAuth(credentials.get('username'),
                                                              credentials.get('password')))
                self.check_response_status_code(response, status_code)
                return response
            else:
                self.log.error("The DELETE request is not sent")
                return None
        except:
            self.log.error("Error during sending DELETE request")
            print_stack()

    def check_xml_tag_value(self, response, tag, value):
        """
        Use this method to check the XML response tag Value
        :param response: XML response
        :param tag: XML tag
        :param value: value which should be checked
        :return Boolean:
        """
        expected_value = False
        try:
            root = ET.fromstring(response.content)
            for child in root.iter('*'):
                if child.tag == tag and child.text == value:
                    expected_value = True
                    break
            assert expected_value
        except:
            self.log.error(f"Cant find expected TAG: {tag} and VALUE {value} result in the response XML")
            print_stack()
            assert False

    def check_json_key_value(self, response, key, value):
        """
        Use this method to check the JSON response tag Value
        :param response: JSON response
        :param tag: JSON tag
        :param value: value which should be checked
        :return Boolean:
        """
        expected_value = False
        try:
            json_response = json.loads(response.text)
            json_path_response = jsonpath.jsonpath(json_response, key)
            if json_path_response is not None:
                for json_key in len(json_path_response):
                    if json_key == value:
                        expected_value = True
                        break
                assert expected_value

        except:
            self.log.error(f"Cant find expected KEY: {key} and VALUE {value} result in the response JSON")
            print_stack()