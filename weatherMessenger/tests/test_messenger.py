import unittest
import lib.messenger as messenger


# Test cases always should perform
# Arrange - creating = objects and dependencies etc,
# Act - implementing functionality,
# Assert - make claims like pass or fail.

# Note these tests does not test the actual API and is used to test my implementation.

class test_messenger(unittest.TestCase):           # subclass unittest mandatory

    def setUp(self):
        '''Fixture for creating an instance which will be used by all the methods in this class'''
                                                    # if setup fails tear down will not be called. This case doesn't need tear down
                                                    # since all the objects are destroyed by python anyway
        self.message = messenger.messenger(8765,
        7653,
        "ae365b2790e519a",
        "ab502ef59e2d")

    def test_send_message(self):                               # name of the test case
        '''Checking the exception handling in send_message method'''

        body = None
        with self.assertRaises(Exception) as test_message:
            self.message.send_message(body)

        self.assertTrue('Message Body is empty, check the api calls result', test_message.exception)