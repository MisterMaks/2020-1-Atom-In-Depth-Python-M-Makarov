import unittest
from multiplication_elements_list_without_current import multiplication_elements_list_without_current as mel
from unittest.mock import patch


class MyTestCase(unittest.TestCase):
    def test_mel(self):
        self.assertEqual(mel([1, 2, 3, 4]), [24, 12, 8, 6], "Should be: [24, 12, 8, 6]")
        self.assertIsNone(mel(12), "Should be: None")
        self.assertIsNone(mel("asd"), "Should be: None")
        self.assertIsNone(mel([1, 2, 3, "test", 4]), "Should be: None")
        self.assertEqual(mel([]), [], "Should be: []")
        self.assertEqual(mel([1]), [], "Should be: []")

    path_to_logging = "multiplication_elements_list_without_current." \
                      "logging"

    @patch(path_to_logging, return_value=None)
    def test_mel_2(self, logging):
        self.assertEqual(mel([1, 2, 3, 4]), [24, 12, 8, 6], "Should be: [24, 12, 8, 6]")
        self.assertIsNone(mel(12), "Should be: None")
        self.assertIsNone(mel("asd"), "Should be: None")
        self.assertIsNone(mel([1, 2, 3, "test", 4]), "Should be: None")
        self.assertEqual(mel([]), [], "Should be: []")
        self.assertEqual(mel([1]), [], "Should be: []")


if __name__ == '__main__':
    unittest.main()
