import unittest

class FindKeyValuePair(unittest.TestCase):
    """ Given:   A key-value pair.
        Then:    When the key is given, the correct value for the key is retrieved.
        Example: For the key-value pair <Test, Success>, Test will retrieve the key-value pair "Test" "Success"
    """

    def successfully_extracts_key(self):
        # read in test file using parse method and store result and compare
        self.assertEqual("\"Key\" \"Value\"", "")

        self.assertNotEqual("\"Invalid Key\" \"Value\"", "")

    def successfully_retrieves_key_value_pair(self):
        # read in test file using parse method and store result and compare
        self.assertEqual("\"Key\" \"Value\"", "")

        self.assertNotEqual("\"Invalid Key\" \"Value\"", "")