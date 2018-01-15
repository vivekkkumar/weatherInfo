import unittest
import requests
import lib.weatherInfo as weatherInfo

# Arrange - creating= objects and dependencies etc,
# Act - implementing functionality,
# Assert - make claims like pass or fail.

# Note - these tests does not test the actual API and is used to test my implementation.

class test_weatherInfo(unittest.TestCase):           # subclass unittest mandatory

    def setUp(self):
        '''Creating the object instance'''
                                                                 # if setup fails tear down will not be called. This case doesn't need tear down
                                                                 # since all the objects are destroyed by python anyway

        self.appObject = weatherInfo.weatherinfo(17,23, "http://api.openweathermap.org/data/2.5/weather?id=17&appid=23")
        self.appObject.req = requests.get(self.url)

    def test_parse_message(self):
        with self.assertRaises(AttributeError):                  # Raises an key error and excepts.
            pass

    @unittest.skip("WIP")                                        # Decorator with WIP message and the test is skipped
    def test_consistence(self):
        self.assertFalse(self.appObject.is_consistent())

    def test_check_status(self):
        '''Verify '''
        self.appObject._url = "http://www.google.com"             # Checking for other values
        self.assertTrue(callable(self.appObject.block_sites))

# these below tests are not handled by the application:

    def test_flatten_regular_dict(self):
        '''Sending a dict of lists instead of dict of dicts'''

        # Expecting AttributeError, 'list' object has no attribute 'items', would not be seen in a json response.

        self.test_dict_of_lists = [{1:"hai", 2:"brb", 3:"test"}, {1:"po", 2: "da", 3: "re"}]
        self.appObject.flatten_dict(self.test_dict_of_lists)


    def test_flatten_input_dict_of_lists(self):

        '''possible to receive a regular dict'''

        # does not break

        self.test_dict = {1: "somevalue", 2: "regular value"}
        self.appObject.flatten_dict(self.test_dict)

    def test_flatten_input_dict_empty(self):
        '''Sending empty dict'''

        # does not break

        self.test_dict_emty = {}
        self.appObject.flatten_dict(self.test_dict_emty)

    def test_flattern_wrong_dataType(self):

        # Breaks, wrong data type, would not be seen in a json response.

        self.test_list = [1, 2, 2, 3, 4, ]
        self.appObject.flatten_dict(self.test_list)